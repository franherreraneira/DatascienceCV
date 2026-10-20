"""Functional and model checks. Run: python3 tests/validate.py.
Uses the system Chromium and Playwright. No packages required by the game.
"""
from pathlib import Path
import json
import os
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get('CITY_TEST_OUTPUT', '/tmp/ciudades-validation'))
OUT.mkdir(parents=True, exist_ok=True)
HTML = (ROOT / 'Ciudades-al-azar.html').read_text()
passed = []

def check(name, condition):
    assert condition, name
    passed.append(name)
    print('PASS:', name)

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=os.environ.get('CHROMIUM', '/usr/bin/chromium'), headless=True, args=['--no-sandbox'])
    context = browser.new_context(offline=True, viewport={'width': 1366, 'height': 768})
    page = context.new_page()
    errors, requests = [], []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.on('request', lambda request: requests.append(request.url))
    # This managed Chromium blocks file:// by policy. Load the exact standalone
    # file as document content in a network-offline context instead.
    page.clock.install()
    page.clock.pause_at(1000000000000)
    page.set_content(HTML)
    page.clock.run_for(20)
    check('Offline landing loads', page.locator('#welcome').is_visible())
    page.screenshot(path=str(OUT / '01-welcome.png'))
    page.locator('#startBtn').click()
    page.locator('[data-pi="0.05"]').click()
    page.locator('[data-predict="unequal"]').click()
    check('Player changes pi before growth', page.evaluate('CityGame.getState().pi') == .05)
    page.locator('#nextBtn').click()
    check('Simon begins with ten seeds', page.evaluate('CityGame.snapshot().model.population') == 10)
    page.clock.fast_forward(75000)
    # flush one animation frame, independent of paint throttling
    page.clock.run_for(20)
    snap = page.evaluate('CityGame.snapshot()')
    check('Simon reaches 1000 units before comparison', snap['model']['population'] == 1000 and snap['phase'] == 2)
    check('Population is conserved, cities are positive integers', sum(c['pop'] for c in snap['model']['cities']) == 1000 and all(c['pop'] >= 1 and isinstance(c['pop'], int) for c in snap['model']['cities']))
    page.locator('#compareBtn').click()
    check('Alternative parameter series is visible', page.locator('#altLegend').is_visible() and '20 %' in page.locator('#altName').inner_text())
    page.locator('#citySelect').select_option('1')
    check('Keyboard-accessible city selector updates map detail', 'San Miguel' in page.locator('#selection').inner_text())
    page.locator('#chart').focus()
    page.keyboard.press('ArrowRight')
    check('Graph supports keyboard selection', page.evaluate('CityGame.getState().selected') != 1)
    top_id = page.evaluate('CityModel.sorted(CityGame.snapshot().model)[0].id')
    page.locator('#chart').click(position={'x': 48, 'y': 16})
    check('Clicking the top graph point selects its city', page.evaluate('CityGame.getState().selected') == top_id)
    page.screenshot(path=str(OUT / '02-comparison.png'))
    page.locator('#nextBtn').click()
    page.locator('#citySelect').select_option('0')
    page.locator('[data-plan="market"]').click()
    page.locator('#lockBtn').click()
    page.locator('#citySelect').select_option('1')
    check('Inspecting another city does not move a locked intervention', page.evaluate('CityGame.getState().target') == 0 and page.evaluate('CityGame.getState().selected') == 1)
    page.clock.fast_forward(58000)
    page.clock.run_for(20)
    snap = page.evaluate('CityGame.snapshot()')
    check('Both branches receive exactly 1000 additional units', snap['phase'] == 4 and snap['model']['population'] == snap['control']['population'] == 2000)
    check('Birth draws match between branches', len(snap['model']['cities']) == len(snap['control']['cities']))
    check('Market changes the target relative to its paired control', snap['model']['cities'][0]['pop'] > snap['control']['cities'][0]['pop'])
    page.locator('[data-q="1"][data-a="wrong"]').click()
    check('Incorrect answers receive conceptual feedback', 'E[ΔS' in page.locator('#feedback1').inner_text())
    page.locator('[data-q="1"][data-a="right"]').click()
    page.locator('[data-q="2"][data-a="right"]').click()
    check('Both learning questions accept correct answers', page.evaluate('CityGame.snapshot().answers') == {'1': 'right', '2': 'right'})
    page.screenshot(path=str(OUT / '03-conclusions.png'))
    page.clock.fast_forward(40000)
    page.clock.run_for(20)
    check('Conclusion ends and remains available', page.evaluate('CityGame.snapshot().finished') and page.locator('#timer').inner_text() == '0:00')
    with page.expect_download() as download_info:
        page.locator('#downloadBtn').click()
    download_info.value.save_as(OUT / 'result.json')
    exported = json.loads((OUT / 'result.json').read_text())
    check('Result export contains reproducible seed and intervention', exported['seed'] == 1955 and exported['intervention']['weight'] == 2 and exported['finished'])
    page.locator('#sourceBtn').click()
    check('Academic source dialog opens', page.locator('#sources').is_visible())
    page.locator('#closeSources').click()
    page.locator('#restartBtn').click()
    check('Restart uses a new seed and resets state', page.evaluate('CityGame.snapshot().seed') != 1955 and page.locator('#welcome').is_visible())
    page.locator('#startBtn').click()
    page.clock.fast_forward(240000)
    page.clock.run_for(20)
    fresh = page.evaluate('CityGame.snapshot()')
    check('Full unattended sequence finishes within 240 seconds', fresh['finished'] and fresh['phase'] == 4)
    check('No intervention is exactly identical to control', fresh['model'] == fresh['control'])
    model_checks = page.evaluate('''() => {
      const M=CityModel;
      let m=M.initial(); M.step(m,.2,.1,.9);
      const birth=m.population===11&&m.cities.length===11&&m.cities[10].pop===1;
      let initial={cities:[{id:0,pop:10},{id:1,pop:20}],population:30};
      // Repeated independent assignments at a fixed state estimate the conditional
      // 1:2 allocation probability; weights change it to 1:1 for target zero.
      let random=M.rng(987),plain=0,weighted=0,N=30000;
      for(let n=0;n<N;n++){
        let u=random(),a=M.clone(initial),b=M.clone(initial);
        M.step(a,0,1,u); M.step(b,0,1,u,0,2);
        plain+=a.cities[0].pop===11; weighted+=b.cities[0].pop===11;
      }
      let a=M.simulate(.2,1955),b=M.simulate(.2,1955),c=M.simulate(.2,1956);
      let rare=M.simulate(.05,1955);
      return {birth,plain:plain/N,weighted:weighted/N,
        replay:JSON.stringify(a)===JSON.stringify(b),
        distinct:JSON.stringify(a)!==JSON.stringify(c),
        moreBirths:a.cities.length>rare.cities.length};
    }''')
    check('Birth creates a city of one indivisible unit', model_checks['birth'])
    check('Conditional assignment is proportional to size', abs(model_checks['plain'] - 1/3) < .015)
    check('Territorial weights alter only conditional assignment', abs(model_checks['weighted'] - .5) < .015)
    check('Seed replays exactly and another seed changes the history', model_checks['replay'] and model_checks['distinct'])
    check('Higher pi produces more cities in the paired experiment', model_checks['moreBirths'])
    check('1366px layout has no horizontal overflow', page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
    # Projection screenshots at each phase, including dense conclusions.
    check('Conclusion and footer fit 1366 × 768', page.locator('footer').bounding_box()['y'] + page.locator('footer').bounding_box()['height'] <= 769)
    page.locator('#projectorBtn').click()
    page.screenshot(path=str(OUT / '04-projection.png'))
    check('Projection mode also fits 1366 × 768', page.locator('footer').bounding_box()['y'] + page.locator('footer').bounding_box()['height'] <= 769)
    page.locator('#projectorBtn').click()
    page.locator('#restartBtn').click()
    page.locator('#startBtn').click()
    for stage in range(4):
        check(f'Phase {stage + 1} fits the projection viewport', page.locator('footer').bounding_box()['y'] + page.locator('footer').bounding_box()['height'] <= 769)
        if stage < 3:
            page.locator('#nextBtn').click()
    page.locator('#citySelect').select_option('0')
    page.locator('[data-plan="congestion"]').click()
    page.locator('#lockBtn').click()
    page.locator('#nextBtn').click()
    congested = page.evaluate('CityGame.snapshot()')
    check('Congestion decreases the chosen city relative to its control', congested['model']['cities'][0]['pop'] < congested['control']['cities'][0]['pop'])
    page.set_viewport_size({'width': 390, 'height': 844})
    page.screenshot(path=str(OUT / '05-mobile.png'), full_page=True)
    check('390px layout has no horizontal overflow', page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
    check('No external resource requests, with networking disabled', not requests)
    check('No JavaScript errors across the full game', not errors)
    (OUT / 'report.json').write_text(json.dumps({'passed':passed,'model_checks':model_checks,'errors':errors,'requests':requests},ensure_ascii=False,indent=2))
    browser.close()
print(f'\n{len(passed)} checks passed. Artifacts: {OUT}')
