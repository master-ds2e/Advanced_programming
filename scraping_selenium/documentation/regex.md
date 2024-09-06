## Regular Expressions (regex)

Regular expressions are powerful tools for pattern matching and manipulation of strings. In Python, the `re` module is used for working with regex.

### Quick Explanation of the Regex in `clean_view_count`:

```python
pattern = r"(?P<number>\d+(?:\.\d+)?)(?P<unit>[KMB]?)"
```

- `(?P<number>...)`: Named capturing group for the numeric part
- `\d+`: One or more digits
- `(?:\.\d+)?`: Optional decimal point followed by one or more digits
- `(?P<unit>[KMB]?)`: Named capturing group for the unit (K, M, B, or nothing)

This regex matches strings like "4.8M", "147K", "1.2B", or "500".

### Using regex:

```python
import re

match = re.match(pattern, "4.8M")
if match:
    number = match.group('number')  # "4.8"
    unit = match.group('unit')      # "M"
```

Regular expressions are incredibly powerful but can be complex. It's often helpful to use online regex testers to visualize and test your patterns.