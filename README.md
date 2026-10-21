# Claude video skills

Vendored from the top picks in
[awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills).

| Skill(s) | Source | Commit | License |
|---|---|---|---|
| `explainroo` | [vincentsch/explainroo](https://github.com/vincentsch/explainroo) (`skills/explainroo` only) | e95232c | MIT |
| `onetake` | [feitangyuan/onetake](https://github.com/feitangyuan/onetake) (demo `.mp4`s and `assets/` left out) | 4157581 | PolyForm Noncommercial 1.0.0: **noncommercial use only** |
| `remotion-*` (12 skills) | [remotion-dev/skills](https://github.com/remotion-dev/skills) | 039e8a2 | see upstream |
| `explainer-default`, `explainer-engaging`, `explainer-high-energy`, `motion-broll`, `object-separation`, `sound-effects` | [Barty-Bart/motion-graphics](https://github.com/Barty-Bart/motion-graphics) | 3d83d98 | MIT (sound effects CC0, see `sound-effects/LICENSES.md`) |

## Requirements

- **explainroo**: Node.js 20.11+, ffmpeg, Chrome/Chromium. On first use the skill
  clones the tool to `~/.explainroo`, runs `npm install` and downloads about 400 MB of voice models.
- **onetake**: python3 with `playwright` (chromium), `numpy`, `scipy`, `Pillow`,
  `matplotlib`, and ffmpeg.
- **remotion-***: Node.js. Each video is a Remotion project (`npx create-video`).
- **motion-graphics skills**: Node.js, ffmpeg, python3 (`numpy`); renders use Playwright Chromium.
  `object-separation` also needs python 3.10+ (it installs torch and SAM 2 into a local venv).

To update, re-copy from upstream.
