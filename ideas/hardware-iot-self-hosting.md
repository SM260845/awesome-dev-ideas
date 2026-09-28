# Hardware, IoT & Self-hosting

> **Scope:** Microcontrollers, home automation, local AI hardware, self-hosted services, networking, radio, backups and homelabs.

66 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Home automation](#home-automation)
- [Local AI hardware](#local-ai-hardware)
- [Self-hosted services](#self-hosted-services)
- [Networking](#networking)
- [Maker electronics](#maker-electronics)
- [Edge, offline & radio](#edge-offline--radio)
- [Backups & storage](#backups--storage)
- [Home lab infrastructure](#home-lab-infrastructure)

## Home automation

- **Presence Detection Fusion**: Combine phone Wi-Fi, BLE and mmWave sensors into reliable room-level presence.
  - **Why:** Single-sensor presence is flaky and ruins automations.
  - **Stack:** ESPHome, Home Assistant, Bayesian sensors · **Difficulty:** 🟡 Intermediate · **Prior art:** [esphome/esphome](https://github.com/esphome/esphome)

- **Energy Monitor with Appliance Detection**: Clamp-meter energy monitoring that identifies appliances by load signature.
  - **Why:** Shows where power goes without per-plug meters.
  - **Stack:** ESP32, CT clamps, Python classifier · **Difficulty:** 🔴 Advanced

- **Local Voice Control Satellite**: Cheap room satellites for fully local wake word, speech recognition and intents.
  - **Why:** Replace cloud speakers without losing voice control.
  - **Stack:** ESP32-S3, Wyoming protocol, Home Assistant · **Difficulty:** 🟡 Intermediate · **Prior art:** [OHF-Voice/wyoming](https://github.com/OHF-Voice/wyoming)

- **Smart Irrigation with Weather Forecast**: Water the garden based on soil moisture and rain forecast.
  - **Why:** Saves water and plants.
  - **Stack:** ESP32, soil sensors, weather API · **Difficulty:** 🟢 Beginner

- **Automation Test Harness for Home Assistant**: Unit-test home automations with simulated sensor states and time travel.
  - **Why:** Automations break silently after updates.
  - **Stack:** Python, Home Assistant test utilities · **Difficulty:** 🟡 Intermediate · **Prior art:** [home-assistant/core](https://github.com/home-assistant/core)

- **Mailbox Notifier**: Low-power sensor that alerts when the mailbox is opened.
  - **Why:** Classic, useful first IoT project.
  - **Stack:** ESP32 deep sleep, reed switch, LoRa or Wi-Fi · **Difficulty:** 🟢 Beginner

- **Zigbee Network Health Map**: Visualise Zigbee mesh routes, link quality and weak devices.
  - **Why:** Zigbee reliability issues are hard to diagnose.
  - **Stack:** Zigbee2MQTT, D3 · **Difficulty:** 🟡 Intermediate · **Prior art:** [Koenkk/zigbee2mqtt](https://github.com/Koenkk/zigbee2mqtt)

- **Garage Door Controller with Position Sensing**: Retrofit controller that reports true door position and auto-closes at night.
  - **Why:** Knowing the door is actually closed matters more than sending a toggle.
  - **Stack:** ESP32, relay, reed or ToF sensor, ESPHome · **Difficulty:** 🟢 Beginner

- **Local Video Doorbell**: Doorbell with on-device person detection and recordings that never leave the house.
  - **Why:** Cloud doorbells charge subscriptions and share footage.
  - **Stack:** Raspberry Pi or ESP32-CAM, Frigate, Home Assistant · **Difficulty:** 🟡 Intermediate

- **Washing Machine Done Notifier**: A vibration or power sensor that notifies you when the washer or dryer finishes.
  - **Why:** Laundry sits wet for hours because nobody heard the beep.
  - **Stack:** ESP32, accelerometer or smart plug, Home Assistant · **Difficulty:** 🟢 Beginner · **Prior art:** [esphome/esphome](https://github.com/esphome/esphome)

- **Water Leak Sensor Network**: Cheap leak sensors under sinks and heaters that alert and optionally shut a valve.
  - **Why:** Small leaks cause expensive damage before anyone notices.
  - **Stack:** ESP32 or Zigbee sensors, motorised valve · **Difficulty:** 🟢 Beginner

- **Room Occupancy Lighting with mmWave**: Lights that stay on while someone is sitting still, using mmWave presence instead of PIR.
  - **Why:** PIR sensors turn lights off on people reading or working.
  - **Stack:** ESP32, LD2410 mmWave sensor, ESPHome · **Difficulty:** 🟡 Intermediate

## Local AI hardware

- **Sound Event Monitor**: Classify household sounds locally (smoke alarm, glass break, baby crying) and send alerts.
  - **Why:** Useful for hearing-impaired people and parents without cloud audio.
  - **Stack:** Raspberry Pi, YAMNet-style audio model, MQTT · **Difficulty:** 🟡 Intermediate

- **Local AI Box on a Mini PC**: Reproducible image for a mini PC running local LLM, speech and image models behind one web UI.
  - **Why:** Families and small offices want private AI without cloud subscriptions.
  - **Stack:** Ollama, Open WebUI, Docker, Ansible · **Difficulty:** 🟡 Intermediate · **Prior art:** [open-webui/open-webui](https://github.com/open-webui/open-webui)

- **AI Camera for Wildlife**: Camera that detects and labels animals locally and posts clips to a gallery.
  - **Why:** Wildlife watching and research without cloud costs.
  - **Stack:** Raspberry Pi 5, AI accelerator, Frigate-style pipeline · **Difficulty:** 🟡 Intermediate · **Prior art:** [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate)

- **E-Ink AI Illustrated Frame**: E-ink frame that shows locally generated illustrations of the weather, bird visitors or calendar.
  - **Why:** Ambient, low-power, delightful display of local AI.
  - **Stack:** ESP32 e-ink, local image model server · **Difficulty:** 🟡 Intermediate · **Prior art:** [arnegiacomo/fugleramme](https://github.com/arnegiacomo/fugleramme)

- **GPU Homelab Scheduler**: Queue and share one or two home GPUs between LLM serving, training and image jobs.
  - **Why:** Contention on a single GPU crashes jobs.
  - **Stack:** Python, Docker, NVIDIA toolkit · **Difficulty:** 🟡 Intermediate

- **Edge Keyword Spotter**: Train a custom wake word and run it on a microcontroller.
  - **Why:** Hands-on TinyML with instant feedback.
  - **Stack:** TensorFlow Lite Micro, ESP32 · **Difficulty:** 🔴 Advanced

- **Local LLM Power Meter**: Measures watts per generated token for local models using a smart plug and publishes comparable results.
  - **Why:** Buyers of local AI hardware want real energy costs, not TDP guesses.
  - **Stack:** Smart plug API, llama.cpp, Python · **Difficulty:** 🟡 Intermediate

## Self-hosted services

- **Homelab Dashboard with Health and Updates**: Dashboard showing service health, pending image updates and backup status.
  - **Why:** Homelabs sprawl and break silently.
  - **Stack:** Go or TypeScript, Docker API · **Difficulty:** 🟢 Beginner · **Prior art:** [gethomepage/homepage](https://github.com/gethomepage/homepage)

- **One-Command Self-Hosting Bundles**: Opinionated compose bundles (photos, docs, passwords) with backups and TLS configured.
  - **Why:** Setup complexity keeps people on cloud services.
  - **Stack:** Docker Compose, Caddy, restic · **Difficulty:** 🟢 Beginner · **Prior art:** [caddyserver/caddy](https://github.com/caddyserver/caddy)

- **Self-Hosted Bookmark Archiver with Full Text**: Save links with full-page archives, screenshots and full-text search.
  - **Why:** Link rot destroys bookmarks.
  - **Stack:** Go, SingleFile, SQLite FTS · **Difficulty:** 🟡 Intermediate · **Prior art:** [karakeep-app/karakeep](https://github.com/karakeep-app/karakeep)

- **Family Recipe Server**: Import recipes from URLs, scale them, plan meals and generate shopping lists.
  - **Why:** Recipe sites are ad-heavy and slow.
  - **Stack:** Python, recipe schema parsing · **Difficulty:** 🟢 Beginner · **Prior art:** [mealie-recipes/mealie](https://github.com/mealie-recipes/mealie)

- **Family Password Manager Rollout Kit**: Kit to roll out a self-hosted password manager to non-technical family, with printed recovery sheets and emergency access.
  - **Why:** The hard part of self-hosting passwords is onboarding people, not the server.
  - **Stack:** Vaultwarden, docs templates, backup scripts · **Difficulty:** 🟢 Beginner · **Prior art:** [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)

- **Family-Friendly Status Page**: A plain-language status page ("Is the photo server up?") driven by your existing monitors.
  - **Why:** Saves answering the same questions when a home service is down.
  - **Stack:** Uptime Kuma API, static page · **Difficulty:** 🟢 Beginner · **Prior art:** [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma)

- **Private Photo Frame from Library**: Digital photo frame that pulls random memories from a self-hosted photo library.
  - **Why:** Enjoy photos without a cloud frame subscription.
  - **Stack:** Raspberry Pi, Immich API, kiosk browser · **Difficulty:** 🟢 Beginner · **Prior art:** [immich-app/immich](https://github.com/immich-app/immich)

- **Kids' Media Server with Allow-Lists**: A self-hosted media server where children only see approved shows, with daily viewing limits.
  - **Why:** Streaming apps' kids' modes still surface unwanted content.
  - **Stack:** Jellyfin, Docker, parental controls · **Difficulty:** 🟢 Beginner · **Prior art:** [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)

- **Self-Hosted Music Streaming Setup Guide**: A tested Compose stack for streaming your music library to phones with offline sync.
  - **Why:** Streaming services remove albums; owners want their own library everywhere.
  - **Stack:** Navidrome, Docker Compose, reverse proxy · **Difficulty:** 🟢 Beginner · **Prior art:** [navidrome/navidrome](https://github.com/navidrome/navidrome)

- **Home Inventory with Warranty Tracking**: Catalogue belongings with photos, receipts and warranty dates, with label printing and insurance export.
  - **Why:** After a burglary or flood, nobody can list what they owned.
  - **Stack:** Self-hosted web app, Docker, label printer · **Difficulty:** 🟡 Intermediate

## Networking

- **Mesh VPN for Family Tech Support**: Preconfigured mesh VPN so you can securely help family devices remotely.
  - **Why:** Remote help without exposing ports.
  - **Stack:** Headscale or Tailscale, RustDesk · **Difficulty:** 🟢 Beginner · **Prior art:** [juanfont/headscale](https://github.com/juanfont/headscale)

- **Kids' Device Schedules on DNS Filtering**: Per-device bedtimes and a simple parent app on top of a self-hosted DNS filter's API.
  - **Why:** Parents want schedules, not blocklist management.
  - **Stack:** AdGuard Home API, PWA · **Difficulty:** 🟢 Beginner · **Prior art:** [AdguardTeam/AdGuardHome](https://github.com/AdguardTeam/AdGuardHome)

- **Home Network Inventory**: Discover devices on your LAN, identify vendors and alert on new unknown devices.
  - **Why:** Unknown devices are a security risk.
  - **Stack:** Go, ARP scans, MAC vendor DB · **Difficulty:** 🟢 Beginner

- **Wi-Fi Heatmap Tool**: Walk around with a laptop and produce a signal strength map of your home.
  - **Why:** Find dead zones before buying mesh nodes.
  - **Stack:** Python, floor plan overlay · **Difficulty:** 🟢 Beginner

- **Bandwidth Monitor per Device**: Track bandwidth usage per device via router or SNMP data.
  - **Why:** Find what's saturating your connection.
  - **Stack:** Go, SNMP or router API, Grafana · **Difficulty:** 🟡 Intermediate

- **Internal Domains with Valid TLS**: Generate split DNS and DNS-challenge certificates so homelab services get real HTTPS names.
  - **Why:** Browser warnings and IP:port bookmarks make self-hosted services painful.
  - **Stack:** Traefik or Caddy, DNS provider API · **Difficulty:** 🟡 Intermediate · **Prior art:** [traefik/traefik](https://github.com/traefik/traefik)

- **Guest Wi-Fi QR Code Display**: An e-ink display showing a rotating guest Wi-Fi password as a QR code.
  - **Why:** Guests ask for the Wi-Fi password every visit.
  - **Stack:** ESP32, e-paper, router API · **Difficulty:** 🟢 Beginner

- **IPv6 Readiness Checker for Home Networks**: Tests your home network's IPv6 setup, firewall and DNS and explains what to fix.
  - **Why:** IPv6 is enabled by ISPs but misconfigured at home.
  - **Stack:** Python, web UI · **Difficulty:** 🟡 Intermediate

## Maker electronics

- **Open Source Macro Pad**: Programmable macro pad with per-app layers and a config web UI.
  - **Why:** Popular maker project with daily utility.
  - **Stack:** RP2040, QMK or KMK firmware · **Difficulty:** 🟡 Intermediate · **Prior art:** [qmk/qmk_firmware](https://github.com/qmk/qmk_firmware)

- **3D Printer Farm Manager**: Queue prints across several printers with camera monitoring and failure detection.
  - **Why:** Print farms waste filament on failed prints.
  - **Stack:** OctoPrint or Klipper APIs, vision model · **Difficulty:** 🔴 Advanced · **Prior art:** [Klipper3d/klipper](https://github.com/Klipper3d/klipper)

- **LED Matrix Information Display**: LED matrix showing transit times, weather and notifications.
  - **Why:** Glanceable information at home or office.
  - **Stack:** ESP32, HUB75 panel, WLED or custom firmware · **Difficulty:** 🟡 Intermediate · **Prior art:** [wled/WLED](https://github.com/wled/WLED)

- **Bench Power Supply Logger**: Log voltage and current from a lab supply to a web dashboard.
  - **Why:** Useful for battery and circuit testing.
  - **Stack:** Microcontroller, INA219, web UI · **Difficulty:** 🟢 Beginner

- **Plant Monitor with Growth Time-Lapse**: Soil, light and temperature sensors plus a camera time-lapse per plant.
  - **Why:** Hobbyist favourite with visible results.
  - **Stack:** Raspberry Pi, sensors, FFmpeg · **Difficulty:** 🟢 Beginner

- **Open Hardware Environmental Sensor**: Indoor CO2, PM2.5 and VOC monitor with local dashboard.
  - **Why:** Indoor air quality affects health and focus.
  - **Stack:** ESP32, SCD4x, PMS5003, ESPHome · **Difficulty:** 🟢 Beginner

- **Smart Pet Feeder with Camera**: Scheduled feeder that logs portions and snaps a photo when the pet eats.
  - **Why:** Pet owners want confirmation, not just a schedule.
  - **Stack:** ESP32-CAM, servo, load cell · **Difficulty:** 🟢 Beginner

- **Car OBD-II Trip Logger**: Log trips, fuel use and fault codes from the car's OBD-II port to a self-hosted dashboard.
  - **Why:** Owners want their own driving data without an insurer's dongle.
  - **Stack:** ESP32 or Raspberry Pi, ELM327, Grafana · **Difficulty:** 🟡 Intermediate

- **Soldering Fume Extractor with Air Quality Readout**: A DIY fume extractor that speeds up based on measured VOC levels.
  - **Why:** Hobbyists breathe solder fumes without realising the levels.
  - **Stack:** Arduino, VOC sensor, PWM fan · **Difficulty:** 🟢 Beginner

- **Desk Occupancy Timer**: A desk sensor that tracks sitting time and nudges you to stand.
  - **Why:** Long sitting stretches are unhealthy and easy to lose track of.
  - **Stack:** ESP32, pressure or mmWave sensor · **Difficulty:** 🟢 Beginner

## Edge, offline & radio

- **LoRa Sensor Network for a Farm**: Long-range sensors for water tanks, gates and weather reporting to a base station.
  - **Why:** Rural properties lack Wi-Fi coverage.
  - **Stack:** LoRa, ESP32, The Things Stack or ChirpStack · **Difficulty:** 🟡 Intermediate · **Prior art:** [chirpstack/chirpstack](https://github.com/chirpstack/chirpstack)

- **Offline Maps and Navigation Server**: Serve vector map tiles for your region offline with search and routing.
  - **Why:** Useful for remote areas and privacy.
  - **Stack:** OpenStreetMap, tile server, OSRM · **Difficulty:** 🟡 Intermediate · **Prior art:** [Project-OSRM/osrm-backend](https://github.com/Project-OSRM/osrm-backend)

- **Solar-Powered Weather Station**: Weather station publishing to MQTT and public weather networks.
  - **Why:** Hyperlocal weather data.
  - **Stack:** ESP32, sensors, solar charging · **Difficulty:** 🟡 Intermediate

- **Aircraft and Ship Tracker**: Receive ADS-B and AIS signals with a cheap SDR and map them.
  - **Why:** Satisfying radio project with live data.
  - **Stack:** RTL-SDR, dump1090, web map · **Difficulty:** 🟢 Beginner

- **LoRa Mesh Internet Bridge**: Base station bridging LoRa mesh messages to the internet when available.
  - **Why:** Community resilience in emergencies.
  - **Stack:** Meshtastic, Raspberry Pi, MQTT · **Difficulty:** 🟡 Intermediate · **Prior art:** [meshtastic/firmware](https://github.com/meshtastic/firmware)

- **Weather Balloon Telemetry Tracker**: Receives LoRa telemetry from a high-altitude balloon and plots its flight live.
  - **Why:** A memorable STEM project with real radio engineering.
  - **Stack:** LoRa, GPS module, web map · **Difficulty:** 🔴 Advanced

## Backups & storage

- **3-2-1 Backup Orchestrator**: Configure local, NAS and off-site backups with verification and restore drills.
  - **Why:** Most home backups are never tested.
  - **Stack:** restic, rclone, cron, web UI · **Difficulty:** 🟡 Intermediate · **Prior art:** [restic/restic](https://github.com/restic/restic)

- **NAS Health Reporter**: Weekly report of disk SMART data, capacity trends and failing drives.
  - **Why:** Drives fail with warning signs that go unread.
  - **Stack:** Python, smartctl, email · **Difficulty:** 🟢 Beginner

- **Photo Library Migration Tool**: Move photos from cloud services to self-hosting with albums and metadata intact.
  - **Why:** Exports from cloud services lose structure.
  - **Stack:** Python, takeout parsing, Immich API · **Difficulty:** 🟡 Intermediate

- **Encrypted Off-Site Backup to a Friend**: Swap encrypted backups with a friend's server over a mesh VPN.
  - **Why:** Cheap off-site backups with trust.
  - **Stack:** restic, Tailscale, scheduled jobs · **Difficulty:** 🟢 Beginner

- **Document Scanner Station**: Button-press scanner station that OCRs and files documents into a DMS.
  - **Why:** Paperless home without a PC in the loop.
  - **Stack:** Raspberry Pi, SANE, paperless-ngx · **Difficulty:** 🟢 Beginner · **Prior art:** [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)

- **Long-Term Cold Archive Planner**: Plans, writes and catalogues long-term archives to optical discs or LTO tape with parity files and a searchable index.
  - **Why:** Spinning disks and cloud accounts are poor bets for 20-year archives.
  - **Stack:** Python, par2, SQLite catalogue · **Difficulty:** 🟡 Intermediate

## Home lab infrastructure

- **Homelab as Code**: Rebuild the whole homelab from a git repo with Ansible and Terraform.
  - **Why:** Disaster recovery for your hobby infrastructure.
  - **Stack:** Ansible, Terraform, Proxmox · **Difficulty:** 🟡 Intermediate · **Prior art:** [ansible/ansible](https://github.com/ansible/ansible)

- **Low-Power Kubernetes Cluster**: Small k3s cluster on mini PCs with GitOps and storage.
  - **Why:** Learn Kubernetes on real hardware cheaply.
  - **Stack:** k3s, Flux, Longhorn · **Difficulty:** 🔴 Advanced · **Prior art:** [k3s-io/k3s](https://github.com/k3s-io/k3s)

- **Power Outage Graceful Shutdown**: UPS monitoring that shuts down servers in order and restarts them after power returns.
  - **Why:** Prevents data corruption during outages.
  - **Stack:** NUT, scripts, Home Assistant · **Difficulty:** 🟢 Beginner

- **Self-Hosted Secrets Manager for Homelab**: Central secrets store for homelab services with rotation and audit.
  - **Why:** Secrets end up in plain compose files.
  - **Stack:** OpenBao or Infisical · **Difficulty:** 🟡 Intermediate · **Prior art:** [openbao/openbao](https://github.com/openbao/openbao)

- **Homelab Cost and Power Tracker**: Track electricity cost per server and service using smart plugs.
  - **Why:** Homelabs can quietly cost a lot to run.
  - **Stack:** Smart plugs, Home Assistant, Grafana · **Difficulty:** 🟢 Beginner

- **Container Update Advisor**: Show available image updates with changelog summaries before applying.
  - **Why:** Blind auto-updates break services.
  - **Stack:** Go, registry APIs, release notes · **Difficulty:** 🟡 Intermediate

- **Out-of-Band Management with PiKVM-Style Access**: Remote keyboard, video and power control for homelab machines when the OS is down.
  - **Why:** Fixing a frozen server should not require walking to it.
  - **Stack:** Raspberry Pi, HDMI capture, relays · **Difficulty:** 🔴 Advanced · **Prior art:** [pikvm/pikvm](https://github.com/pikvm/pikvm)
