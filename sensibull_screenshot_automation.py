import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException

# List of URLs to capture
URLS = [
    {"name": "option_chain", "url": "https://web.sensibull.com/option-chain?view=ltp"},
    {"name": "option_chain_greeks", "url": "https://web.sensibull.com/option-chain?view=greeks"},  # Added new URL for option chain greeks
    {"name": "oi_change_vs_strike", "url": "https://web.sensibull.com/open-interest/oi-change-vs-strike?tradingsymbol=NIFTY"},
    {"name": "multistrike_oi", "url": "https://web.sensibull.com/open-interest/multistrike-oi?tradingsymbol=NIFTY"},
    {"name": "oi_vs_time", "url": "https://web.sensibull.com/open-interest/oi-vs-time?tradingsymbol=NIFTY"},
    {"name": "fut_oi_vs_time", "url": "https://web.sensibull.com/open-interest/fut-oi-vs-time?tradingsymbol=NIFTY"},
    {"name": "fii_dii_data", "url": "https://web.sensibull.com/fii-dii-data"},
    {"name": "fii_dii_fno", "url": "https://web.sensibull.com/fii-dii-data/fno"},
    {"name": "fii_dii_cash_market", "url": "https://web.sensibull.com/fii-dii-data/cash-market"},
    {"name": "fii_dii_history", "url": "https://web.sensibull.com/fii-dii-data/history"},
    {"name": "futures_options_data", "url": "https://web.sensibull.com/futures-options-data?tradingsymbol=NIFTY"},
    {
        "name": "daily_nifty_analysis",
        "url": f"https://web.sensibull.com/daily-nifty-analysis?lang=english&date={datetime.now().strftime('%Y-%m-%d')}"
    }
]

# Set up the Selenium WebDriver
def setup_driver():
    try:
        # Try using Edge
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        edge_options.add_argument("--disable-gpu")
        edge_service = EdgeService(executable_path="edgedriver_mac64_m1/msedgedriver")  # Updated with the correct path to Edge WebDriver
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        print("Using Microsoft Edge for automation.")
    except WebDriverException:
        # Fallback to Chrome
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_service = ChromeService(executable_path="/path/to/chromedriver")  # Update with the path to your Chrome driver
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        print("Using Chrome for automation.")
    return driver

# Take a screenshot of a specific page
def take_screenshot(driver, url, name, folder_path):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    screenshot_path = os.path.join(folder_path, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

# Main function
def main():
    # Create a folder for today's date
    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join("screenshots", today)
    os.makedirs(folder_path, exist_ok=True)

    # Set up the driver
    driver = setup_driver()

    try:
        # Iterate through the URLs and take screenshots
        for page in URLS:
            print(f"Capturing: {page['name']}")
            take_screenshot(driver, page["url"], page["name"], folder_path)
    finally:
        driver.quit()
        print("Automation complete.")

if __name__ == "__main__":
    main()
