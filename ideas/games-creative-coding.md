# Games & Creative Coding

> **Scope:** Games, game tooling, generative art, music and audio, interactive experiments, retro and creative tools.

100 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

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

- **Big-O Card Battler**: A card game where each card is an algorithm and fights are won by picking the right complexity for the input.
  - **Why:** Makes complexity analysis stick through play.
  - **Stack:** TypeScript, Phaser · **Difficulty:** 🟢 Beginner · **Prior art:** [phaserjs/phaser](https://github.com/phaserjs/phaser)

- **Bug Hunt Browser Game**: Spot the bug in short code snippets against the clock, with explanations after each round.
  - **Why:** Code review skills improve with deliberate, bite-sized practice.
  - **Stack:** Svelte, JSON snippet packs · **Difficulty:** 🟢 Beginner

- **Git Branching Tower Defence**: Defend main by placing merges, rebases and reverts as towers against incoming conflicts.
  - **Why:** A playful way to internalise git operations.
  - **Stack:** TypeScript, Phaser · **Difficulty:** 🟢 Beginner

- **Packet Delivery Puzzle**: Route packets through switches, routers and firewalls to learn how networks forward traffic.
  - **Why:** Networking concepts are abstract until you can see packets move.
  - **Stack:** Godot, GDScript · **Difficulty:** 🟡 Intermediate · **Prior art:** [godotengine/godot](https://github.com/godotengine/godot)

- **Kubernetes Scheduling Puzzle**: Place pods onto nodes under CPU, memory and affinity constraints before the cluster overflows.
  - **Why:** Teaches scheduling rules better than reading docs.
  - **Stack:** TypeScript, canvas · **Difficulty:** 🟡 Intermediate

- **Escape Room in the Browser DevTools**: A puzzle website whose clues are hidden in the console, network tab and source maps.
  - **Why:** Teaches developer tools while feeling like a heist.
  - **Stack:** HTML, JavaScript · **Difficulty:** 🟢 Beginner

- **Password Cracker Simulator**: Watch how long guessed passwords survive a simulated dictionary and brute-force attack.
  - **Why:** Makes password strength tangible for non-technical players.
  - **Stack:** JavaScript, zxcvbn · **Difficulty:** 🟢 Beginner · **Prior art:** [dropbox/zxcvbn](https://github.com/dropbox/zxcvbn)

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

- **Dialogue Tree Editor for the Web**: A node-based editor for branching dialogue that exports JSON for any engine.
  - **Why:** Small teams write dialogue in spreadsheets and lose track of branches.
  - **Stack:** React Flow, TypeScript · **Difficulty:** 🟢 Beginner

- **Game Feel Juice Library**: Drop-in screen shake, hit-stop, squash and stretch and particle bursts with sensible defaults.
  - **Why:** Juice turns a flat prototype into something fun, but beginners don't know the tricks.
  - **Stack:** Godot addon or Phaser plugin · **Difficulty:** 🟢 Beginner

- **Playtest Heatmap Recorder**: Records player positions, deaths and quits during playtests and renders heatmaps over the level.
  - **Why:** Designers guess where players struggle instead of seeing it.
  - **Stack:** Godot or Unity plugin, web viewer · **Difficulty:** 🟡 Intermediate

- **Input Remapping Kit**: A controller and keyboard remapping screen with conflict detection and saved profiles.
  - **Why:** Remapping is an accessibility must-have that most indie games skip.
  - **Stack:** Godot addon · **Difficulty:** 🟢 Beginner

- **Accessibility Options Pack for Games**: Drop-in subtitle styling, colour-blind filters, hold-to-toggle inputs and difficulty assists for indie games.
  - **Why:** Accessibility options widen the audience but rarely make the schedule.
  - **Stack:** Godot addon or Unity package · **Difficulty:** 🟡 Intermediate

- **Procedural Quest Generator**: Generates fetch, escort and mystery quests from a world's factions, places and items.
  - **Why:** Open-world games need content volume that small teams can't hand-write.
  - **Stack:** Python or C#, grammar-based generation · **Difficulty:** 🟡 Intermediate

- **Rollback Netcode Sandbox**: A minimal fighting game demonstrating rollback netcode with adjustable latency and packet loss.
  - **Why:** Rollback is the gold standard for online action games but hard to learn.
  - **Stack:** Rust or C++, GGRS · **Difficulty:** 🔴 Advanced · **Prior art:** [gschup/ggrs](https://github.com/gschup/ggrs)

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

- **Daily Generative Postcard**: Generates a new art postcard each day from the date as a seed and emails it to subscribers.
  - **Why:** A tiny, delightful project to learn seeded randomness and email.
  - **Stack:** p5.js, Node.js, email API · **Difficulty:** 🟢 Beginner · **Prior art:** [processing/p5.js](https://github.com/processing/p5.js)

- **Truchet Tile Playground**: Explore Truchet and Wang tile patterns with live controls and SVG export for printing.
  - **Why:** Simple rules make beautiful patterns, perfect for learning generative design.
  - **Stack:** JavaScript, SVG · **Difficulty:** 🟢 Beginner

- **L-System Garden**: Grow plants from L-system grammars with sliders for angle, depth and randomness.
  - **Why:** A classic generative technique with instantly rewarding results.
  - **Stack:** p5.js or Processing · **Difficulty:** 🟢 Beginner

- **Circle Packing Poster Maker**: Pack circles into shapes and text to make posters, with palette and density controls.
  - **Why:** Circle packing looks impressive and teaches spatial algorithms.
  - **Stack:** JavaScript, canvas, SVG export · **Difficulty:** 🟢 Beginner

- **Reaction-Diffusion on the GPU**: Real-time Gray-Scott reaction-diffusion with painting tools and parameter presets.
  - **Why:** Organic patterns plus a first real taste of GPU compute.
  - **Stack:** WebGL or WebGPU shaders · **Difficulty:** 🟡 Intermediate

- **Genetic Art Evolver**: Evolve images with a genetic algorithm where viewers vote on which children survive.
  - **Why:** Teaches evolutionary algorithms through a crowd-driven art piece.
  - **Stack:** TypeScript, canvas, small backend · **Difficulty:** 🟡 Intermediate

- **Strange Attractor Renderer**: Render millions of points from Clifford and de Jong attractors into high-resolution prints.
  - **Why:** Chaotic systems produce gallery-quality images from a few lines of maths.
  - **Stack:** Rust or C++, PNG output · **Difficulty:** 🟡 Intermediate

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

- **Chord Progression Explorer**: Pick a key and mood and hear common chord progressions with voicing and substitution tips.
  - **Why:** Songwriters get stuck on the same progressions.
  - **Stack:** JavaScript, Tone.js · **Difficulty:** 🟢 Beginner · **Prior art:** [Tonejs/Tone.js](https://github.com/Tonejs/Tone.js)

- **Metronome with Practice Plans**: A metronome that ramps tempo over a session and logs practice time per piece.
  - **Why:** Musicians improve with gradual tempo increases but track them on paper.
  - **Stack:** React Native or PWA, Web Audio API · **Difficulty:** 🟢 Beginner

- **Drum Machine in the Browser**: A 16-step drum sequencer with swing, sample kits and shareable pattern URLs.
  - **Why:** A classic first audio project with a satisfying result.
  - **Stack:** JavaScript, Web Audio API · **Difficulty:** 🟢 Beginner

- **Ear Training Game**: Identify intervals, chords and scales by ear with adaptive difficulty.
  - **Why:** Ear training apps are often paid and ad-heavy.
  - **Stack:** Svelte, Tone.js · **Difficulty:** 🟢 Beginner

- **Sheet Music Page Turner**: Turns pages of a PDF score with a foot pedal, head nod or audio following.
  - **Why:** Musicians need both hands and hate awkward page turns.
  - **Stack:** Web app, MediaPipe or Bluetooth pedal · **Difficulty:** 🟡 Intermediate

- **Audio-Reactive Visualiser Kit**: Visuals that react to live audio with beat detection and presets for VJ sets.
  - **Why:** Small venues and streamers want visuals without expensive software.
  - **Stack:** WebGL, Web Audio API · **Difficulty:** 🟡 Intermediate

- **Pitch-Accurate Tuner with Temperaments**: A chromatic tuner supporting historical temperaments and custom reference pitches.
  - **Why:** Early-music players and piano tuners need more than equal temperament.
  - **Stack:** JavaScript, autocorrelation pitch detection · **Difficulty:** 🟡 Intermediate

- **Real-Time Guitar Effects Pedal on a Microcontroller**: Low-latency distortion, delay and reverb running on a microcontroller with a simple UI.
  - **Why:** A deep dive into DSP with a tangible result.
  - **Stack:** Teensy or Daisy Seed, C++ DSP · **Difficulty:** 🔴 Advanced

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

- **Gravity Letters**: Type text and watch the letters fall, bounce and stack with physics.
  - **Why:** A fun first physics project with instant feedback.
  - **Stack:** JavaScript, Matter.js · **Difficulty:** 🟢 Beginner · **Prior art:** [liabru/matter-js](https://github.com/liabru/matter-js)

- **Boids Flocking Playground**: Tune separation, alignment and cohesion and add predators or obstacles live.
  - **Why:** Emergent behaviour from simple rules is a great teaching moment.
  - **Stack:** p5.js · **Difficulty:** 🟢 Beginner

- **Webcam Ink Painting**: Paint with your finger in the air using hand tracking, with ink that spreads realistically.
  - **Why:** Combines computer vision and simulation in one playful demo.
  - **Stack:** MediaPipe, WebGL · **Difficulty:** 🟡 Intermediate

- **Sand Falling Simulation**: A falling-sand toy with water, fire, plants and custom materials.
  - **Why:** Cellular simulations teach performance and emergent design.
  - **Stack:** JavaScript or Rust with WebAssembly · **Difficulty:** 🟡 Intermediate

- **Interactive Solar System Scale Model**: Scroll through the solar system at true scale with facts at each planet.
  - **Why:** Shows how empty space really is; a strong portfolio piece.
  - **Stack:** Three.js · **Difficulty:** 🟢 Beginner · **Prior art:** [mrdoob/three.js](https://github.com/mrdoob/three.js)

- **Ray-Marched Fractal Explorer**: Fly through 3D fractals like the Mandelbulb in real time with saved camera paths.
  - **Why:** Demonstrates signed distance fields and shader optimisation.
  - **Stack:** GLSL, WebGL2 · **Difficulty:** 🔴 Advanced

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

- **Retro Font and Palette Pack Builder**: Convert modern fonts and palettes into formats for retro platforms and fantasy consoles.
  - **Why:** Retro devs spend ages hand-converting assets.
  - **Stack:** Python, Pillow · **Difficulty:** 🟢 Beginner

- **Text Adventure in the Style of Zork**: A parser-based adventure with rooms, inventory and save files.
  - **Why:** Teaches parsing and state machines through a beloved genre.
  - **Stack:** Python or Inform 7 · **Difficulty:** 🟢 Beginner

- **Game Boy Homebrew Starter Game**: A complete small platformer for the Game Boy with a build script and emulator testing.
  - **Why:** Constraints teach more than modern engines do.
  - **Stack:** GB Studio or GBDK-2020 · **Difficulty:** 🟡 Intermediate · **Prior art:** [gbdk-2020/gbdk-2020](https://github.com/gbdk-2020/gbdk-2020)

- **6502 Assembly Playground**: Write 6502 code in the browser and step through it with registers and memory visible.
  - **Why:** A gentle first taste of assembly on a classic CPU.
  - **Stack:** TypeScript, 6502 emulator core · **Difficulty:** 🟡 Intermediate

- **Cycle-Accurate NES Emulator**: A NES emulator accurate enough to pass common test ROMs, with a debugger.
  - **Why:** One of the most respected emulator projects for a portfolio.
  - **Stack:** Rust or C++ · **Difficulty:** 🔴 Advanced

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

- **Emoji Charades**: Players guess films or phrases described only in emoji, in real time rooms.
  - **Why:** A light multiplayer game that's quick to build and fun to share.
  - **Stack:** Node.js, Socket.IO · **Difficulty:** 🟢 Beginner

- **Collaborative Story Chain**: Each player adds one sentence to a story but only sees the previous line, then it's revealed.
  - **Why:** A classic party game that works well online.
  - **Stack:** SvelteKit, WebSocket · **Difficulty:** 🟢 Beginner

- **Watch Party Quiz Overlay**: A live quiz overlay for streams and watch parties where viewers answer from their phones.
  - **Why:** Streamers want easy audience interaction.
  - **Stack:** Node.js, WebSocket, OBS browser source · **Difficulty:** 🟡 Intermediate

- **Hide and Seek on a Real Map**: A location game where seekers get periodic, fuzzed hints of hiders' positions.
  - **Why:** Gets people outside and teaches geolocation privacy trade-offs.
  - **Stack:** React Native, maps, WebSocket · **Difficulty:** 🔴 Advanced

- **Multiplayer Physics Sandbox with Server Authority**: Many players build and break structures in a shared physics world without desync.
  - **Why:** Teaches authoritative servers and client prediction.
  - **Stack:** Rust, Rapier, WebSocket · **Difficulty:** 🔴 Advanced · **Prior art:** [dimforge/rapier](https://github.com/dimforge/rapier)

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

- **Palette from Mood Board**: Drop in several images and get a harmonised palette with accessible text pairings.
  - **Why:** Designers start from mood boards, not single images.
  - **Stack:** JavaScript, k-means clustering · **Difficulty:** 🟢 Beginner

- **Pixel Font Designer**: Draw bitmap glyphs on a grid and export TTF, BDF and sprite sheets.
  - **Why:** Pixel artists and retro devs need custom fonts without complex font software.
  - **Stack:** TypeScript, opentype.js · **Difficulty:** 🟡 Intermediate

- **Vector Animation to Lottie Exporter**: Animate simple vector scenes on a timeline and export Lottie or animated SVG.
  - **Why:** Indie developers want lightweight animations without pro motion tools.
  - **Stack:** TypeScript, SVG, Lottie JSON · **Difficulty:** 🔴 Advanced
