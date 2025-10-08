from selenium import webdriver  # Main library for browser automation
from selenium.webdriver.common.by import By  # Used to specify how to locate elements (XPATH, ID, CLASS, etc.)
from selenium.webdriver.support.ui import WebDriverWait  # Allows waiting for elements to load before interacting
from selenium.webdriver.support import expected_conditions as EC  # Conditions to check if page elements are ready
from selenium.common.exceptions import TimeoutException  # Handle cases when page takes too long to load
from selenium.webdriver.chrome.service import Service  # Required for Selenium 4 to specify ChromeDriver location
import pandas as pd  # Library for data manipulation and creating tables/DataFrames

# Configure Chrome browser options
driver_option = webdriver.ChromeOptions()
driver_option.add_argument("--incognito")  # Opens browser in incognito/private mode
chromedriver_path = r"C:\webdrivers\chromedriver.exe"  # Path to ChromeDriver executable (r = raw string to handle backslashes)


def create_webdriver():
    """
    Creates and returns a new Chrome WebDriver instance.
    This function makes it easy to open multiple browser windows if needed.
    """
    service = Service(executable_path=chromedriver_path)  # Tell Selenium where ChromeDriver is located
    return webdriver.Chrome(service=service, options=driver_option)  # Launch Chrome with our settings


# Open a new Chrome browser window
browser = create_webdriver()

# Navigate to the GitHub machine learning collections page
browser.get('https://github.com/collections/machine-learning')

# Find all project elements on the page
# XPATH locates elements by their HTML structure: h1 tags with class 'h3 lh-condensed'
projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

# Dictionary to store project names and their URLs
project_list = {}

# Loop through each project element found on the page
for proj in projects:
    proj_name = proj.text  # Extract the visible text (project name)

    # Find the <a> (link) tag inside the project element and get its href attribute (URL)
    # [0] gets the first link found (in case there are multiple)
    proj_url = proj.find_elements(By.XPATH, "a")[0].get_attribute('href')

    # Add to dictionary: key = project name, value = project URL
    project_list[proj_name] = proj_url

# Close the browser and end the session
browser.quit()

# Convert dictionary to pandas DataFrame for easier data manipulation
# orient='index' means dictionary keys (project names) become row indices
project_df = pd.DataFrame.from_dict(project_list, orient='index')

# Clean up the DataFrame structure
# Step 1: Create a new column 'project_name' from the index (which contains project names)
project_df['project_name'] = project_df.index

# Step 2: Rename columns to be more descriptive
# Column 0 (URLs) becomes 'project_url', Column 1 becomes 'project_name'
project_df.columns = ['project_url', 'project_name']

# Step 3: Reset the index to use standard numerical indexing (0, 1, 2, ...)
# drop=True removes the old index column so we don't have duplicate project names
project_df = project_df.reset_index(drop=True)

# Display the cleaned DataFrame in the console
print(project_df)

# Export the DataFrame to a CSV file in the current directory
# This creates a file called 'project_list.csv' that can be opened in Excel or other tools
# The CSV file will contain all scraped project names and URLs
project_df.to_csv('project_list.csv')

print("\nData successfully exported to 'project_list.csv'!")