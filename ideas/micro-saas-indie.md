# Micro-SaaS & Indie Apps

> **Scope:** Small web or mobile products a solo developer can ship and charge for: developer SaaS, niche AI tools, local-business and vertical apps.

97 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Developer-facing SaaS](#developer-facing-saas)
- [AI-powered niche tools](#ai-powered-niche-tools)
- [Local business & trades](#local-business--trades)
- [Creator & content tools](#creator--content-tools)
- [Productivity apps](#productivity-apps)
- [B2B vertical niches](#b2b-vertical-niches)
- [Indie app mechanics](#indie-app-mechanics)

## Developer-facing SaaS

- **Status Page with Synthetic Checks**: Hosted status pages plus multi-region HTTP and browser checks, priced per monitor.
  - **Why:** Small SaaS teams need credible uptime communication without enterprise pricing.
  - **Stack:** Next.js, Playwright workers, Postgres · **Difficulty:** 🟡 Intermediate · **Prior art:** [openstatusHQ/openstatus](https://github.com/openstatusHQ/openstatus)

- **Cron Job Monitor**: Dead-man's-switch pings for scheduled jobs with alerting when a job doesn't report in.
  - **Why:** Silent cron failures are discovered days later.
  - **Stack:** Go, Postgres, email/Slack alerts · **Difficulty:** 🟢 Beginner · **Prior art:** [healthchecks/healthchecks](https://github.com/healthchecks/healthchecks)

- **Changelog and Roadmap Widget**: Embeddable changelog, public roadmap and feedback board for SaaS products.
  - **Why:** Users want to see progress; founders want feedback in one place.
  - **Stack:** Next.js, Postgres, embeddable script · **Difficulty:** 🟢 Beginner

- **Transactional Email Template Tester**: Preview email templates across clients, check links and spam score before sending.
  - **Why:** Broken emails damage trust and deliverability.
  - **Stack:** TypeScript, MJML, rendering workers · **Difficulty:** 🟡 Intermediate · **Prior art:** [resend/react-email](https://github.com/resend/react-email)

- **API Usage Metering and Billing**: Meter API calls per customer and sync usage-based invoices to Stripe.
  - **Why:** Usage-based pricing is popular but painful to implement.
  - **Stack:** Go, ClickHouse, Stripe API · **Difficulty:** 🔴 Advanced · **Prior art:** [getlago/lago](https://github.com/getlago/lago)

- **Feature Voting for Open Source**: Let users of an OSS project fund and vote on features, with transparent payouts.
  - **Why:** Links sustainability to what users actually want.
  - **Stack:** Next.js, Stripe Connect, GitHub API · **Difficulty:** 🟡 Intermediate

- **Screenshot and OG Image API**: Generate social cards and page screenshots from URLs or templates via API.
  - **Why:** Every content site needs social images.
  - **Stack:** Node, headless Chromium, CDN · **Difficulty:** 🟢 Beginner

- **Docs Search as a Service**: Crawl a docs site and provide typo-tolerant search with analytics on failed queries.
  - **Why:** Failed searches reveal missing documentation.
  - **Stack:** Meilisearch, crawler, embeddable UI · **Difficulty:** 🟡 Intermediate · **Prior art:** [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)

- **Link Preview Checker**: Paste a URL and see how it previews on each social network and chat app, with fixes for broken tags.
  - **Why:** Broken link previews quietly kill click-through on every share.
  - **Stack:** Next.js, server-side fetch, Open Graph parser · **Difficulty:** 🟢 Beginner

- **README Badge Generator Service**: Custom badges for any JSON endpoint or metric with caching and a visual designer.
  - **Why:** Maintainers want bespoke badges without hosting their own service.
  - **Stack:** Node.js, SVG templates, edge cache · **Difficulty:** 🟢 Beginner

- **Form Backend for Static Sites**: An endpoint static sites post forms to, with spam filtering, email notifications and CSV export.
  - **Why:** Static sites need forms without running a server.
  - **Stack:** Go or Node.js, Postgres, hCaptcha · **Difficulty:** 🟢 Beginner

- **PDF Invoice Generation API**: Send JSON and get back a branded, tax-compliant PDF invoice with templates per country.
  - **Why:** Developers rebuild invoice PDFs in every SaaS they ship.
  - **Stack:** Go, Typst, S3-compatible storage · **Difficulty:** 🟢 Beginner

- **Environment Config Diff Service**: Compares env vars across dev, staging and production and flags missing or mismatched keys without storing values.
  - **Why:** Missing config is a top cause of failed deploys.
  - **Stack:** Go, hashed key comparison, web UI · **Difficulty:** 🟡 Intermediate

- **Dependency Upgrade Digest**: A weekly email per repo listing which dependencies have updates, with breaking-change notes summarised.
  - **Why:** Bots open too many PRs; a digest is easier to plan around.
  - **Stack:** Node.js, GitHub API, changelog parsing · **Difficulty:** 🟡 Intermediate

## AI-powered niche tools

- **Contract Clause Checker for Freelancers**: Upload a client contract and get risky clauses flagged with plain-language explanations.
  - **Why:** Freelancers sign contracts without legal review.
  - **Stack:** Python, LLM, PDF parsing · **Difficulty:** 🟡 Intermediate

- **Grant Application Assistant**: Match nonprofits to grants and draft application sections from their existing documents.
  - **Why:** Small nonprofits lack grant writers.
  - **Stack:** Python, retrieval, LLM, grant databases · **Difficulty:** 🟡 Intermediate

- **Menu and Allergen Translator**: Restaurants upload a menu and get translated versions with allergen icons and QR codes.
  - **Why:** Tourist-area restaurants lose customers to language barriers.
  - **Stack:** Next.js, LLM translation, QR generation · **Difficulty:** 🟢 Beginner

- **Real Estate Listing Writer with Compliance**: Generate listing descriptions from photos and specs, flagging fair-housing compliance issues.
  - **Why:** Agents write dozens of listings and risk non-compliant wording.
  - **Stack:** Python, vision LLM, rules engine · **Difficulty:** 🟡 Intermediate

- **Customer Support Macro Builder**: Analyse past support tickets and suggest macros and help-centre articles for recurring issues.
  - **Why:** Support teams answer the same questions manually.
  - **Stack:** Python, clustering, helpdesk APIs · **Difficulty:** 🟡 Intermediate

- **Podcast to Newsletter**: Turn podcast episodes into newsletters, show notes and social posts with timestamps.
  - **Why:** Podcasters want more reach without extra writing time.
  - **Stack:** Python, whisper, LLM, email API · **Difficulty:** 🟢 Beginner

- **Code Interview Question Generator from Your Codebase**: Generate take-home and live interview tasks based on real (sanitised) problems from a company's code.
  - **Why:** Generic interview questions don't predict job performance.
  - **Stack:** Python, repo analysis, LLM · **Difficulty:** 🟡 Intermediate

- **Accessibility Fix Suggestions for Shopify Stores**: Scan a store theme for accessibility issues and propose exact Liquid template fixes.
  - **Why:** Store owners face accessibility complaints but can't code.
  - **Stack:** Node, axe-core, Shopify API · **Difficulty:** 🟡 Intermediate

- **Plant Care Diagnosis from Photos**: Snap a sick houseplant and get likely causes and a care plan with follow-up reminders.
  - **Why:** Plant owners guess and over-water; a paid diagnosis app has clear demand.
  - **Stack:** React Native, vision model API · **Difficulty:** 🟢 Beginner

- **Wedding Speech Coach**: Drafts and rehearses a speech with timing feedback and filler-word counts from a recording.
  - **Why:** Best men and bridesmaids panic about speeches once and pay happily.
  - **Stack:** Next.js, Whisper API, LLM · **Difficulty:** 🟢 Beginner

- **Pet Adoption Listing Writer**: Shelters paste notes and photos and get warm, accurate adoption listings in their house style.
  - **Why:** Shelter staff are overworked; better listings mean faster adoptions.
  - **Stack:** Next.js, vision model, templates · **Difficulty:** 🟢 Beginner

- **Tender Response Drafting for Small Firms**: Drafts responses to government tenders from a firm's past answers, flagging gaps against criteria.
  - **Why:** Small firms lose tenders because writing responses takes weeks.
  - **Stack:** Python, retrieval over past bids, web UI · **Difficulty:** 🟡 Intermediate

- **Meeting Minutes for Strata and HOA Committees**: Turns recordings into minutes in the legally required format with motions and votes.
  - **Why:** Volunteer committee secretaries dread minute-taking.
  - **Stack:** Whisper, LLM structured output, PDF export · **Difficulty:** 🟡 Intermediate

- **Product Photo Background Studio**: Removes backgrounds and places products on consistent, marketplace-compliant backdrops in bulk.
  - **Why:** Small online sellers need clean photos without a studio.
  - **Stack:** Python, background removal model, S3 · **Difficulty:** 🟢 Beginner

## Local business & trades

- **Quote Builder for Tradespeople**: Mobile-first quotes with photos, line items and e-signature acceptance.
  - **Why:** Tradespeople lose jobs by quoting slowly.
  - **Stack:** React Native or PWA, Postgres, PDF · **Difficulty:** 🟢 Beginner

- **Appointment Reminder via SMS and WhatsApp**: Reminders with confirm/reschedule replies for clinics and salons.
  - **Why:** No-shows cost small businesses real money.
  - **Stack:** Node, Twilio or WhatsApp API · **Difficulty:** 🟢 Beginner

- **Missed Call Text-Back**: When a business misses a call, automatically text the caller with a booking link.
  - **Why:** Missed calls are lost customers for busy trades.
  - **Stack:** Node, telephony API, webhook · **Difficulty:** 🟢 Beginner

- **Review Request Automation**: After a job is completed, send a review request and route unhappy customers to private feedback.
  - **Why:** Online reviews drive local business growth.
  - **Stack:** Next.js, SMS/email APIs · **Difficulty:** 🟢 Beginner

- **Inventory for Market Stalls**: Offline-first inventory and sales tracking for market vendors with end-of-day reports.
  - **Why:** Market sellers track stock on paper.
  - **Stack:** PWA, IndexedDB, sync backend · **Difficulty:** 🟢 Beginner

- **Roster and Shift Swap App**: Simple rostering with shift swaps, availability and award-rate calculations for small teams.
  - **Why:** Small hospitality teams roster in spreadsheets and group chats.
  - **Stack:** Next.js, Postgres, push notifications · **Difficulty:** 🟡 Intermediate

- **Job Photo Documentation**: Before/after photo logs tied to job addresses with timestamps and client-shareable reports.
  - **Why:** Proves work was done and prevents disputes.
  - **Stack:** Mobile app, object storage, PDF reports · **Difficulty:** 🟢 Beginner

- **Invoice Chaser**: Polite, escalating reminders for overdue invoices synced from accounting software, with pay-now links.
  - **Why:** Late payments strain small-business cash flow and chasing is awkward.
  - **Stack:** Node, Xero/QuickBooks APIs, Stripe payment links · **Difficulty:** 🟢 Beginner

- **AI Phone Receptionist for Trades**: Voice agent that answers calls, captures job details, books slots in the calendar and texts a summary.
  - **Why:** Trades miss calls while on the tools and lose jobs to competitors.
  - **Stack:** Python, telephony API, speech models, Calendar API · **Difficulty:** 🟡 Intermediate

- **Loyalty Stamp Card App**: Digital stamp cards for cafés with QR scanning and no customer app download.
  - **Why:** Paper loyalty cards get lost; big loyalty platforms are overkill.
  - **Stack:** PWA, Postgres, QR codes · **Difficulty:** 🟢 Beginner

- **Salon Waitlist and Walk-In Queue**: Walk-in customers join a queue by QR and get an SMS when it's nearly their turn.
  - **Why:** Barbers and nail salons lose walk-ins who won't wait in a crowded shop.
  - **Stack:** Next.js, Twilio, Postgres · **Difficulty:** 🟢 Beginner

- **Cleaning Business Job Checklists**: Room-by-room checklists with photo proof sent to the client after each clean.
  - **Why:** Cleaners get disputes they can't disprove.
  - **Stack:** React Native, image storage · **Difficulty:** 🟢 Beginner

- **Tutor Scheduling and Payments**: Lesson booking, recurring payments and progress notes for independent tutors.
  - **Why:** Tutors chase payments and juggle schedules by text message.
  - **Stack:** Rails or Laravel, Stripe · **Difficulty:** 🟢 Beginner

- **Mobile Mechanic Job Router**: Plans the day's route for mobile mechanics with parts lists per job.
  - **Why:** Mobile trades waste hours driving in inefficient orders.
  - **Stack:** Next.js, routing API, Postgres · **Difficulty:** 🟡 Intermediate

- **Gym Class Booking with Waitlists**: Class booking with capped spots, automatic waitlist promotion and no-show tracking.
  - **Why:** Boutique gyms pay heavily for booking software with features they don't use.
  - **Stack:** Django, Stripe, SMS · **Difficulty:** 🟡 Intermediate

## Creator & content tools

- **Link-in-Bio with Analytics You Own**: Self-hostable link page with privacy-friendly analytics and custom domains.
  - **Why:** Creators want ownership of audience data.
  - **Stack:** Next.js, SQLite, edge functions · **Difficulty:** 🟢 Beginner · **Prior art:** [dubinc/dub](https://github.com/dubinc/dub)

- **Newsletter Archive to Website**: Turn a newsletter archive into a searchable, SEO-friendly website automatically.
  - **Why:** Newsletter content is buried in inboxes.
  - **Stack:** Static site generator, email API import · **Difficulty:** 🟢 Beginner

- **YouTube Chapter Generator**: Generate accurate chapters and descriptions from video transcripts.
  - **Why:** Chapters improve watch time and search visibility.
  - **Stack:** Python, whisper, LLM · **Difficulty:** 🟢 Beginner

- **Social Post Scheduler for Developers**: Schedule posts across X, Bluesky, Mastodon and LinkedIn from Markdown files in a repo.
  - **Why:** Developers prefer git workflows to social media dashboards.
  - **Stack:** TypeScript, platform APIs, GitHub Action · **Difficulty:** 🟡 Intermediate · **Prior art:** [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app)

- **Course Platform with Code Sandboxes**: Sell courses where each lesson includes a runnable code sandbox.
  - **Why:** Coding courses need hands-on environments.
  - **Stack:** Next.js, WebContainers or containers, Stripe · **Difficulty:** 🔴 Advanced

- **Stock Photo Licence Tracker**: Track where licensed images are used and when licences expire.
  - **Why:** Businesses get invoices for unlicensed image use.
  - **Stack:** Next.js, image hashing, reminders · **Difficulty:** 🟡 Intermediate

- **Newsletter Sponsorship Marketplace**: Matches small newsletters with sponsors, handling booking, invoicing and performance reports.
  - **Why:** Small newsletters can't find sponsors and sponsors can't find niche audiences.
  - **Stack:** Next.js, Stripe Connect, Postgres · **Difficulty:** 🟡 Intermediate

- **Podcast Guest Booking Page**: A page where potential guests pitch, pick a slot and receive a prep kit automatically.
  - **Why:** Podcasters handle guest logistics by email threads.
  - **Stack:** SvelteKit, calendar APIs · **Difficulty:** 🟢 Beginner

- **Thumbnail A/B Tester for Videos**: Rotates video thumbnails and titles and reports which variant earns more clicks.
  - **Why:** Thumbnails decide views; creators test by guesswork.
  - **Stack:** Node.js, YouTube Data API · **Difficulty:** 🟡 Intermediate

- **Content Repurposing Calendar**: Plans how one long piece becomes clips, threads and posts across a month.
  - **Why:** Creators produce long content but struggle to distribute it.
  - **Stack:** Next.js, Postgres, calendar views · **Difficulty:** 🟢 Beginner

- **Digital Download Store for Musicians**: Sell stems, sample packs and presets with licence files and download limits.
  - **Why:** Musicians give large cuts to marketplaces for simple file sales.
  - **Stack:** Next.js, Stripe, S3 signed URLs · **Difficulty:** 🟢 Beginner

- **Watermarking Service for Photographers**: Batch-watermark galleries with visible or invisible marks and track where images appear.
  - **Why:** Photographers lose work to uncredited reposts.
  - **Stack:** Python, Pillow, reverse image search API · **Difficulty:** 🔴 Advanced

## Productivity apps

- **Meeting Cost Calculator for Calendars**: Show the estimated cost of meetings based on attendee roles and suggest ones to cut.
  - **Why:** Makes meeting overload visible to managers.
  - **Stack:** Browser extension, Calendar API · **Difficulty:** 🟢 Beginner

- **Focus Timer with Git Awareness**: Pomodoro timer that logs what you committed during each session.
  - **Why:** Developers want lightweight time tracking tied to output.
  - **Stack:** Tauri, git hooks, SQLite · **Difficulty:** 🟢 Beginner

- **Personal CRM for Networking**: Remember people, context and follow-ups with reminders, imported from email and calendar.
  - **Why:** Professional relationships fade without follow-up.
  - **Stack:** Next.js or mobile, Google APIs · **Difficulty:** 🟡 Intermediate · **Prior art:** [monicahq/monica](https://github.com/monicahq/monica)

- **Receipt Scanner for Tax Time**: Photograph receipts, extract data with OCR and export categorised reports for an accountant.
  - **Why:** Freelancers scramble to find receipts at tax time.
  - **Stack:** Mobile app, OCR, CSV export · **Difficulty:** 🟡 Intermediate

- **Family Chore and Allowance App**: Chores, rewards and allowance tracking with parent approval.
  - **Why:** Families want structure without spreadsheets.
  - **Stack:** React Native, Firebase or Supabase · **Difficulty:** 🟢 Beginner

- **Subscription Tracker with Cancellation Guides**: Detect recurring charges from bank exports and link to cancellation steps.
  - **Why:** People pay for forgotten subscriptions.
  - **Stack:** Web app, CSV parsing, rules · **Difficulty:** 🟢 Beginner

- **Travel Document Wallet**: Store passport, visa and booking details offline with expiry reminders.
  - **Why:** Travellers juggle documents across apps and emails.
  - **Stack:** Mobile app, encrypted local storage · **Difficulty:** 🟢 Beginner

- **Screen-Free Kids' Routine Chart**: A printable and tablet-friendly routine chart with picture cards and rewards.
  - **Why:** Parents want routines for young kids without handing them screens.
  - **Stack:** SvelteKit, print CSS · **Difficulty:** 🟢 Beginner

- **Gift Idea Tracker**: Save gift ideas for people throughout the year with price watching before birthdays.
  - **Why:** Everyone forgets the perfect idea they had months ago.
  - **Stack:** React Native, price scraping · **Difficulty:** 🟢 Beginner

- **Home Maintenance Scheduler**: Tracks filter changes, gutter cleaning and appliance services with reminders and history.
  - **Why:** Home owners forget maintenance until something breaks.
  - **Stack:** Flutter, SQLite, notifications · **Difficulty:** 🟢 Beginner

- **Freelancer Time-to-Invoice**: Tracks time per client and turns it into invoices with one click, including late-fee rules.
  - **Why:** Freelancers leak income by not billing all their hours.
  - **Stack:** Next.js, Stripe · **Difficulty:** 🟢 Beginner

- **Shared Grocery List with Aisle Sorting**: A shared list that sorts items by the aisle order of your usual store.
  - **Why:** Couples and families duplicate purchases and zig-zag through shops.
  - **Stack:** React Native, realtime sync · **Difficulty:** 🟢 Beginner

- **Document Expiry Tracker for Families**: Tracks passports, licences and insurance for the whole family with renewal reminders.
  - **Why:** Expired passports ruin trips every holiday season.
  - **Stack:** PWA, encrypted storage · **Difficulty:** 🟢 Beginner

## B2B vertical niches

- **Compliance Checklist for Small Clinics**: Track required certifications, audits and staff training deadlines.
  - **Why:** Small clinics risk fines from missed renewals.
  - **Stack:** Next.js, Postgres, email reminders · **Difficulty:** 🟢 Beginner

- **Property Maintenance Request Portal**: Tenants report issues with photos; landlords assign tradespeople and track status.
  - **Why:** Small landlords manage requests over text messages.
  - **Stack:** Next.js, Postgres, SMS · **Difficulty:** 🟡 Intermediate

- **Equipment Hire Booking**: Availability calendar, deposits and damage reports for equipment hire businesses.
  - **Why:** Hire businesses double-book with paper calendars.
  - **Stack:** Next.js, Stripe, calendar UI · **Difficulty:** 🟡 Intermediate

- **Event Check-In App**: QR tickets, offline check-in and live attendance counts for small events.
  - **Why:** Event software is priced for large conferences.
  - **Stack:** PWA, QR scanning, sync · **Difficulty:** 🟢 Beginner

- **Construction Daily Log**: Site diaries with weather, crew, deliveries and photos exported to PDF.
  - **Why:** Daily logs are legally important and often incomplete.
  - **Stack:** Mobile app, weather API, PDF · **Difficulty:** 🟡 Intermediate

- **School Club Management**: Membership, fees, attendance and parent communication for school clubs.
  - **Why:** Volunteer-run clubs manage everything by email.
  - **Stack:** Next.js, Stripe, email · **Difficulty:** 🟢 Beginner

- **Food Truck Locator and Pre-Order**: Live truck location, menu and pre-orders for pickup.
  - **Why:** Customers can't find trucks; trucks lose sales to queues.
  - **Stack:** React Native, maps, Stripe · **Difficulty:** 🟡 Intermediate

- **Farm Spray Record Keeping**: Log chemical applications with weather conditions for compliance audits.
  - **Why:** Farmers must keep spray records and still do it on paper.
  - **Stack:** React Native offline, weather API · **Difficulty:** 🟡 Intermediate

- **Dental Recall Reminders**: Automated patient recall reminders with online rebooking for small dental practices.
  - **Why:** Missed recalls are lost revenue for practices without big software.
  - **Stack:** Django, Twilio, calendar integration · **Difficulty:** 🟡 Intermediate

- **Vet Clinic Vaccine Reminder Cards**: Sends pet owners vaccine and check-up reminders with branded digital cards.
  - **Why:** Clinics lose repeat visits when owners forget.
  - **Stack:** Next.js, email and SMS · **Difficulty:** 🟢 Beginner

- **Security Guard Patrol Logger**: Guards scan NFC tags on patrol routes; managers see proof of patrols and incident reports.
  - **Why:** Small security firms rely on paper logs clients don't trust.
  - **Stack:** React Native NFC, Postgres · **Difficulty:** 🟡 Intermediate

- **Driving School Lesson Tracker**: Tracks learner progress against test criteria with instructor notes and bookings.
  - **Why:** Instructors track progress on paper cards.
  - **Stack:** Flutter, Postgres · **Difficulty:** 🟢 Beginner

- **Brewery Batch Tracker**: Records batches, gravity readings and tank usage for small craft breweries with tax reports.
  - **Why:** Craft brewers juggle spreadsheets for compliance and planning.
  - **Stack:** Django, Postgres, charts · **Difficulty:** 🟡 Intermediate

- **Wholesale Order Portal for Small Producers**: Lets retailers reorder from a small producer's catalogue with tiered pricing.
  - **Why:** Small producers take wholesale orders by phone and email.
  - **Stack:** Next.js, Stripe invoicing · **Difficulty:** 🔴 Advanced

- **Commercial Kitchen Temperature Logs**: Wireless probes and a checklist app that log fridge temperatures for food safety audits.
  - **Why:** Paper temperature logs are faked and fail inspections.
  - **Stack:** ESP32 probes, web app, alerts · **Difficulty:** 🔴 Advanced

## Indie app mechanics

- **Paywall and Pricing Experiments Kit**: Run pricing-page experiments with proper statistics and revenue attribution.
  - **Why:** Pricing is the highest-leverage lever for indie founders.
  - **Stack:** TypeScript, feature flags, Stripe webhooks · **Difficulty:** 🟡 Intermediate · **Prior art:** [growthbook/growthbook](https://github.com/growthbook/growthbook)

- **Waitlist with Referral Leaderboard**: Launch waitlist with referral tracking, positions and anti-fraud checks.
  - **Why:** Pre-launch audiences grow through referrals.
  - **Stack:** Next.js, Postgres, email · **Difficulty:** 🟢 Beginner

- **Churn Signal Alerts**: Watch product usage and payments for churn signals and alert founders to reach out.
  - **Why:** Saving customers is cheaper than finding new ones.
  - **Stack:** Python, Stripe API, product analytics events · **Difficulty:** 🟡 Intermediate

- **In-App Feedback Widget with Screenshots**: Embeddable feedback button that captures screenshots, console logs and browser details.
  - **Why:** Users report bugs without the details developers need.
  - **Stack:** TypeScript, html2canvas, backend API · **Difficulty:** 🟢 Beginner

- **Localisation Service for Indie Apps**: Machine translation with human review queues and over-the-air string updates for mobile apps.
  - **Why:** Localisation opens new markets but is operationally heavy.
  - **Stack:** Next.js, LLM translation, OTA SDK · **Difficulty:** 🟡 Intermediate · **Prior art:** [tolgee/tolgee-platform](https://github.com/tolgee/tolgee-platform)

- **Open Startup Metrics Page**: Public revenue, users and churn dashboard pulled from Stripe and analytics.
  - **Why:** Building in public attracts customers and trust.
  - **Stack:** Next.js, Stripe API, charts · **Difficulty:** 🟢 Beginner

- **Lifetime Deal Licence Server**: Issue, validate and revoke licence keys for desktop and self-hosted apps.
  - **Why:** Indie apps selling one-time licences need key management.
  - **Stack:** Go, Ed25519 signatures, Postgres · **Difficulty:** 🟡 Intermediate · **Prior art:** [keygen-sh/keygen-api](https://github.com/keygen-sh/keygen-api)

- **Trial Expiry Email Sequences**: A drop-in service for trial-ending emails with personalised usage stats.
  - **Why:** Most indie SaaS lose conversions at trial end with generic emails.
  - **Stack:** Node.js, email API, webhooks · **Difficulty:** 🟢 Beginner

- **Referral Credits Engine**: Gives both parties credits on referral with fraud checks and a hosted dashboard.
  - **Why:** Referral programmes are valuable but tedious to build safely.
  - **Stack:** TypeScript, Postgres, Stripe · **Difficulty:** 🟡 Intermediate

- **Pricing Page Localiser**: Shows prices in local currency with purchasing power parity discounts.
  - **Why:** International customers bounce when prices feel too high.
  - **Stack:** Edge functions, IP geolocation, Stripe · **Difficulty:** 🟡 Intermediate

- **Cancellation Flow with Save Offers**: A hosted cancel flow that asks why and offers pauses or discounts before churn.
  - **Why:** A good cancel flow saves a meaningful share of churn.
  - **Stack:** Next.js, Stripe Billing · **Difficulty:** 🔴 Advanced

- **App Store Review Responder**: Drafts replies to App Store and Play Store reviews and routes bug reports to your tracker.
  - **Why:** Indie developers ignore reviews because replying is tedious.
  - **Stack:** Node.js, store APIs, LLM · **Difficulty:** 🔴 Advanced

- **Usage-Based Upgrade Nudges**: Detects users hitting plan limits and triggers in-app upgrade prompts at the right moment.
  - **Why:** Upgrade prompts at the moment of need convert far better.
  - **Stack:** TypeScript SDK, event stream · **Difficulty:** 🔴 Advanced

- **Multi-Tenant Custom Domains Service**: Lets your customers attach their own domains with automatic TLS.
  - **Why:** Custom domains are a common paid feature that's painful to build.
  - **Stack:** Caddy on-demand TLS, Go API · **Difficulty:** 🔴 Advanced
