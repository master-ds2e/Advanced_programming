

## Selenium
Selenium WebDriver is a tool for automating web browser interaction.
Selenium offers a wide range of functions for web automation and scraping. Here are some of the most commonly used and useful ones:
from selenium import webdriver

Example: Scrapping YouTube: [Link](https://scrapingking.medium.com/scrape-youtube-comments-using-python-and-selenium-43a7b39d80c3)

### 1. Finding Elements

- `find_element(By.ID, "id")`: Finds an element by its ID.
- `find_element(By.NAME, "name")`: Finds an element by its name attribute.
- `find_element(By.XPATH, "xpath")`: Finds an element using XPath.
- `find_element(By.CSS_SELECTOR, "selector")`: Finds an element using CSS selectors.
- `find_elements(By.CLASS_NAME, "class")`: Finds all elements with a specific class name.

### 2. Interacting with Elements

- `element.click()`: Clicks on an element.
- `element.send_keys("text")`: Types text into an input field.
- `element.clear()`: Clears the content of a text input.
- `element.text`: Retrieves the visible text of an element.
- `element.get_attribute("attribute")`: Gets the value of a specified attribute.

### 3. Waits
- `WebDriverWait(driver, timeout).until(expected_condition)`: Waits for a condition to be true before proceeding.

Example:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myDynamicElement"))
)
```

### 4. Navigation

- `driver.get("url")`: Navigates to a specific URL.
- `driver.back()`: Goes back to the previous page.
- `driver.forward()`: Goes forward to the next page.
- `driver.refresh()`: Refreshes the current page.

### 5. Window Management

- `driver.switch_to.window(handle)`: Switches to a different window or tab.
- `driver.switch_to.frame(frame_reference)`: Switches to an iframe.
- `driver.switch_to.default_content()`: Switches back to the main frame.

### 6. JavaScript Execution

- `driver.execute_script("script")`: Executes JavaScript in the context of the current page.

Example:
```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
```