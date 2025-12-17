# 🕷️ Python Web Scraping & Crawler Projects

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat\&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Web%20Automation-43B02A?style=flat\&logo=selenium)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat\&logo=pandas)

This repository contains various **web scraping and crawler projects** developed using **Python** and **Selenium**. The projects demonstrate different scraping techniques, ranging from basic static page scraping to advanced pagination handling and structured data extraction pipelines.

---

## 📂 Projects

### 1. 📚 Book Scraper (Pagination & Data Extraction)

A robust scraper that collects book information from [Books to Scrape](http://books.toscrape.com). The bot automatically navigates through the entire catalogue.

* **File:** `book_scraper.py`
* **Target:** All **1000 books** across **50 pages**
* **Key Features:**

  * **Automated Pagination:** Detects the "Next" button and iterates through pages using a `while` loop until no more pages are available.
  * **Defensive Programming:** Uses `try-except` blocks to gracefully handle exceptions such as `NoSuchElementException`.
  * **Star Rating Mapping:** Converts CSS-based star rating classes (e.g., `"Three"`) into numeric values using a mapping dictionary.
  * **Data Cleaning:** Removes currency symbols and unnecessary whitespace from scraped values.
  * **Excel Export:** Stores the collected data in a structured `books_data.xlsx` file using Pandas.

---

### 2. 📖 Wikipedia Search Scraper

A focused scraper that searches for specific keywords on Wikipedia and collects structured search results.

* **Location:** `wikipedia/` directory
* **Target:** Wikipedia search result pages
* **Key Features:**

  * **Browser Automation:** Automates form input, key presses, and page navigation.
  * **Explicit Waits:** Uses `WebDriverWait` with Expected Conditions (`EC`) to ensure elements are loaded before interaction, reducing synchronization issues.
  * **Data Extraction:** Collects article titles, links, and short summary texts.
  * **Excel Export:** Saves results as `wikipedia_results.xlsx`.

---

## 🛠️ Technologies & Tools

* **Python 3.9+**
* **Selenium WebDriver** – Browser automation and DOM interaction
* **Pandas** – Data structuring and DataFrame operations
* **OpenPyXL** – Writing Excel (`.xlsx`) files
* **WebDriver Manager** – Automatic browser driver management

---

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/klckubra/selenium-learning-bootcamp.git
   ```

2. **Install required dependencies:**

   ```bash
   pip install selenium pandas openpyxl webdriver-manager
   ```

---

## 🚀 Usage

### Running the Book Scraper

Run the script from the root directory:

```bash
python book_scraper.py
```

**Output:**
A file named `books_data.xlsx` will be created in the root directory.

---

### Running the Wikipedia Scraper

Navigate to the `wikipedia` directory and run the script:

```bash
cd wikipedia
python main.py
```

**Output:**
A file named `wikipedia_results.xlsx` will be created inside the `wikipedia` directory.

---

## ⚠️ Disclaimer

These projects are developed **for educational purposes only** to demonstrate web scraping techniques. Please respect websites’ terms of service and robots.txt rules when scraping data.
