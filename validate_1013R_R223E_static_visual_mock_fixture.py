import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent
checks = []
def check(name, cond, detail=''):
    checks.append({'name': name, 'passed': bool(cond), 'detail': detail})
html = (ROOT / 'R223E_static_visual_mock_fixture.html').read_text(encoding='utf-8')
state = json.loads((ROOT / 'R223E_static_visual_mock_state.json').read_text(encoding='utf-8'))
check('stage_id', state.get('stage_id') == '1013R_R223E_STATIC_VISUAL_MOCK_FIXTURE')
for key in ['ui_implementation','r97b_modified','frontend_backend_modified','runtime_enabled','provider_model_prompt_db','formal_apply']:
    check(f'{key}_false', state.get(key) is False)
for item in ['prep_canvas','focused_section_card','current_component_suggestion_strip']:
    check(f'default open: {item}', item in state.get('default_open', []))
for item in ['ordinary_source_assumptions','ordinary_material_gaps','full_reasoning_chain','non_selected_component_bindings']:
    check(f'default collapsed: {item}', item in state.get('default_collapsed', []))
check('daily_component_count_3', state.get('daily_component_count') == 3)
check('quick_component_count_2', state.get('quick_component_count') == 2)
check('html body stage marker', 'data-stage="R223E"' in html)
check('html says no r97b', 'data-r97b-modified="false"' in html)
check('html says no runtime', 'data-runtime="false"' in html)
check('primary canvas marker', 'data-primary-reading-object="true"' in html)
check('high risk visible marker', 'data-high-risk-visible="true"' in html)
check('selected component only binding', 'data-open-policy="selected_component_only"' in html)
check('daily max marker', 'data-max-components-daily="3"' in html)
check('quick max marker', 'data-max-components-quick="2"' in html)
check('not toolbox marker', 'data-not-toolbox="true"' in html)
check('non chat marker', 'data-non-chat="true"' in html)
component_ids = re.findall(r'data-component-id="([^"]+)"', html)
check('daily components include expected', all(x in component_ids for x in ['material_mystery_box','technique_step_demo','learning_sheet_record']))
check('quick components include expected', component_ids.count('technique_step_demo') >= 2 and component_ids.count('learning_sheet_record') >= 2)
for forbidden in ['问我任何问题','继续聊天生成','component marketplace','open component marketplace']:
    check(f'forbidden text absent: {forbidden}', forbidden not in html)
required_files = ['R223E_static_visual_mock_spec.md','R223E_static_visual_mock_fixture.html','R223E_density_compliance_check.md','R223E_report.md','README_FOR_GPT_REVIEW.md']
for name in required_files:
    check(f'file exists: {name}', (ROOT / name).exists())
smoke_json_path = ROOT / 'R223E_screenshot_smoke_result.json'
smoke_md_path = ROOT / 'R223E_screenshot_smoke_result.md'
screenshot_path = ROOT / 'R223E_static_visual_mock_screenshot.png'
check('file exists: R223E_screenshot_smoke_result.json', smoke_json_path.exists())
check('file exists: R223E_screenshot_smoke_result.md', smoke_md_path.exists())
check('file exists: R223E_static_visual_mock_screenshot.png', screenshot_path.exists())
if smoke_json_path.exists():
    smoke = json.loads(smoke_json_path.read_text(encoding='utf-8'))
    check('screenshot smoke passed', smoke.get('passed') is True)
    check('screenshot smoke daily max respected', 0 < smoke.get('dailyComponentCount', 0) <= 3)
    check('screenshot smoke quick max respected', 0 < smoke.get('quickComponentCount', 0) <= 2)
    check('screenshot smoke high risk visible', smoke.get('highRiskVisible') is True)
    check('screenshot smoke ordinary gaps folded', smoke.get('ordinaryGapsFolded') is True)
    check('screenshot smoke selected binding only', smoke.get('selectedOnlyBinding') is True)
    check('screenshot smoke bottom non chat', smoke.get('bottomNonChat') is True)
    check('screenshot smoke no shelf marker', smoke.get('noGlobalComponentShelf') is True)
    check('screenshot smoke no chat marker', smoke.get('noChatPlaceholder') is True)
    check('screenshot smoke no forbidden chat text', smoke.get('forbiddenChat') == [])
    check('screenshot smoke no horizontal overflow', smoke.get('bodyScrollWidth', 0) <= smoke.get('bodyClientWidth', 0) + 4)
    check('screenshot smoke image nonempty', smoke.get('screenshotBytes', 0) > 10000)
else:
    smoke = {}
if screenshot_path.exists():
    check('screenshot png nonempty', screenshot_path.stat().st_size > 10000)
result = {'passed': all(c['passed'] for c in checks), 'check_count': len(checks), 'failed': sum(1 for c in checks if not c['passed']), 'failed_checks': [c for c in checks if not c['passed']]}
(ROOT / 'validate_1013R_R223E_static_visual_mock_fixture_result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False))
raise SystemExit(0 if result['passed'] else 1)
