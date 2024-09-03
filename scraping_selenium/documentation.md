## 1. Logging

Logging is a way to track events that happen when your program runs. It's more flexible and powerful than using `print()` statements.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    filename='project_logs.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
```
logging.basicConfig(): Sets up the basic configuration for the logging system.

level: Sets the minimum severity of messages to log (INFO logs all levels from INFO and above).
1.  `logger.debug("This is a debug message")`
2. `logger.info("Program is running normally")`
3. `logger.warning("This action might cause an issue")`
4. `logger.error("An error occurred while processing the file")`
5. `logger.critical("Critical error: database connection lost")`
filename: Specifies the file where logs will be written.
filemode: 'a' means append (add to existing file), 'w' would overwrite.
format: Defines how each log message will be structured.

logger = logging.getLogger(__name__): Creates a logger object for this module.

Use logging to record important events, errors, and debug information in your program.
example:
```python
def process_data(data):
    logger.info(f"Processing data with {len(data)} records")
    try:
        result = perform_calculation(data)
        logger.debug(f"Calculation result: {result}")
        return result
    except ValueError as e:
        logger.error(f"Error processing data: {str(e)}")
        return None
```

## 2. Selenium
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

## 3. Try-Except-Finally Structure
This structure helps manage exceptions (errors) and ensures proper resource cleanup.

```python
try:
    # Code that might raise an exception
except Exception as e:
    # Code to handle exceptions
finally:
    # Code that will always run, even if there's an exception
```

## 4. if name == "main"

```python
if __name__ == "__main__":
    # Do something
```
This idiom is used to check whether a Python script is being run directly or being imported as a module.

When a Python file is run directly, __name__ is set to "__main__".
When a file is imported as a module, __name__ is set to the module's name.

Using this check allows you to write code that only runs when the script is executed directly, not when it's imported as a module in another script.