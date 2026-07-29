import glob

files = glob.glob('modules/*.py')
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    new_content = content.replace('template="plotly_dark"', 'template="plotly_white"')
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        print('Updated:', f)
print('Done')
