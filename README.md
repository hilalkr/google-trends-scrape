In this project, we automated the process of scraping daily trending search topics from Google Trends. It uses Selenium for web scraping and OpenPyXL to store the extracted data in an Excel file. Each day's trending topics are saved in an .xlsx file named after the current date, along with relevant details such as the number of searches and description.

**Recuirements**

Python 3.x
Selenium WebDriver
ChromeDriver (compatible with your Chrome version)
OpenPyXL

**Necessary Libraries**
selenium.webdriver is used for automating web browser interaction from Python.
By is used to select elements with specific attributes.
openpyxl is for reading from and writing to Excel files (.xlsx format).
time is used for handling time-related tasks, like waiting for a page to load.

You can install Selenium and OpenPyXL using pip:

```pip install selenium openpyxl```

**Usage**

```python main.py```

The script will automatically open a Chrome window and navigate to the Google Trends page.  It will scrape the trending searches data and save it to an Excel file named with the current date in the same directory as the script.
