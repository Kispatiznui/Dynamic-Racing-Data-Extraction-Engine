Dynamic Racing Data Extraction Engine

A modular Python-based automation engine for extracting structured data from modern JavaScript-heavy web applications using Selenium.

This project is designed to run on local machines or Windows Server VPS environments and focuses on robust browser automation, dynamic content extraction, and structured Excel export with hyperlink preservation.

---
Overview

Modern websites like RacingPost are built as dynamic web applications where data is rendered through JavaScript and cannot be reliably extracted using traditional scraping methods or copy/paste techniques.

This engine solves that by:

* Automating browser interaction
* Navigating dynamic UI states (tabs, scroll regions, rendered components)
* Extracting structured and semi-structured data from non-table layouts
* Exporting clean datasets into Excel with preserved hyperlinks

---
Features

* Automated login handling (session-based scraping)
* Multi-URL scraping support
* Dynamic UI navigation (Stats tab handling)
* Scroll-based content loading support
* Extraction from non-table structured DOM elements
* Excel export with hyperlink preservation
* VPS-ready execution (Windows Server 2022 compatible)
* Modular architecture for easy extension
* Logging system for debugging and monitoring

---
 Architecture

```text
USER INPUT
   ↓
CLI / Config Loader
   ↓
AUTH MODULE
   ↓
SELENIUM BROWSER ENGINE
   ↓
NAVIGATION LAYER (Stats Tab Handling)
   ↓
DYNAMIC SCRAPER (RPR Extraction Engine)
   ↓
DATA PROCESSING LAYER
   ↓
EXCEL EXPORTER
   ↓
LOGGING + VPS EXECUTION SUPPORT
```

---
Project Structure

```text
dynamic-racing-data-engine/

├── src/
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── retry.py
│   │
│   ├── browser/
│   │   ├── driver.py
│   │   ├── login.py
│   │   ├── navigator.py
│   │
│   ├── scraper/
│   │   ├── rpr_extractor.py
│   │   ├── dom_parser.py
│   │
│   ├── export/
│   │   ├── excel_exporter.py
│   │
│   ├── utils/
│   │   ├── helpers.py
│
├── data/
│   ├── output.xlsx
│
├── config/
│   ├── config.json
│
├── logs/
│   ├── app.log
│
├── main.py
├── requirements.txt
└── README.md
```

---
Tech Stack

* Python 3.10+
* Selenium WebDriver
* OpenPyXL
* Pandas (optional)
* Chrome / ChromeDriver

---
How It Works

1. User provides login credentials and target URLs
2. The system launches a Selenium-controlled browser session
3. It logs into RacingPost and maintains session state
4. For each URL:

   * Navigates to the page
   * Opens the Stats tab
   * Waits for dynamic content to render
   * Scrolls if required to load full dataset
5. Extracts RPR-related structured data
6. Converts extracted data into a clean dataset
7. Exports results into Excel with clickable hyperlinks

---
Running the Project

Install dependencies

```bash
pip install -r requirements.txt
```

---
Run the engine

```bash
python main.py
```

---
Input example

```text
Username: ********
Password: ********
URLs: https://example1.com, https://example2.com
```

---
Key Challenges Solved

* Dynamic JavaScript-rendered content extraction
* Non-table structured UI parsing
* Scroll-based lazy loading handling
* Session-based authenticated scraping
* Data normalization into structured Excel output

---
 Future Improvements

* Headless mode optimization for VPS performance
* Async multi-browser scraping
* Dockerized deployment
* API wrapper around scraping engine
* Database integration (PostgreSQL / SQLite)
* Web dashboard for job control and visualization

---
Disclaimer

This project is intended for educational and automation purposes. Users are responsible for ensuring compliance with the terms of service of any website they interact with.

---
 Author

Built by a systems-oriented developer focused on automation engineering, dynamic web extraction, AI-assisted data pipelines, and experimental computational systems.

