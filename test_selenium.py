from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# Specify the grid hub URL
grid_url = "http://localhost:4444/wd/hub"

# Set the desired capabilities
capabilities = DesiredCapabilities.CHROME.copy()

# Set Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Create a remote WebDriver instance pointing to the Selenium Grid hub
driver = webdriver.Remote(
    command_executor=grid_url,
    desired_capabilities=capabilities,
    options=chrome_options
)

# Navigate to a website
driver.get("https://www.example.com")

# Get the page title and print it
print("Title of the page is:", driver.title)

# Close the browser
driver.quit()
