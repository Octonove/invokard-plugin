"""Builds the directory edition of Invokard: the plugin that Anthropic's directory (claude.ai/directory) accepts
from an organization it has not verified, which is Markdown, text, JSON, YAML and images only.

It keeps the 55 skills and leaves out what the directory takes only from verified organizations: the SessionStart
hook (hooks/), the CRBRO MCP server (.mcp.json), the rules exported for other editors (rules/) and the
agent-plugins manifest (plugin.json at the root). The README is tools/directory/README.md.

.github/workflows/directory-edition.yml runs this on every push to main and commits the result to the `directory`
branch, the branch the directory tracks. To look at it locally:

    python tools/directory_edition.py <empty or new folder>
"""
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools', 'directory')

DESCRIPTION = ('Fifty-five working roles for Claude as skills, and the rules that route between them. '
               'Text only: no code, no connections. Free.')
DROP_KEYWORDS = {'memory', 'crbro', 'mcp'}
ALLOWED = ('.md', '.txt', '.json', '.yml', '.yaml', '.png', '.jpg', '.jpeg', '.gif', '.webp')
IMAGES = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
FORBIDDEN_NAMES = {'hooks.json', '.mcp.json', '.lsp.json', 'monitors.json', 'package.json', '.npmrc'}
# What the edition must not claim: in this edition nothing is installed, loaded on its own or run.
FORBIDDEN_TEXT = ('that this plugin installs', 'SessionStart', 'session-start.js')

PATCHES = {
    # The CRBRO card says the plugin installs the server; this edition does not.
    os.path.join('skills', 'zero-crbro', 'SKILL.md'): [
        ('Uses the CRBRO MCP server that this plugin installs.',
         'Uses the CRBRO MCP server, installed separately (github.com/Octonove/crbro-memory).'),
    ],
}


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def manifest(name, describe):
    data = json.loads(read(os.path.join(ROOT, '.claude-plugin', name)))
    describe(data)
    return json.dumps(data, indent=2, ensure_ascii=False) + '\n'


def plugin_entry(entry):
    entry['description'] = DESCRIPTION
    entry['keywords'] = [k for k in entry.get('keywords', []) if k not in DROP_KEYWORDS]


def build(out):
    if os.path.isdir(out) and os.listdir(out):
        raise SystemExit(f'{out} is not empty: give a new or empty folder')

    shutil.copytree(os.path.join(ROOT, 'skills'), os.path.join(out, 'skills'))
    for rel, pairs in PATCHES.items():
        path = os.path.join(out, rel)
        text = read(path)
        for old, new in pairs:
            if text.count(old) != 1:
                raise SystemExit(f'{rel}: expected one match for {old!r}')
            text = text.replace(old, new)
        write(path, text)

    shutil.copyfile(os.path.join(ROOT, 'LICENSE'), os.path.join(out, 'LICENSE'))
    shutil.copyfile(os.path.join(HERE, 'README.md'), os.path.join(out, 'README.md'))
    os.makedirs(os.path.join(out, '.claude-plugin'), exist_ok=True)
    shutil.copyfile(os.path.join(ROOT, '.claude-plugin', 'icon.png'), os.path.join(out, '.claude-plugin', 'icon.png'))

    version = json.loads(read(os.path.join(ROOT, '.claude-plugin', 'plugin.json')))['version']

    def market(data):
        data['description'] = ("Invokard's marketplace, directory edition: fifty-five working roles for Claude "
                               'as skills. Text only.')
        for entry in data['plugins']:
            plugin_entry(entry)
            entry['version'] = version

    write(os.path.join(out, '.claude-plugin', 'plugin.json'), manifest('plugin.json', plugin_entry))
    write(os.path.join(out, '.claude-plugin', 'marketplace.json'), manifest('marketplace.json', market))


def audit(out):
    problems, count = [], 0
    for folder, dirs, files in os.walk(out):
        dirs[:] = [d for d in dirs if d != '.git']
        for name in files:
            count += 1
            path = os.path.join(folder, name)
            rel = os.path.relpath(path, out).replace(os.sep, '/')
            ext = os.path.splitext(name)[1].lower()
            if name in FORBIDDEN_NAMES or rel.startswith(('hooks/', 'rules/')):
                problems.append(f'{rel}: not allowed in the directory edition')
            if name != 'LICENSE' and ext not in ALLOWED:
                problems.append(f'{rel}: file type not accepted from an unverified organization')
            if ext in IMAGES:
                continue
            raw = open(path, 'rb').read()
            if raw.startswith(b'#!') or b'\0' in raw:
                problems.append(f'{rel}: starts with #! or holds NUL bytes')
            if len(raw) > 256 * 1024:
                problems.append(f'{rel}: {len(raw)} bytes (over 256 KiB)')
            try:
                text = raw.decode('utf-8')
            except UnicodeDecodeError:
                problems.append(f'{rel}: not UTF-8')
                continue
            for phrase in FORBIDDEN_TEXT:
                if phrase in text:
                    problems.append(f'{rel}: says {phrase!r}, which is not true of this edition')
    if count > 512:
        problems.append(f'{count} files (over 512)')
    skills = os.listdir(os.path.join(out, 'skills'))
    if len(skills) != 55:
        problems.append(f'{len(skills)} skills instead of 55')
    return problems, count


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    target = os.path.abspath(sys.argv[1])
    build(target)
    problems, count = audit(target)
    if problems:
        raise SystemExit('The directory edition failed its audit:\n- ' + '\n- '.join(problems))
    print(f'Directory edition built in {target}: {count} files, audit clean')
