# GitHub ML Scraper (GitHub Collections → CSV)

Collects repository **names + URLs** from GitHub’s **Machine Learning** Collection page and exports the results to a tidy CSV file.

- **Target page**: `https://github.com/collections/machine-learning`
- **Output**: `project_list.csv` (columns: `project_name`, `project_url`)

## What it does

- Opens the GitHub ML Collection page in Chrome (automated with Selenium)
- Waits for the project cards to load
- Extracts:
  - **Project name** (e.g., `tensorflow / tensorflow`)
  - **Project URL** (e.g., `https://github.com/tensorflow/tensorflow`)
- Saves everything to `project_list.csv`

## Why this exists

This is a small, practical project to build hands-on skills in:

- **QA automation fundamentals** (waiting, stability, selectors)
- **Web scraping workflows** (extract → normalize → export)
- **Data handling** with Pandas

## Tech stack

- **Python 3**
- **Selenium WebDriver** (Chrome)
- **Pandas**

## Project layout

- `github_scraper.py`: scraper script
- `project_list.csv`: generated output (example committed here)

## Quick start

### 1) Prerequisites

- **Python 3.9+** recommended
- **Google Chrome** installed (Selenium will launch Chrome)

> Note: The script uses Selenium Manager (built into Selenium) to automatically find/download a compatible ChromeDriver in most environments—no manual driver download is usually needed.

### 2) Install dependencies

```bash
pip install selenium pandas
```

### 3) Run the scraper

```bash
python github_scraper.py
```

When it finishes, you’ll see a printed table in the console and a message confirming export to `project_list.csv`.

## Output

`project_list.csv` looks like:

```text
project_name,project_url
apache / spark,https://github.com/apache/spark
scikit-learn / scikit-learn,https://github.com/scikit-learn/scikit-learn
tensorflow / tensorflow,https://github.com/tensorflow/tensorflow
...
```

## Notes on reliability

- The script uses an explicit wait (`WebDriverWait`) to reduce flakiness.
- If GitHub updates their HTML/CSS classes, the XPath selector may need updating.

## Troubleshooting

- **Chrome opens and closes immediately**: check the console for Selenium exceptions; GitHub may be rate-limiting or the selector may have changed.
- **TimeoutException**: try increasing the wait time (e.g., 20 seconds) or verify you can load the page in a normal browser session.
- **Corporate proxy / restricted network**: Selenium may fail to download/manage drivers; install drivers manually or run from an unrestricted network.

## Responsible scraping

- Be mindful of GitHub’s Terms of Service and rate limits.
- Avoid running the scraper in tight loops; add delays/backoff if you extend it.

## Ideas to extend

- Export additional fields (stars, description, topics, language)
- Follow each repo link and scrape repo metadata
- Add CLI flags (output file, headless mode, timeouts)
- Add tests for selectors and a CI check
