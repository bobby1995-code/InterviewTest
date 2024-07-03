from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with the path to your ChromeDriver executable
chrome_driver_path = '/Users/pc/Downloads/chromedriver'

# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

try:
    # Open the web page
    driver.get("http://localhost:6464/")  # Replace with your application's URL

    # Find the input field and submit button
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "number"))
    )
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "getFactorial"))
    )

    # Enter the number 7 into the input field
    input_field.clear()  # Clear existing input (if any)
    input_field.send_keys("7")

    # Click the submit button
    submit_button.click()

    # Wait for the calculation to complete (assuming the result is displayed dynamically)
    time.sleep(1)  # Adjust the sleep time as needed based on your application's responsiveness

    # Find the element that displays the result
    result_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "resultDiv"))
    )

    # Get the text content of the result element
    result_text = result_element.text

    # Assert that the result matches the expected factorial value
    expected_result = "5040"  # This is the factorial of 7
    assert result_text.strip() == expected_result, f"Expected result: {expected_result}, but got: {result_text}"

    print("Factorial of 7 is correctly calculated as 5040!")

finally:
    # Close the browser window
    driver.quit()
