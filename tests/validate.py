"""Functional and probabilistic checks for the guided, offline game.
Run: python3 tests/validate.py (development requires Playwright and Chromium).
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
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('request', lambda r: requests.append(r.url))
    page.clock.install()
    page.clock.pause_at(1000000000000)
    # Managed Chromium blocks file://. Execute the exact document offline.
    page.set_content(HTML)
    page.clock.run_for(20)
    check('Offline welcome shows three short steps', page.locator('#welcome').is_visible() and page.locator('.intro-steps span').count() == 3)
    page.screenshot(path=str(OUT / '01-welcome.png'))
    page.locator('#startBtn').click()
    check('Game has three phases and begins with ten equal cities', page.locator('.steps li').count() == 3 and all(c['pop'] == 1 for c in page.evaluate('CityGame.snapshot().model.cities')))
    check('Main instructions use one in five, without a parameter choice', 'Uno de cada cinco' in page.locator('#coachText').inner_text() and 'π' not in page.locator('body').inner_text())
    check('Graph and comparison controls are disclosed later', not page.locator('#graphBtn').is_visible() and not page.locator('#comparisonTabs').is_visible())
    page.clock.fast_forward(65000)
    page.clock.run_for(20)
    check('Growth reaches 1000 groups before the first decision', page.evaluate('CityGame.snapshot().model.population') == 1000 and page.evaluate('CityGame.getState().phase') == 0)
    check('Zipf is introduced as half and one third', 'la mitad y un tercio' in page.locator('#coachTitle').inner_text() and 'no tienen que coincidir' in page.locator('#coachText').inner_text())
    check('Only the three largest cities are shown in the default comparison', page.locator('#bars .bar-row').count() == 3)
    geometry = page.evaluate('''() => Array.from(document.querySelectorAll('#bars .bar-row')).map(row=>({
       track:row.querySelector('.bar-track').getBoundingClientRect().width,
       fill:row.querySelector('.bar-fill').getBoundingClientRect().width,
       marker:parseFloat(row.querySelector('.zipf-mark').style.left),
       id:Number(row.dataset.city)
    }))''')
    snap = page.evaluate('CityGame.snapshot()')
    largest = max(c['pop'] for c in snap['model']['cities'])
    check('Population bars have a visible, accurately scaled width', all(g['track'] > 200 and abs(g['fill']/g['track'] - snap['model']['cities'][g['id']]['pop']/largest) < .01 for g in geometry))
    check('Zipf markers show half and a third of the largest city', abs(geometry[1]['marker'] - 50) < .01 and abs(geometry[2]['marker'] - 100/3) < .01)
    top_id = geometry[0]['id']
    page.locator('#bars .bar-row').first.click()
    check('Selecting a population bar selects the same city on the map', page.evaluate('CityGame.getState().selected') == top_id)
    page.locator('#graphBtn').click()
    check('Logarithmic rank-size chart remains available on request', page.locator('#logPanel').is_visible() and not page.locator('#sizeBars').is_visible())
    page.locator('#chart').focus()
    previous = page.evaluate('CityGame.getState().selected')
    page.keyboard.press('ArrowRight')
    check('Rank-size chart supports keyboard selection', page.evaluate('CityGame.getState().selected') != previous)
    page.locator('#graphBtn').click()
    page.screenshot(path=str(OUT / '02-zipf.png'))
    page.locator('#nextBtn').click()
    check('Decision shows exactly two choices and hides the charts', page.locator('#decision .choice').count() == 2 and not page.locator('#sizePanel').is_visible() and page.locator('#nextBtn').is_disabled())
    page.locator('#citySelect').select_option('0')
    page.locator('#marketBtn').click()
    check('One click installs the market and locks its target', page.evaluate('CityGame.getState().locked') and page.evaluate('CityGame.snapshot().intervention.weight') == 2)
    page.locator('#citySelect').select_option('1')
    check('Inspecting another city does not move the market', page.evaluate('CityGame.getState().target') == 0 and page.evaluate('CityGame.getState().selected') == 1)
    page.clock.fast_forward(90000)
    page.clock.run_for(20)
    snap = page.evaluate('CityGame.snapshot()')
    check('Paired branches receive the same total population and foundation draws', snap['phase'] == 2 and snap['model']['population'] == snap['control']['population'] == 2000 and len(snap['model']['cities']) == len(snap['control']['cities']))
    check('Market changes its city relative to the paired control', snap['model']['cities'][0]['pop'] > snap['control']['cities'][0]['pop'])
    check('Results compare one city in two versions, without showing everything at once', page.locator('#resultBars').is_visible() and not page.locator('#sizePanel').is_visible() and 'dos versiones' in page.locator('#coachTitle').inner_text())
    page.locator('[data-answer="yes"]').click()
    check('Misconception receives feedback instead of a score', 'no demuestra su causa' in page.locator('#feedback').inner_text())
    page.locator('[data-answer="no"]').click()
    check('Critical conclusion distinguishes pattern from cause', 'Distintos procesos' in page.locator('#feedback').inner_text())
    page.screenshot(path=str(OUT / '03-result.png'))
    page.locator('#zipfTab').click()
    check('Final Zipf comparison can be explored separately', page.locator('#sizeBars').is_visible() and not page.locator('#resultBars').is_visible())
    page.locator('#graphBtn').click()
    page.locator('#chart').click(position={'x':48, 'y':16})
    check('Clicking the top chart point selects the largest city', page.evaluate('CityGame.getState().selected') == page.evaluate('CityModel.sorted(CityGame.snapshot().model)[0].id'))
    page.locator('#resultTab').click()
    page.clock.fast_forward(70000)
    page.clock.run_for(20)
    check('The complete game ends automatically in at most 240 seconds', page.evaluate('CityGame.snapshot().finished') and page.locator('#timer').inner_text() == '0:00')
    page.locator('#sourceBtn').click()
    check('Equations, assumptions and limits remain available in academic details', page.locator('#sources').is_visible() and '1 / (1 − π)' in page.locator('#sources').inner_text())
    with page.expect_download() as info:
        page.locator('#downloadBtn').click()
    info.value.save_as(OUT / 'result.json')
    exported = json.loads((OUT / 'result.json').read_text())
    check('Export retains the seed, parameter and intervention', exported['version'] == 2 and exported['pi'] == .2 and exported['intervention']['weight'] == 2 and exported['finished'])
    page.locator('#closeSources').click()
    check('Standard layout fits a 1366 by 768 projection', page.locator('footer').bounding_box()['y'] + page.locator('footer').bounding_box()['height'] <= 768)
    page.locator('#projectorBtn').click()
    check('Larger projection text fits the viewport', page.locator('footer').bounding_box()['y'] + page.locator('footer').bounding_box()['height'] <= 768)
    page.screenshot(path=str(OUT / '04-projection.png'))
    page.locator('#projectorBtn').click()
    page.locator('#restartBtn').click()
    check('Restart resets the experiment with a new seed', page.evaluate('CityGame.snapshot().seed') != 1955 and page.evaluate('CityGame.snapshot().control') is None)
    page.locator('#startBtn').click()
    page.clock.fast_forward(240000)
    page.clock.run_for(20)
    unattended = page.evaluate('CityGame.snapshot()')
    check('Unattended decision defaults to no intervention', unattended['finished'] and unattended['intervention']['plan'] == 'neutral' and unattended['model'] == unattended['control'])
    page.locator('#restartBtn').click()
    page.locator('#startBtn').click()
    page.locator('#nextBtn').click()
    page.locator('#neutralBtn').click()
    page.locator('#nextBtn').click()
    neutral = page.evaluate('CityGame.snapshot()')
    check('Explicitly leaving things unchanged gives identical paired results', neutral['model'] == neutral['control'])
    page.locator('#nextBtn').click()
    check('Early completion preserves results', page.evaluate('CityGame.snapshot().finished'))
    model_checks = page.evaluate('''() => {
      const M=CityModel; let m=M.initial(); M.step(m,.2,.1,.9);
      const birth=m.population===11&&m.cities.length===11&&m.cities[10].pop===1;
      let initial={cities:[{id:0,pop:10},{id:1,pop:20}],population:30};
      let rng=M.rng(987),plain=0,weighted=0,N=30000;
      for(let n=0;n<N;n++){let u=rng(),a=M.clone(initial),b=M.clone(initial);M.step(a,0,1,u);M.step(b,0,1,u,0,2);plain+=a.cities[0].pop===11;weighted+=b.cities[0].pop===11;}
      let a=M.simulate(.2,1955),b=M.simulate(.2,1955),c=M.simulate(.2,1956);
      return{birth,plain:plain/N,weighted:weighted/N,replay:JSON.stringify(a)===JSON.stringify(b),distinct:JSON.stringify(a)!==JSON.stringify(c),population:a.population,sum:a.cities.reduce((s,c)=>s+c.pop,0),positive:a.cities.every(c=>Number.isInteger(c.pop)&&c.pop>=1)};
    }''')
    check('Every founding event creates one indivisible group', model_checks['birth'])
    check('Conditional assignment remains proportional to population', abs(model_checks['plain'] - 1/3) < .015)
    check('Territorial weight changes conditional attraction as specified', abs(model_checks['weighted'] - .5) < .015)
    check('Same seed replays exactly and different seeds change the history', model_checks['replay'] and model_checks['distinct'])
    check('Population is conserved and city sizes stay positive integers', model_checks['population'] == model_checks['sum'] == 1000 and model_checks['positive'])
    page.set_viewport_size({'width':390,'height':844})
    page.screenshot(path=str(OUT / '05-mobile.png'),full_page=True)
    check('Mobile layout has no horizontal overflow', page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
    check('Standalone entry and named game are identical', (ROOT / 'index.html').read_text() == HTML)
    check('Offline play makes no external network requests', not requests)
    check('All interactions run without JavaScript errors', not errors)
    (OUT / 'report.json').write_text(json.dumps({'version':2,'passed':passed,'model_checks':model_checks,'errors':errors,'requests':requests},ensure_ascii=False,indent=2))
    browser.close()
print(f'\n{len(passed)} checks passed. Artifacts: {OUT}')
