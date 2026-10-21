# Claude video skills

Vendored from the top picks in
[awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills).

| Skill(s) | Source | Commit | License |
|---|---|---|---|
| `explainroo` | [vincentsch/explainroo](https://github.com/vincentsch/explainroo) (`skills/explainroo` only) | e95232c | MIT |
| `onetake` | [feitangyuan/onetake](https://github.com/feitangyuan/onetake) (demo `.mp4`s and `assets/` left out) | 4157581 | PolyForm Noncommercial 1.0.0: **noncommercial use only** |
| `remotion-*` (12 skills) | [remotion-dev/skills](https://github.com/remotion-dev/skills) | 039e8a2 | see upstream |

## Requirements

- **explainroo**: Node.js 20.11+, ffmpeg, Chrome/Chromium. On first use the skill
  clones the tool to `~/.explainroo`, runs `npm install` and downloads about 400 MB of voice models.
- **onetake**: python3 with `playwright` (chromium), `numpy`, `scipy`, `Pillow`,
  `matplotlib`, and ffmpeg.
- **remotion-***: Node.js. Each video is a Remotion project (`npx create-video`).

To update, re-copy from upstream.

## Plugin: voice-to-claude

[enesbasbug/voice-to-claude](https://github.com/enesbasbug/voice-to-claude) (MIT) adds
push-to-talk dictation: hold **Ctrl+Alt** (Ctrl+Option on macOS), speak, release to
transcribe locally with whisper.cpp. It is a Claude Code plugin, not a skill, so it is
not vendored. `.claude/settings.json` registers its marketplace and enables it, so Claude
Code offers to install it when you trust this folder.

After it installs, run once:

```
/voice-to-claude:setup
```

Setup builds whisper.cpp and downloads the base model (~142 MB), about 3-5 minutes.
It needs **macOS** (Apple Silicon recommended), Python 3.10-3.12, cmake and the Xcode
Command Line Tools (`brew install cmake && xcode-select --install`). Other commands:
`/voice-to-claude:start`, `stop`, `status`, `config`.

To install by hand instead:

```
/plugin marketplace add enesbasbug/voice-to-claude
/plugin install voice-to-claude@voice-to-claude-marketplace
```
