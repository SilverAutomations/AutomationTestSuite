from appium import webdriver

# Desired capabilities to specify the device and app details
desired_caps = {
    "platformName": "Android",
    "platformVersion": "your_android_version",  # e.g., "10.0"
    "deviceName": "your_device_name",           # e.g., "emulator-5554" or device name from `adb devices`
    "appPackage": "com.android.calculator2",    # Calculator app package
    "appActivity": "com.android.calculator2.Calculator",  # Calculator app activity
    "automationName": "UiAutomator2"            # Use UiAutomator2 as the automation engine
}

# Create a WebDriver instance
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Perform actions - for example, pressing a button in the calculator app
# Find the element for digit 2 and click it
digit_2 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
digit_2.click()

# Find the element for the plus button and click it
plus_button = driver.find_element_by_accessibility_id("plus")
plus_button.click()

# Find the element for digit 3 and click it
digit_3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
digit_3.click()

# Find the element for the equals button and click it
equals_button = driver.find_element_by_accessibility_id("equals")
equals_button.click()

# Optionally, get the result and print it
result = driver.find_element_by_id("com.android.calculator2:id/result")
print("The result of the calculation is:", result.text)

# Close the Appium session
driver.quit()
