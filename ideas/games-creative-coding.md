# Games & Creative Coding

> **Scope:** Games, game tooling, generative art, music and audio, interactive experiments, retro and creative tools.

52 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Games with a dev twist](#games-with-a-dev-twist)
- [Game engines & tools](#game-engines--tools)
- [Generative art](#generative-art)
- [Music & audio](#music--audio)
- [Interactive & visual experiments](#interactive--visual-experiments)
- [Retro & emulation](#retro--emulation)
- [Social & multiplayer toys](#social--multiplayer-toys)
- [Creative tools](#creative-tools)

## Games with a dev twist

- **Git Conflict Puzzle Game**: Levels are real merge conflicts; resolve them correctly under a timer to progress.
  - **Why:** Teaches git in a memorable, low-stakes way.
  - **Stack:** TypeScript, web, git fixtures · **Difficulty:** 🟡 Intermediate

- **Terminal Roguelike with Shell Commands**: A roguelike where spells are Unix commands and pipes combine effects.
  - **Why:** Makes learning the shell playful.
  - **Stack:** Rust, ratatui, procedural generation · **Difficulty:** 🟡 Intermediate

- **Regex Crossword Generator**: Generate solvable regex crosswords of increasing difficulty.
  - **Why:** Fun regex practice with infinite content.
  - **Stack:** TypeScript, constraint solver · **Difficulty:** 🟡 Intermediate

- **SQL Murder Mystery Builder**: Toolkit to author SQL detective games on custom datasets.
  - **Why:** Engaging SQL teaching format that educators can extend.
  - **Stack:** SQLite, web UI · **Difficulty:** 🟢 Beginner · **Prior art:** [NUKnightLab/sql-mysteries](https://github.com/NUKnightLab/sql-mysteries)

- **Code Golf Arena**: Real-time code golf battles with sandboxed runners for several languages.
  - **Why:** Competitive, short-form coding fun.
  - **Stack:** Go, containers, WebSockets · **Difficulty:** 🔴 Advanced

- **Agent vs Agent Arena**: Bots written by players (or LLM agents) compete in a turn-based game with replays and ladder rankings.
  - **Why:** A playful benchmark for agent strategy and code.
  - **Stack:** Python or TypeScript, sandboxed bots, replay viewer · **Difficulty:** 🟡 Intermediate

- **Typing Game for Code**: Typing practice using real code snippets from popular repos with language-aware scoring.
  - **Why:** Coding typing speed differs from prose.
  - **Stack:** TypeScript, GitHub API · **Difficulty:** 🟢 Beginner

- **CPU Architecture Puzzle Game**: Build a working CPU from logic gates across levels, ending with running a small program.
  - **Why:** Deep learning disguised as a game.
  - **Stack:** TypeScript or Godot, logic simulation · **Difficulty:** 🔴 Advanced

## Game engines & tools

- **Level Editor for Tilemap Games**: Web-based level editor exporting to common formats with auto-tiling rules.
  - **Why:** Indie devs need quick level tooling.
  - **Stack:** TypeScript, Canvas, Tiled format · **Difficulty:** 🟡 Intermediate · **Prior art:** [mapeditor/tiled](https://github.com/mapeditor/tiled)

- **Procedural Dungeon Library**: Library with several generation algorithms (BSP, cellular automata, WFC) and a visual playground.
  - **Why:** Procedural content speeds up game development.
  - **Stack:** Rust or TypeScript, visual demo · **Difficulty:** 🟡 Intermediate · **Prior art:** [mxgmn/WaveFunctionCollapse](https://github.com/mxgmn/WaveFunctionCollapse)

- **Sprite Sheet Packer and Animator**: Pack sprites, define animations and preview them in the browser.
  - **Why:** Asset pipeline friction slows small game teams.
  - **Stack:** TypeScript, Canvas · **Difficulty:** 🟢 Beginner

- **Game Save Sync Service**: Sync save files for emulators and PC games across devices with version history.
  - **Why:** Players lose progress switching devices.
  - **Stack:** Go, file watchers, object storage · **Difficulty:** 🟡 Intermediate

- **Deterministic Lockstep Networking Demo**: Multiplayer RTS demo with lockstep networking, rollback and desync detection.
  - **Why:** Networking is the hardest part of multiplayer games to learn.
  - **Stack:** Rust or C#, UDP · **Difficulty:** 🔴 Advanced

- **Bevy Plugin for Dialogue**: Branching dialogue system with an editor and localisation support for Bevy.
  - **Why:** Narrative tools are thin in newer engines.
  - **Stack:** Rust, Bevy, Yarn-like format · **Difficulty:** 🟡 Intermediate · **Prior art:** [bevyengine/bevy](https://github.com/bevyengine/bevy)

- **Game Jam Starter Kits**: Minimal, well-structured templates for popular engines with menus, audio and save systems.
  - **Why:** Game jams waste the first hours on boilerplate.
  - **Stack:** Godot, raylib, Phaser templates · **Difficulty:** 🟢 Beginner · **Prior art:** [raysan5/raylib](https://github.com/raysan5/raylib)

## Generative art

- **Plotter Art Toolkit**: Generate SVG art optimised for pen plotters with path ordering and pen changes.
  - **Why:** Pen plotters are popular with creative coders but tooling is fragmented.
  - **Stack:** Python or JS, SVG optimisation · **Difficulty:** 🟡 Intermediate · **Prior art:** [abey79/vpype](https://github.com/abey79/vpype)

- **Generative Art Gallery with Seeds**: Publish generative pieces where each seed reproduces a unique output, with a gallery.
  - **Why:** Sharing reproducible generative work.
  - **Stack:** p5.js, static site · **Difficulty:** 🟢 Beginner · **Prior art:** [processing/p5.js](https://github.com/processing/p5.js)

- **Shader Playground with Presets**: Live GLSL editor with a preset library and export to video or wallpaper.
  - **Why:** Shaders are fun but setup-heavy.
  - **Stack:** WebGL2, TypeScript · **Difficulty:** 🟡 Intermediate

- **Flow Field Explorer**: Interactive tool to explore noise-based flow fields with export to print resolution.
  - **Why:** Classic generative art technique made tweakable.
  - **Stack:** Canvas, TypeScript · **Difficulty:** 🟢 Beginner

- **Photo to Mosaic Generator**: Build mosaics from your own photo library with colour matching.
  - **Why:** Personal, giftable output.
  - **Stack:** Python, Pillow, KD-tree · **Difficulty:** 🟢 Beginner

- **Generative Typography Tool**: Animate and distort type along paths and noise for posters and videos.
  - **Why:** Designers want code-driven type effects.
  - **Stack:** p5.js or Canvas, OpenType.js · **Difficulty:** 🟡 Intermediate · **Prior art:** [opentypejs/opentype.js](https://github.com/opentypejs/opentype.js)

## Music & audio

- **Live Coding Music Environment in the Browser**: Pattern-based live coding for music with samples and visual feedback.
  - **Why:** Live coding performances are growing; browser setups remove install friction.
  - **Stack:** TypeScript, Web Audio · **Difficulty:** 🔴 Advanced

- **Commit History Sonifier**: Turn a repo's commit history into music: authors as instruments, churn as intensity.
  - **Why:** A delightful demo for talks and READMEs.
  - **Stack:** Python or Tone.js, git log · **Difficulty:** 🟢 Beginner · **Prior art:** [Tonejs/Tone.js](https://github.com/Tonejs/Tone.js)

- **Guitar Tab to MIDI Converter**: Parse text tabs into MIDI with playback and tempo control.
  - **Why:** Tabs online are plain text with no playback.
  - **Stack:** Python, mido, parsing · **Difficulty:** 🟢 Beginner

- **Browser Synth with Modular Patching**: Visual modular synthesiser with patch cables and saveable patches.
  - **Why:** Learn synthesis hands-on without hardware.
  - **Stack:** Web Audio, TypeScript, Canvas · **Difficulty:** 🟡 Intermediate

- **Practice Tracker for Musicians**: Log practice with a metronome, recordings and progress charts.
  - **Why:** Musicians improve faster with structured practice.
  - **Stack:** PWA, Web Audio, IndexedDB · **Difficulty:** 🟢 Beginner

- **Stem Separation Desktop App**: Local app that splits songs into vocals, drums and bass for practice or remixing.
  - **Why:** Musicians want offline, private separation.
  - **Stack:** Python, Demucs, Tauri · **Difficulty:** 🟡 Intermediate

## Interactive & visual experiments

- **Webcam Pose Games**: Browser games controlled by body pose from a webcam.
  - **Why:** Active, accessible games without special hardware.
  - **Stack:** MediaPipe, TypeScript · **Difficulty:** 🟡 Intermediate · **Prior art:** [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe)

- **Physics Sandbox**: Browser sandbox with rigid bodies, joints and shareable scenes.
  - **Why:** Playful physics exploration and teaching.
  - **Stack:** Rapier or matter.js, TypeScript · **Difficulty:** 🟡 Intermediate · **Prior art:** [dimforge/rapier](https://github.com/dimforge/rapier)

- **Cellular Automata Lab**: Explore life-like and continuous automata with rule editors and GPU speed.
  - **Why:** Beautiful emergent behaviour; great learning tool.
  - **Stack:** WebGL, TypeScript · **Difficulty:** 🟡 Intermediate

- **Interactive Fiction Engine with State Graph**: Author branching stories with a visual graph and variable tracking.
  - **Why:** Writers want structure without code.
  - **Stack:** TypeScript, graph editor · **Difficulty:** 🟡 Intermediate · **Prior art:** [inkle/ink](https://github.com/inkle/ink)

- **3D Portfolio Room**: A walkable 3D room showcasing projects as interactive objects.
  - **Why:** Memorable portfolio format.
  - **Stack:** Three.js, glTF · **Difficulty:** 🟡 Intermediate · **Prior art:** [mrdoob/three.js](https://github.com/mrdoob/three.js)

- **Particle Text Effects Library**: Text that dissolves into particles and reforms, for landing pages.
  - **Why:** Popular eye-catching effect, reusable.
  - **Stack:** Canvas or WebGL · **Difficulty:** 🟢 Beginner

- **Pixel Art Editor with Animation**: Web pixel editor with layers, onion skinning and GIF export.
  - **Why:** Lightweight alternative to desktop tools.
  - **Stack:** TypeScript, Canvas · **Difficulty:** 🟡 Intermediate

## Retro & emulation

- **CHIP-8 Emulator with Debugger**: Emulator with step-through debugging, memory viewer and ROM loader.
  - **Why:** Classic first emulator, made more educational with a debugger.
  - **Stack:** Rust or TypeScript · **Difficulty:** 🟡 Intermediate

- **Retro Game Achievement Tracker**: Track achievements across emulators with a social feed.
  - **Why:** Retro gaming communities love achievements.
  - **Stack:** Web app, emulator hooks · **Difficulty:** 🟡 Intermediate · **Prior art:** [libretro/RetroArch](https://github.com/libretro/RetroArch)

- **Fantasy Console Game**: Build and publish a complete game on a fantasy console within its constraints.
  - **Why:** Constraints spark creativity and finish lines.
  - **Stack:** TIC-80, Lua · **Difficulty:** 🟢 Beginner · **Prior art:** [nesbox/TIC-80](https://github.com/nesbox/TIC-80)

- **NES Homebrew Toolchain Tutorial**: Step-by-step homebrew NES game with build tooling and CI.
  - **Why:** Low-level programming with visible results.
  - **Stack:** 6502 assembly, cc65 · **Difficulty:** 🔴 Advanced · **Prior art:** [cc65/cc65](https://github.com/cc65/cc65)

- **Demoscene Intro in 4 KB**: Build a size-coded audiovisual intro with shader tricks and compression.
  - **Why:** Extreme optimisation practice.
  - **Stack:** C, GLSL, crinkler-style packers · **Difficulty:** 🔴 Advanced

- **Speedrun Timer with Auto-Splits**: Cross-platform speedrun timer that auto-splits by reading game memory or screen cues.
  - **Why:** Speedrunners on Linux and macOS lack good timers.
  - **Stack:** Rust, egui, screen capture · **Difficulty:** 🟡 Intermediate · **Prior art:** [LiveSplit/LiveSplit](https://github.com/LiveSplit/LiveSplit)

## Social & multiplayer toys

- **Board Game Rules Engine**: Encode a board game's rules once and get online multiplayer, AI opponents and move validation.
  - **Why:** Hobbyists want to playtest their own designs online.
  - **Stack:** TypeScript, boardgame.io · **Difficulty:** 🟡 Intermediate · **Prior art:** [boardgameio/boardgame.io](https://github.com/boardgameio/boardgame.io)

- **Multiplayer Drawing Guessing Game**: Real-time drawing and guessing with rooms and custom word lists.
  - **Why:** Classic party game, great realtime practice.
  - **Stack:** WebSockets, Canvas, Node · **Difficulty:** 🟢 Beginner

- **Shared Pixel Canvas**: Collaborative pixel canvas with cooldowns, moderation and time-lapse.
  - **Why:** Viral community format.
  - **Stack:** Redis bitfields, WebSockets · **Difficulty:** 🟡 Intermediate

- **Trivia Bot for Communities**: Scheduled trivia in Discord with leaderboards and user-submitted questions.
  - **Why:** Keeps community servers active.
  - **Stack:** Discord bot, SQLite · **Difficulty:** 🟢 Beginner

- **Async Chess by Email or Chat**: Correspondence chess through email or chat with board images.
  - **Why:** Low-pressure games with friends.
  - **Stack:** Python, python-chess, email/chat API · **Difficulty:** 🟢 Beginner

- **Daily Word Game Engine**: Engine for Wordle-style daily puzzles with custom dictionaries and share cards.
  - **Why:** Easy to theme for niche communities.
  - **Stack:** TypeScript, static site · **Difficulty:** 🟢 Beginner

- **Geo Guessing Game with Open Imagery**: Guess locations from open street-level imagery.
  - **Why:** Fun and educational with open data.
  - **Stack:** Mapillary API, MapLibre · **Difficulty:** 🟡 Intermediate · **Prior art:** [maplibre/maplibre-gl-js](https://github.com/maplibre/maplibre-gl-js)

## Creative tools

- **Procedural Planet Generator**: Generate explorable planets with terrain, biomes and atmosphere in the browser.
  - **Why:** A showcase project for noise, LOD and shaders.
  - **Stack:** Three.js, GLSL, noise functions · **Difficulty:** 🔴 Advanced

- **AI Storyboard Generator**: Turn a script into a storyboard with scene breakdowns and shot suggestions.
  - **Why:** Filmmakers and animators plan faster.
  - **Stack:** Python, LLM, image generation · **Difficulty:** 🟡 Intermediate

- **Font Pairing Explorer**: Browse and preview font pairings with real content.
  - **Why:** Design decisions made visually.
  - **Stack:** TypeScript, Google Fonts API · **Difficulty:** 🟢 Beginner

- **Colour Palette Extractor**: Extract palettes from images with accessibility contrast checks.
  - **Why:** Designers need accessible palettes.
  - **Stack:** TypeScript, k-means, WCAG checks · **Difficulty:** 🟢 Beginner

- **Video Captions Styler**: Style and burn in animated captions for short-form videos.
  - **Why:** Captions boost engagement on social video.
  - **Stack:** FFmpeg, ASS subtitles, web UI · **Difficulty:** 🟡 Intermediate · **Prior art:** [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg)
