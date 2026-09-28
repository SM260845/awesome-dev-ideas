# Data & Analytics

> **Scope:** Pipelines, data quality, BI, product analytics, datasets, visualisation, notebooks and observability data.

82 ideas · Difficulty: 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · [Back to README](../README.md)

## Contents

- [Pipelines & ELT](#pipelines--elt)
- [Data quality & observability](#data-quality--observability)
- [BI & dashboards](#bi--dashboards)
- [Product & web analytics](#product--web-analytics)
- [Datasets & scraping for insight](#datasets--scraping-for-insight)
- [Visualisation](#visualisation)
- [Notebooks & analysis tools](#notebooks--analysis-tools)
- [Observability data](#observability-data)

## Pipelines & ELT

- **Niche dlt Source Pack**: Tested dlt sources for APIs nobody has packaged yet (local accounting, government or industry APIs).
  - **Why:** Loading data is easy once a good source exists; niche APIs lack one.
  - **Stack:** Python, dlt, DuckDB · **Difficulty:** 🟢 Beginner · **Prior art:** [dlt-hub/dlt](https://github.com/dlt-hub/dlt)

- **Change Data Capture to Lakehouse**: Stream Postgres changes into Iceberg tables with schema evolution handled.
  - **Why:** Analytics on fresh operational data without hammering the primary.
  - **Stack:** Debezium or logical replication, Iceberg · **Difficulty:** 🔴 Advanced · **Prior art:** [debezium/debezium](https://github.com/debezium/debezium)

- **Pipeline Lineage Visualiser**: Parse SQL and dbt models to build column-level lineage graphs.
  - **Why:** Knowing which dashboards break when a column changes.
  - **Stack:** Python, sqlglot, graph UI · **Difficulty:** 🟡 Intermediate · **Prior art:** [tobymao/sqlglot](https://github.com/tobymao/sqlglot)

- **Data Contract Checker**: Validate producer schemas against declared contracts in CI before consumers break.
  - **Why:** Upstream schema changes silently break downstream pipelines.
  - **Stack:** Python, YAML contracts, CI · **Difficulty:** 🟡 Intermediate

- **Spreadsheet Ingestion with Validation**: Upload messy spreadsheets, map columns, validate and load them with a correction UI.
  - **Why:** Business data still arrives as spreadsheets.
  - **Stack:** Python, pandas, web UI · **Difficulty:** 🟢 Beginner

- **Incremental Web Archive Pipeline**: Crawl selected sites on a schedule and store changes as dated snapshots for analysis.
  - **Why:** Researchers need historical versions of pages.
  - **Stack:** Python, Scrapy, WARC, DuckDB · **Difficulty:** 🟡 Intermediate · **Prior art:** [scrapy/scrapy](https://github.com/scrapy/scrapy)

- **Local Data Stack in a Box**: DuckDB, dbt and a BI tool preconfigured in one compose file with sample data.
  - **Why:** Learning and prototyping modern data stacks without cloud costs.
  - **Stack:** Docker, DuckDB, dbt, Superset · **Difficulty:** 🟢 Beginner · **Prior art:** [duckdb/duckdb](https://github.com/duckdb/duckdb)

- **Google Sheets to DuckDB Sync**: Pulls chosen Google Sheets into a local DuckDB file on a schedule with type inference and history.
  - **Why:** Small teams run their business in sheets but want SQL over it.
  - **Stack:** Python, Google Sheets API, DuckDB · **Difficulty:** 🟢 Beginner · **Prior art:** [duckdb/duckdb](https://github.com/duckdb/duckdb)

- **Email Attachment Ingestion Pipeline**: Watches an inbox for CSV and Excel reports from partners and loads them into a warehouse with validation.
  - **Why:** Many partners still send data only as email attachments.
  - **Stack:** Python, IMAP, dlt · **Difficulty:** 🟢 Beginner · **Prior art:** [dlt-hub/dlt](https://github.com/dlt-hub/dlt)

- **Parquet Converter with Schema Report**: Converts folders of CSV and JSON to partitioned Parquet and reports inferred types and nulls.
  - **Why:** Parquet makes analysis faster, but converting messy files is fiddly.
  - **Stack:** Python, PyArrow · **Difficulty:** 🟡 Intermediate

- **Backfill Planner**: Plans safe backfills for incremental models by date range, cost estimate and dependency order.
  - **Why:** Backfills are risky, expensive and done by hand.
  - **Stack:** Python, dbt manifest, warehouse APIs · **Difficulty:** 🔴 Advanced

## Data quality & observability

- **Freshness and Volume Monitor**: Alert when tables stop updating or row counts deviate from normal.
  - **Why:** Stale data leads to wrong decisions without anyone noticing.
  - **Stack:** Python, SQL, anomaly detection · **Difficulty:** 🟡 Intermediate

- **Schema Drift Alerts**: Detect new, removed or type-changed columns in source systems daily.
  - **Why:** Drift breaks pipelines at night.
  - **Stack:** Python, information_schema, alerts · **Difficulty:** 🟢 Beginner

- **Data Quality Tests from Samples**: Profile a dataset and propose quality tests (ranges, uniqueness, nulls) to review and adopt.
  - **Why:** Writing tests from scratch is why data teams skip them.
  - **Stack:** Python, profiling, Great Expectations · **Difficulty:** 🟡 Intermediate · **Prior art:** [fivetran/great_expectations](https://github.com/fivetran/great_expectations)

- **Metric Definition Registry**: Define business metrics once in YAML and compile them to SQL for every tool.
  - **Why:** "Revenue" means three different things in three dashboards.
  - **Stack:** Python, semantic layer, SQL generation · **Difficulty:** 🔴 Advanced · **Prior art:** [cube-js/cube](https://github.com/cube-js/cube)

- **PII Scanner for Warehouses**: Scan columns for personal data patterns and tag them for access policies.
  - **Why:** Personal data spreads into analytics tables unnoticed.
  - **Stack:** Python, regex and classifiers, warehouse APIs · **Difficulty:** 🟡 Intermediate

- **Duplicate Record Finder**: Finds fuzzy duplicate customers, products or addresses in a table and suggests merges.
  - **Why:** Duplicate records skew counts and annoy customers.
  - **Stack:** Python, splink or recordlinkage, DuckDB · **Difficulty:** 🟢 Beginner · **Prior art:** [moj-analytical-services/splink](https://github.com/moj-analytical-services/splink)

- **Null and Outlier Profiler**: A one-command profile of any table: null rates, outliers, cardinality and value histograms.
  - **Why:** Analysts profile data by hand before every analysis.
  - **Stack:** Python, DuckDB, HTML report · **Difficulty:** 🟢 Beginner

- **Dashboard Usage Audit**: Shows which dashboards nobody opens so teams can archive them.
  - **Why:** BI tools fill up with abandoned dashboards that still cost compute.
  - **Stack:** Python, BI tool APIs · **Difficulty:** 🟡 Intermediate

- **Upstream Change Impact Report**: When a source table's schema changes, lists every downstream model, dashboard and owner affected.
  - **Why:** Schema changes break reports that nobody knew depended on them.
  - **Stack:** Python, dbt manifest, BI metadata · **Difficulty:** 🔴 Advanced

## BI & dashboards

- **Dashboard Screenshot Tests**: Render dashboards in CI and diff them against baselines to catch broken charts and empty panels.
  - **Why:** Dashboards break silently when queries or schemas change.
  - **Stack:** Playwright, image diff, CI · **Difficulty:** 🟡 Intermediate · **Prior art:** [evidence-dev/evidence](https://github.com/evidence-dev/evidence)

- **Metric Anomaly Explainer**: When a KPI moves, break it down by dimensions to find which segment drove the change.
  - **Why:** Analysts spend hours slicing data to answer "why did it drop?"
  - **Stack:** Python, DuckDB, contribution analysis · **Difficulty:** 🟡 Intermediate

- **Natural-Language Query with SQL Review**: Ask a question, see the generated SQL and its explanation, and approve before running.
  - **Why:** Text-to-SQL is useful but must be verifiable.
  - **Stack:** Python, LLM, sqlglot validation · **Difficulty:** 🟡 Intermediate

- **Embedded Analytics Starter**: Multi-tenant embedded charts for SaaS apps with row-level security.
  - **Why:** Customers want analytics inside the product.
  - **Stack:** TypeScript, Cube or Postgres RLS, charts · **Difficulty:** 🟡 Intermediate

- **Personal Analytics Dashboard**: Combine sleep, exercise, screen time and spending exports into one private dashboard.
  - **Why:** Quantified-self data lives in silos.
  - **Stack:** Python, DuckDB, Streamlit · **Difficulty:** 🟢 Beginner · **Prior art:** [streamlit/streamlit](https://github.com/streamlit/streamlit)

- **TV Wall Dashboard Rotator**: Rotate dashboards on office TVs with auth handling and failure fallbacks.
  - **Why:** Office screens often show expired login pages.
  - **Stack:** Electron or browser kiosk, config · **Difficulty:** 🟢 Beginner

- **KPI Email Digest**: Sends a weekly email with the five metrics that matter, each with trend and a plain-language note.
  - **Why:** Executives don't open dashboards but do read email.
  - **Stack:** Python, SQL, email templates · **Difficulty:** 🟢 Beginner

- **Goal Tracker Dashboard for Small Teams**: Set quarterly numeric goals and track progress automatically from SQL queries.
  - **Why:** Goal tracking lives in slides that are out of date.
  - **Stack:** Metabase or Evidence, SQL · **Difficulty:** 🟢 Beginner · **Prior art:** [evidence-dev/evidence](https://github.com/evidence-dev/evidence)

- **Dashboard as Code Starter**: Define charts and dashboards in version-controlled files with previews on PRs.
  - **Why:** Clicked-together dashboards can't be reviewed or reproduced.
  - **Stack:** Evidence or Observable Framework, GitHub Actions · **Difficulty:** 🟡 Intermediate

## Product & web analytics

- **Opt-In Usage Analytics for APIs and CLIs**: Privacy-respecting usage stats per endpoint or command, with opt-in and data minimisation built in.
  - **Why:** Tool makers want usage data without invasive telemetry.
  - **Stack:** Go, ClickHouse or DuckDB · **Difficulty:** 🟡 Intermediate · **Prior art:** [plausible/analytics](https://github.com/plausible/analytics)

- **Feature Adoption Tracker**: Track which features each account uses and flag unused paid features.
  - **Why:** Product teams need adoption data for roadmap and churn.
  - **Stack:** Event tracking, SQL, dashboard · **Difficulty:** 🟡 Intermediate

- **A/B Test Analysis Notebook**: Correct statistical analysis for experiments with sequential testing and guardrail metrics.
  - **Why:** Peeking at results and bad stats lead to false wins.
  - **Stack:** Python, statsmodels, marimo · **Difficulty:** 🟡 Intermediate

- **Session Replay Sampler**: Record a sample of sessions with privacy masking and link them to errors.
  - **Why:** Seeing what users did beats guessing from logs.
  - **Stack:** rrweb, object storage, privacy rules · **Difficulty:** 🟡 Intermediate · **Prior art:** [rrweb-io/rrweb](https://github.com/rrweb-io/rrweb)

- **Search Query Analytics**: Analyse site search logs for zero-result queries and rising topics.
  - **Why:** Failed searches reveal content gaps and demand.
  - **Stack:** Python, log parsing, dashboard · **Difficulty:** 🟢 Beginner

- **UTM and Referrer Cleaner**: Normalise messy campaign parameters and referrers into clean channel groupings.
  - **Why:** Marketing attribution is ruined by inconsistent tags.
  - **Stack:** SQL, dbt macros · **Difficulty:** 🟢 Beginner

- **Cookieless Pageview Counter**: A tiny self-hosted pageview counter with no cookies, no personal data and a public stats page.
  - **Why:** Personal sites want basic stats without consent banners.
  - **Stack:** Go, SQLite, 1 KB script · **Difficulty:** 🟢 Beginner

- **Onboarding Funnel Analyzer**: Builds a funnel from signup events and highlights the step with the biggest drop-off by segment.
  - **Why:** Founders know users drop off but not where.
  - **Stack:** SQL, Python, charts · **Difficulty:** 🟢 Beginner

- **Retention Cohort Generator**: Turns an event table into weekly retention cohorts with a clean heatmap.
  - **Why:** Cohort analysis is essential and error-prone to build by hand.
  - **Stack:** SQL, DuckDB, Plotly · **Difficulty:** 🟢 Beginner

- **Feature Usage Correlation with Churn**: Finds which features retained users use more than churned users, with confidence intervals.
  - **Why:** Product teams need evidence for what to double down on.
  - **Stack:** Python, pandas, statsmodels · **Difficulty:** 🟡 Intermediate

## Datasets & scraping for insight

- **GitHub Trend Dataset**: Daily snapshots of trending repos, stars and topics published as an open dataset.
  - **Why:** Researchers and builders study ecosystem trends.
  - **Stack:** Python, GitHub API, Parquet, GitHub Actions · **Difficulty:** 🟢 Beginner

- **Job Market Skills Tracker**: Scrape job postings and track demand for skills and tools over time.
  - **Why:** Developers and educators want to know what's in demand.
  - **Stack:** Python, Playwright, NLP, DuckDB · **Difficulty:** 🟡 Intermediate

- **Package Ecosystem Health Dataset**: Collect downloads, releases and maintainer counts for npm or PyPI packages over time.
  - **Why:** Supports dependency decisions and research.
  - **Stack:** Python, registry APIs, BigQuery or DuckDB · **Difficulty:** 🟡 Intermediate

- **Real Estate Price Index for Your City**: Build a local price index from listings and sales with suburb-level charts.
  - **Why:** Official indices are coarse and delayed.
  - **Stack:** Python, scraping, hedonic regression · **Difficulty:** 🟡 Intermediate

- **Hacker News Topic Trends**: Track topic frequency and sentiment on HN over years.
  - **Why:** Useful signal for trend research and writing.
  - **Stack:** Python, HN Algolia API, embeddings · **Difficulty:** 🟢 Beginner

- **Open Data Joiner**: Join public datasets by geography (postcode, census area) with a simple UI.
  - **Why:** Geographic joins are the hardest part of civic data work.
  - **Stack:** Python, GeoPandas, DuckDB spatial · **Difficulty:** 🟡 Intermediate · **Prior art:** [geopandas/geopandas](https://github.com/geopandas/geopandas)

- **Smart Meter Tariff Comparator**: Load interval data from your energy meter and simulate your bill on every available tariff.
  - **Why:** Households overpay because comparing time-of-use tariffs by hand is hard.
  - **Stack:** Python, pandas, tariff configs, Streamlit · **Difficulty:** 🟢 Beginner

- **Historical Weather Explorer**: Pull decades of weather for any location and chart trends, extremes and anomalies.
  - **Why:** Useful for gardening, event planning and climate curiosity.
  - **Stack:** Python, Open-Meteo API, DuckDB · **Difficulty:** 🟢 Beginner · **Prior art:** [open-meteo/open-meteo](https://github.com/open-meteo/open-meteo)

- **Fantasy Sports Model Pipeline**: Ingest player stats, build projections and backtest selection strategies.
  - **Why:** A fun, motivating way to practise the full modelling workflow.
  - **Stack:** Python, scikit-learn, DuckDB · **Difficulty:** 🟡 Intermediate

- **Grocery Price Tracker for Your Area**: Tracks prices of a basket of groceries across local supermarkets over time.
  - **Why:** Households want real inflation numbers for their own shopping.
  - **Stack:** Python, Playwright, SQLite, charts · **Difficulty:** 🟢 Beginner

- **Conference Talk Topic Trends**: Scrapes conference schedules to chart which tech topics rise and fall year over year.
  - **Why:** Shows real industry interest beyond hype on social media.
  - **Stack:** Python, scraping, NLP topic modelling · **Difficulty:** 🟡 Intermediate

- **Open Source Licence Trends Dataset**: Tracks licence choices in new repos over time by language and ecosystem.
  - **Why:** Useful for researchers and anyone choosing a licence.
  - **Stack:** Python, GitHub API, Parquet · **Difficulty:** 🟡 Intermediate

- **Public Holiday and School Term Dataset**: A clean, versioned dataset of holidays and school terms by region for forecasting.
  - **Why:** Demand forecasting needs calendar features that are hard to gather.
  - **Stack:** Python, CSV and Parquet releases · **Difficulty:** 🟢 Beginner

- **Satellite Image Change Detector**: Detects land changes like new construction or deforestation from free satellite imagery.
  - **Why:** Journalists and researchers need change evidence at scale.
  - **Stack:** Python, Sentinel-2 data, rasterio · **Difficulty:** 🔴 Advanced

## Visualisation

- **Chart Linter**: Flag misleading charts: truncated axes, dual axes, rainbow palettes and unlabeled units.
  - **Why:** Bad charts mislead decisions.
  - **Stack:** Python or JS, Vega-Lite spec analysis · **Difficulty:** 🟡 Intermediate · **Prior art:** [vega/vega-lite](https://github.com/vega/vega-lite)

- **Git History Visualiser**: Animate a repo's history as a city or timeline showing contributors and churn.
  - **Why:** Fun and insightful for retrospectives and talks.
  - **Stack:** TypeScript, WebGL, git log · **Difficulty:** 🟡 Intermediate · **Prior art:** [acaudwell/Gource](https://github.com/acaudwell/Gource)

- **Large Graph Explorer in the Browser**: Render and explore million-node graphs with GPU layout and filtering.
  - **Why:** Network analysis tools choke on large graphs.
  - **Stack:** TypeScript, WebGL, force layout · **Difficulty:** 🔴 Advanced · **Prior art:** [cosmosgl/graph](https://github.com/cosmosgl/graph)

- **Map Story Builder**: Create animated map stories from GeoJSON and a script.
  - **Why:** Journalists want map animations without GIS skills.
  - **Stack:** MapLibre, TypeScript, timeline UI · **Difficulty:** 🟡 Intermediate

- **Terminal Charts for Data**: Plot CSVs and query results directly in the terminal.
  - **Why:** Quick looks at data without leaving the shell.
  - **Stack:** Rust or Python, Unicode plotting · **Difficulty:** 🟢 Beginner

- **Diagram from Data Model**: Generate ER diagrams from a live database with change history.
  - **Why:** Schema docs go stale fast.
  - **Stack:** Python, SQLAlchemy reflection, Mermaid · **Difficulty:** 🟢 Beginner

- **Calendar Heatmap Generator**: Turns any dated CSV into a GitHub-style calendar heatmap as SVG or PNG.
  - **Why:** People love this visual for habits, sales or commits.
  - **Stack:** Python or JavaScript, SVG · **Difficulty:** 🟢 Beginner

- **Sankey Diagram from Transactions**: Visualises where money goes from income to categories as an interactive Sankey diagram.
  - **Why:** Budget flows are easiest to understand as flows.
  - **Stack:** JavaScript, D3 · **Difficulty:** 🟢 Beginner · **Prior art:** [d3/d3](https://github.com/d3/d3)

- **Uncertainty Visualisation Kit**: Chart components for confidence intervals, fan charts and hypothetical outcome plots.
  - **Why:** Charts that hide uncertainty mislead decision makers.
  - **Stack:** Vega-Lite or Observable Plot · **Difficulty:** 🟡 Intermediate

- **Animated Bar Chart Race Maker**: Upload a time series and export a bar chart race video.
  - **Why:** Popular for storytelling and social posts with minimal effort.
  - **Stack:** JavaScript, D3, video export · **Difficulty:** 🟢 Beginner

## Notebooks & analysis tools

- **Reactive Notebook Templates**: Template gallery of reactive notebooks for common analyses (cohorts, funnels, forecasts).
  - **Why:** Reusable analyses save hours.
  - **Stack:** marimo or Observable, Python · **Difficulty:** 🟢 Beginner · **Prior art:** [marimo-team/marimo](https://github.com/marimo-team/marimo)

- **Notebook to Pipeline Converter**: Convert an exploratory notebook into a parameterised, tested pipeline.
  - **Why:** Notebook work rarely reaches production.
  - **Stack:** Python, AST analysis, papermill · **Difficulty:** 🟡 Intermediate

- **SQL Notebook for Local Files**: Query CSV, Parquet and JSON files with SQL in a notebook UI.
  - **Why:** Analysts want SQL on files without loading a database.
  - **Stack:** DuckDB, web UI · **Difficulty:** 🟢 Beginner

- **Forecasting Toolkit for Small Business**: Simple sales and demand forecasts with seasonality from spreadsheet exports.
  - **Why:** Small businesses order stock by gut feel.
  - **Stack:** Python, statsforecast, Streamlit · **Difficulty:** 🟡 Intermediate · **Prior art:** [Nixtla/statsforecast](https://github.com/Nixtla/statsforecast)

- **Data Diff Tool**: Compare two tables across databases row by row and summarise differences.
  - **Why:** Validating migrations and pipelines needs row-level diffs.
  - **Stack:** Python, hashing, SQL · **Difficulty:** 🟡 Intermediate

- **Open-Ended Survey Analyser**: Cluster free-text survey answers into themes with representative quotes and counts.
  - **Why:** Free-text answers are the most valuable and least analysed part of surveys.
  - **Stack:** Python, embeddings, clustering, report · **Difficulty:** 🟡 Intermediate

- **Warehouse Query Cost Analyser**: Find the most expensive queries and tables in a cloud warehouse and suggest fixes.
  - **Why:** Warehouse bills grow from a few bad queries.
  - **Stack:** Python, query history views, dashboard · **Difficulty:** 🟡 Intermediate

- **Analytics Tracking Plan Validator**: Declare product events and properties in YAML and validate live events against it.
  - **Why:** Event data rots into inconsistent names and types.
  - **Stack:** TypeScript, JSON Schema, event stream · **Difficulty:** 🟡 Intermediate

- **Survey Weighting Tool**: Reweights survey responses to match population demographics with raking and shows estimates before and after.
  - **Why:** Unweighted surveys mislead decisions.
  - **Stack:** Python, pandas, iterative proportional fitting · **Difficulty:** 🟡 Intermediate

- **Notebook Reproducibility Checker**: Re-runs notebooks in a clean environment and reports cells that fail or produce different output.
  - **Why:** Notebooks rot and results can't be reproduced.
  - **Stack:** Python, nbclient, Docker · **Difficulty:** 🟡 Intermediate

- **Statistical Test Picker**: Asks a few questions about your data and recommends the right statistical test with code.
  - **Why:** Picking the wrong test is a common analysis mistake.
  - **Stack:** Web app, Python code templates · **Difficulty:** 🟢 Beginner

## Observability data

- **Logs to Metrics Converter**: Derive metrics from log patterns without changing application code.
  - **Why:** Legacy apps lack metrics but have logs.
  - **Stack:** Vector, regex, Prometheus · **Difficulty:** 🟡 Intermediate · **Prior art:** [vectordotdev/vector](https://github.com/vectordotdev/vector)

- **Cost Per Feature Attribution**: Attribute cloud costs to product features using tags and traces.
  - **Why:** Product decisions ignore infrastructure costs.
  - **Stack:** Python, billing exports, tracing data · **Difficulty:** 🔴 Advanced

- **Trace Sampling Advisor**: Recommend sampling rules that keep rare errors while cutting trace volume.
  - **Why:** Tracing everything is expensive.
  - **Stack:** Python, OTel data analysis · **Difficulty:** 🟡 Intermediate

- **Error Budget Report**: Weekly SLO and error budget report emailed to stakeholders.
  - **Why:** SLOs matter only when people see them.
  - **Stack:** Prometheus API, templating, email · **Difficulty:** 🟢 Beginner

- **Kubernetes Cost Dashboard**: Break down cluster costs by namespace, team and workload.
  - **Why:** Shared clusters hide who's spending what.
  - **Stack:** OpenCost, Grafana · **Difficulty:** 🟡 Intermediate · **Prior art:** [opencost/opencost](https://github.com/opencost/opencost)

- **Log Volume Budget by Service**: Shows which services produce the most log bytes and what that costs per month.
  - **Why:** Logging bills grow with no clear owner.
  - **Stack:** Python, log platform APIs · **Difficulty:** 🟡 Intermediate

- **Alert Fatigue Analyzer**: Measures alert frequency, acknowledgment time and actionability to find noisy alerts.
  - **Why:** Noisy alerts get ignored until a real one is missed.
  - **Stack:** Python, PagerDuty or Opsgenie API · **Difficulty:** 🔴 Advanced

- **High-Cardinality Metric Finder**: Finds metrics whose label cardinality is exploding and estimates the storage cost.
  - **Why:** Cardinality explosions crash metrics backends and budgets.
  - **Stack:** Go, Prometheus TSDB stats · **Difficulty:** 🔴 Advanced
