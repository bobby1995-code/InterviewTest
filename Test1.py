from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://192.168.8.101:6464")  

# This is the actual xpath on the url provided
error_message = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/p")

# This is the actual CSS Selector on the url provided
result_div = driver.find_element_by_css_selector('#resultDiv')

# Example using XPath to find the error message element
error_message = driver.find_element_by_xpath("//input[contains(@style, 'border-color: red')]")

# Example using CSS selector to find elements with red form validation styling
elements_with_red_validation = driver.find_elements_by_css_selector("input:invalid")


print(error_message.text)  

driver.quit()
