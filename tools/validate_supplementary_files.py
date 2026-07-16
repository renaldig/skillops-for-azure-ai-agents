from __future__ import annotations

import json
import py_compile
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

required = [
    'Chapter_03/skillops-chapter3-lab/.github/skills/azure-deployment-review/SKILL.md',
    'Chapter_03/skillops-chapter3-lab/.vscode/mcp.json',
    'Chapter_06/skillops-chapter-6/.azure/deployment-plan.md',
    'Chapter_06/skillops-deployment-review-agent/src/skillops-toolbox-agent/main.py',
    'Chapter_06/skillops-deployment-review-agent/src/skillops-toolbox-agent/Dockerfile',
    'Chapter_08/policy-retrieval-hosted-agent/src/skillops-toolbox-agent/main.py',
    'Chapter_08/policy-retrieval-hosted-agent/src/skillops-toolbox-agent/Dockerfile',
    'Chapter_08/policy-retrieval-hosted-agent/src/skillops-toolbox-agent/toolbox.yaml',
    'Chapter_08/sample-policy-documents/parental-leave.txt',
    'Chapter_09/evaluations/foundry-skill-evaluation.jsonl',
    'Chapter_10/governance/hosted-agent-release-record.md',
]
for rel in required:
    if not (ROOT / rel).is_file(): errors.append(f'Missing required file: {rel}')

for path in ROOT.rglob('*.json'):
    try: json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'Invalid JSON {path.relative_to(ROOT)}: {exc}')

for path in ROOT.rglob('*.jsonl'):
    for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip(): continue
        try: json.loads(line)
        except Exception as exc: errors.append(f'Invalid JSONL {path.relative_to(ROOT)} line {i}: {exc}')

for path in [*ROOT.rglob('*.yaml'), *ROOT.rglob('*.yml')]:
    try: yaml.safe_load(path.read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f'Invalid YAML {path.relative_to(ROOT)}: {exc}')

skill_names: dict[str, list[str]] = {}
for path in ROOT.rglob('SKILL.md'):
    # The intentionally weak Chapter 4 input demonstrates bad naming and is not a valid deployable skill.
    if 'Chapter_04/weak-draft/' in path.as_posix():
        continue
    text = path.read_text(encoding='utf-8')
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.S)
    if not match:
        errors.append(f'Missing YAML front matter: {path.relative_to(ROOT)}')
        continue
    try: meta = yaml.safe_load(match.group(1)) or {}
    except Exception as exc:
        errors.append(f'Invalid skill front matter {path.relative_to(ROOT)}: {exc}')
        continue
    name = meta.get('name')
    desc = meta.get('description')
    if not name or not desc: errors.append(f'Skill missing name/description: {path.relative_to(ROOT)}')
    if name and path.parent.name != name:
        errors.append(f'Skill folder/name mismatch: {path.relative_to(ROOT)} -> {name}')
    skill_names.setdefault(str(name), []).append(str(path.relative_to(ROOT)))

for path in ROOT.rglob('*.py'):
    if path.name == 'validate_supplementary_files.py': continue
    try: py_compile.compile(str(path), doraise=True)
    except Exception as exc: errors.append(f'Python syntax error {path.relative_to(ROOT)}: {exc}')

if errors:
    print('\n'.join(f'ERROR: {e}' for e in errors))
    sys.exit(1)
print(f'Validation passed. Checked {sum(1 for p in ROOT.rglob("*") if p.is_file())} files.')
