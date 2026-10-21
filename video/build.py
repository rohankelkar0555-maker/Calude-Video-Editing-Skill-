# Inline the woff2 fonts into the page: python3 build.py -> journal-promo.html
import base64, pathlib
s = pathlib.Path('journal-promo.src.html').read_text()
for f in pathlib.Path('fonts').glob('*.woff2'):
    s = s.replace('{{%s}}' % f.stem, base64.b64encode(f.read_bytes()).decode())
assert '{{' not in s
pathlib.Path('journal-promo.html').write_text(s)
