# Python Error Handling: try-except

Error handling is crucial in programming to manage unexpected situations gracefully. Python uses the try-except structure for this purpose.

## Basic Structure

```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
```

## Extended Structure

```python
try:
    # Code that might raise an exception
except ExceptionType1:
    # Handle exception of ExceptionType1
except ExceptionType2:
    # Handle exception of ExceptionType2
except Exception as e:
    # Handle any other exceptions
else:
    # Code to run if try block succeeds
finally:
    # Code that will always run, regardless of exceptions
```

## Key Points

1. **Multiple except blocks**: You can have multiple except blocks to handle different types of exceptions differently.

2. **Catching specific exceptions**: It's generally better to catch specific exceptions rather than using a bare except clause.

3. **The else clause**: Code in the else block runs if the try block doesn't raise an exception.

4. **The finally clause**: Code in the finally block always runs, whether an exception occurred or not. It's useful for cleanup operations.

5. **Exception as e**: This syntax allows you to access the exception object, which can be useful for logging or displaying error messages.

## Example

```python
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Invalid types for division!")
    else:
        print(f"The result is {result}")
    finally:
        print("Executing finally clause")

# Usage
divide(10, 2)  # Successful division
divide(10, 0)  # Division by zero
divide('10', 2)  # Type error
```

This structure allows for robust error handling, making your code more resilient and user-friendly.