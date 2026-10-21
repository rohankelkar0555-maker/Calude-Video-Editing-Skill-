# Journal promo (15 s)

Made with the `explainer-high-energy` skill. 1920×1080, 60 fps, 128 BPM, synthesised soundtrack.

- `journal-promo.mp4`: the finished video with sound
- `journal-promo.html`: open it in a browser to play or scrub the animation live
- `journal-promo.src.html`: the source to edit (fonts are placeholders); run `python3 build.py` to rebuild the `.html`
- `render.mjs`: re-render with `npm i playwright && node render.mjs journal-promo.html journal-promo.mp4 60 4 4`

Scenes: spark → JOURNAL title → WRITE. / REFLECT. / and breathe. → particle ring
("untangle the day") → a journal entry being written and saved → end card
("Write it down. Let it go."). The full beat sheet is at the top of the page's script.

All the text is placeholder copy. To change the name, tagline or card text, edit the
strings in `journal-promo.src.html`, then rebuild and re-render.
