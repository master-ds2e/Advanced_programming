## 1. Logging

Logging is a way to track events that happen when your program runs. It's more flexible and powerful than using `print()` statements.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    filename='../project_logs.log',
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