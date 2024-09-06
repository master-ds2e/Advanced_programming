# Python: Docstrings and Doctests

## Docstrings

Docstrings are string literals that appear right after the definition of a function, method, class, or module. They are used to document the purpose and behavior of the code.

### Example from `clean_view_count`:

```python
def clean_view_count(view: str) -> int:
    """
    Convert a YouTube view count string to an integer.

    Args:
    - view (str): The view count string, which may include 'K' (thousand), 'M' (million), or 'B' (billion) suffixes.

    Returns:
    - int: The numeric view count.

    Examples:
    >>> clean_view_count("4.8M")
    4800000
    >>> clean_view_count("147K")
    147000
    >>> clean_view_count("1.2B")
    1200000000
    >>> clean_view_count("500")
    500
    >>> clean_view_count("Not a number")
    -1
    """
    # Function implementation...
```

Docstrings can include:
- A brief description of the function
- Args: Description of parameters
- Returns: Description of the return value
- Examples: Demonstrating usage and expected outputs
- Raises: Description of exceptions that might be raised

## Doctests

Doctests are a way to embed tests directly in the docstrings of Python functions, modules, or classes. They serve dual purposes:
1. As documentation, showing how to use the function and what to expect.
2. As test cases that can be automatically executed to verify the code's behavior.

### Writing Doctests

Doctests are written as if they were typed into the Python interactive interpreter. They consist of Python expressions or statements, followed by their expected output.

```python
def add(a, b):
    """
    Add two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(3.14, 2.86)
    6.0
    """
    return a + b
```

### Running Doctests

To run doctests, you can use the `doctest` module. Add this at the end of your Python file:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

When you run the script, it will execute all the doctests in the file and report any failures.

### Benefits of Doctests

1. **Documentation and Testing Combined**: Doctests serve as both documentation and tests, ensuring that your examples are accurate and up-to-date.
2. **Readable Tests**: Doctests are easy to read and understand, as they mimic interactive Python sessions.
3. **Maintenance**: When you update your code, you're reminded to update the documentation and tests simultaneously.

### Best Practices

1. Keep doctests simple and focused on demonstrating typical usage.
2. Include edge cases and potential error conditions in your doctests.
3. Use doctests for simple functions; for more complex testing scenarios, consider using a dedicated testing framework like `unittest` or `pytest`.

Doctests are an excellent tool for ensuring that your code examples work as expected and for maintaining the accuracy of your documentation over time.