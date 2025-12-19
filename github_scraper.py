from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

# Configure Chrome browser options
driver_option = webdriver.ChromeOptions()
driver_option.add_argument("--incognito")
driver_option.add_argument("--start-maximized")

def create_webdriver():
    """
    Creates and returns a new Chrome WebDriver instance.
    Selenium Manager will automatically download the correct ChromeDriver.
    """
    return webdriver.Chrome(options=driver_option)

# Open browser
browser = create_webdriver()

# Navigate to page
browser.get("https://github.com/collections/machine-learning")

# Wait for projects to load (IMPORTANT for reliability)
WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//h1[@class='h3 lh-condensed']"))
)

projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

project_list = {}

for proj in projects:
    proj_name = proj.text
    proj_url = proj.find_element(By.XPATH, "a").get_attribute("href")
    project_list[proj_name] = proj_url

browser.quit()

# Convert to DataFrame
project_df = pd.DataFrame(
    project_list.items(),
    columns=["project_name", "project_url"]
)

print(project_df)

project_df.to_csv("project_list.csv", index=False)

print("\nData successfully exported to 'project_list.csv'!")
