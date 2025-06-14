import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException
from PyPDF2 import PdfMerger
from PyPDF2.errors import PdfReadError

# Import configuration from separate file
from config import URLS, PDF_SETTINGS, BROWSER_SETTINGS

# Set up the Selenium WebDriver
def setup_driver():
    try:
        # Try using Edge with settings from config
        edge_options = EdgeOptions()
        if BROWSER_SETTINGS["headless"]:
            edge_options.add_argument("--headless")
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument(f"--window-size={BROWSER_SETTINGS['window_size'][0]},{BROWSER_SETTINGS['window_size'][1]}")
        edge_options.add_argument(f"--user-agent={BROWSER_SETTINGS['user_agent']}")
        edge_service = EdgeService(executable_path="edgedriver_mac64_m1/msedgedriver")
        driver = webdriver.Edge(service=edge_service, options=edge_options)
        driver.set_window_size(BROWSER_SETTINGS['window_size'][0], BROWSER_SETTINGS['window_size'][1])
        print("Using Microsoft Edge for automation.")
    except WebDriverException:
        # Fallback to Chrome with settings from config
        chrome_options = ChromeOptions()
        if BROWSER_SETTINGS["headless"]:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument(f"--window-size={BROWSER_SETTINGS['window_size'][0]},{BROWSER_SETTINGS['window_size'][1]}")
        chrome_options.add_argument(f"--user-agent={BROWSER_SETTINGS['user_agent']}")
        chrome_service = ChromeService(executable_path="/path/to/chromedriver")
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.set_window_size(BROWSER_SETTINGS['window_size'][0], BROWSER_SETTINGS['window_size'][1])
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")  # Set desktop resolution
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Desktop user agent
        chrome_service = ChromeService(executable_path="/path/to/chromedriver")  # Update with the path to your Chrome driver
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.set_window_size(1920, 1080)  # Ensure desktop viewport
        print("Using Chrome for automation.")
    return driver

# Print a page to PDF using Microsoft Edge's DevTools Protocol with custom settings
def print_page_to_pdf_with_edge(driver, url, name, folder_path, scale=0.5, page_ranges=None, landscape=True, pre_print_actions=None):
    try:
        driver.get(url)
        
        # Wait for page to load completely using multiple strategies
        wait = WebDriverWait(driver, 20)  # Maximum 20 seconds wait
        
        try:
            # Strategy 1: Wait for common Sensibull elements to load
            wait.until(EC.any_of(
                EC.presence_of_element_located((By.TAG_NAME, "table")),           # Tables (option chains, data)
                EC.presence_of_element_located((By.CLASS_NAME, "chart")),         # Charts
                EC.presence_of_element_located((By.CLASS_NAME, "data-table")),    # Data tables
                EC.presence_of_element_located((By.TAG_NAME, "canvas")),          # Chart canvases
                EC.presence_of_element_located((By.CLASS_NAME, "content"))        # General content
            ))
        except:
            # Strategy 2: Fallback - wait for document ready state
            wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        
        # Additional wait for dynamic content to load (charts, AJAX data)
        time.sleep(2)  # Brief wait for dynamic content after DOM is ready
        print(f"Page loaded successfully: {name}")
        
        # Execute pre-print actions if specified
        if pre_print_actions:
            print(f"Executing {len(pre_print_actions)} pre-print actions for {name}")
            for i, action in enumerate(pre_print_actions, 1):
                try:
                    # Determine selector type (CSS by default, XPath if specified)
                    selector_type = action.get("selector_type", "css")
                    selector = action["selector"]
                    
                    if action["action"] == "click":
                        print(f"  Action {i}: Clicking element '{selector}' using {selector_type}")
                        if selector_type == "xpath":
                            element = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                        else:
                            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                        element.click()
                        time.sleep(action.get("wait_after", 1))
                    elif action["action"] == "click_all":
                        print(f"  Action {i}: Clicking ALL elements matching '{selector}' using {selector_type}")
                        if selector_type == "xpath":
                            elements = driver.find_elements(By.XPATH, selector)
                        else:
                            elements = driver.find_elements(By.CSS_SELECTOR, selector)
                        
                        if elements:
                            print(f"    Found {len(elements)} matching elements")
                            for j, element in enumerate(elements, 1):
                                try:
                                    # Wait for element to be clickable and click it
                                    WebDriverWait(driver, 10).until(lambda d: element.is_enabled() and element.is_displayed())
                                    element.click()
                                    print(f"    Clicked element {j}/{len(elements)}")
                                    time.sleep(action.get("wait_between", 0.5))  # Small delay between clicks
                                except Exception as click_error:
                                    print(f"    Warning: Failed to click element {j}/{len(elements)} - {click_error}")
                        else:
                            print(f"    No elements found matching '{selector}'")
                        time.sleep(action.get("wait_after", 1))
                    elif action["action"] == "wait":
                        print(f"  Action {i}: Waiting {action['duration']} seconds")
                        time.sleep(action["duration"])
                    elif action["action"] == "scroll":
                        print(f"  Action {i}: Scrolling to element '{selector}' using {selector_type}")
                        if selector_type == "xpath":
                            element = driver.find_element(By.XPATH, selector)
                        else:
                            element = driver.find_element(By.CSS_SELECTOR, selector)
                        driver.execute_script("arguments[0].scrollIntoView();", element)
                        time.sleep(action.get("wait_after", 1))
                except Exception as e:
                    print(f"  Warning: Action {i} failed - {e}")
                    continue
        
        # Prepare PDF settings with custom scale, page ranges, and orientation from config
        pdf_settings = {
            "printBackground": True,
            "landscape": landscape,  # Use individual landscape setting
            "scale": scale,
            "format": PDF_SETTINGS["format"],
            "marginTop": PDF_SETTINGS["margins"]["top"],
            "marginBottom": PDF_SETTINGS["margins"]["bottom"],
            "marginLeft": PDF_SETTINGS["margins"]["left"],
            "marginRight": PDF_SETTINGS["margins"]["right"],
            "displayHeaderFooter": False
        }
        
        # Add page ranges if specified
        if page_ranges:
            pdf_settings["pageRanges"] = ",".join(page_ranges)
        
        # Use DevTools Protocol to print the page to PDF with custom settings
        pdf_data = driver.execute_cdp_cmd("Page.printToPDF", pdf_settings)

        # Save the PDF data to a file (decode from base64)
        import base64
        pdf_path = os.path.join(folder_path, f"{name}.pdf")
        with open(pdf_path, "wb") as f:
            f.write(base64.b64decode(pdf_data['data']))
        print(f"Page saved as PDF: {pdf_path}")
        return pdf_path
    except Exception as e:
        print(f"Error generating PDF for {name} ({url}): {e}")
        return None

# Merge all PDFs into one
def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    for pdf in pdf_files:
        try:
            merger.append(pdf)
        except PdfReadError:
            print(f"Skipping invalid PDF: {pdf}")
    merger.write(output_path)
    merger.close()
    print(f"All valid PDFs merged into: {output_path}")

# Main function
def main():
    # Create a folder for today's date
    today = datetime.now().strftime("%Y-%m-%d")
    folder_path = os.path.join("pdfs", today)
    os.makedirs(folder_path, exist_ok=True)

    # Set up the driver
    driver = setup_driver()

    pdf_files = []
    try:
        # Iterate through the URLs and print pages to PDF with custom settings
        for page in URLS:
            orientation = "landscape" if page.get("landscape", True) else "portrait"
            print(f"Printing: {page['name']} (scale: {page['scale']}, pages: {page['page_ranges']}, orientation: {orientation})")
            # Use Edge's DevTools Protocol for PDF generation with custom settings
            pdf_path = print_page_to_pdf_with_edge(
                driver, 
                page["url"], 
                page["name"], 
                folder_path, 
                scale=page["scale"], 
                page_ranges=page["page_ranges"],
                landscape=page.get("landscape", True),  # Default to landscape if not specified
                pre_print_actions=page.get("pre_print_actions", None)  # Pass pre-print actions if specified
            )
            if pdf_path:  # Only add valid PDF paths
                pdf_files.append(pdf_path)
    finally:
        driver.quit()
        print("Automation complete.")

    # Merge all PDFs into one
    output_pdf = os.path.join(folder_path, "Sensibull_Report.pdf")
    merge_pdfs(pdf_files, output_pdf)

if __name__ == "__main__":
    main()
