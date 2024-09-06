


## datetime Module

The `datetime` module in Python provides classes for working with dates and times. Two important classes from this module are `datetime` and `timedelta`.

### datetime

The `datetime` class represents a date and time.

```python
from datetime import datetime

# Current date and time
now = datetime.now()

# Create a specific datetime
specific_date = datetime(2023, 9, 6, 15, 30, 0)  # 2023-09-06 15:30:00

# Format datetime as string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

# Parse string to datetime
parsed_date = datetime.strptime("2023-09-06 15:30:00", "%Y-%m-%d %H:%M:%S")
```

### timedelta

The `timedelta` class represents a duration of time.

```python
from datetime import timedelta

# Create a duration
duration = timedelta(days=1, hours=2, minutes=30)

# Add duration to a datetime
future_date = datetime.now() + duration

# Calculate difference between two datetimes
diff = future_date - datetime.now()
```
