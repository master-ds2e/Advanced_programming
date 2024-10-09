The database is available on
[kaggle](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots).


You can find many more datasets, and the notebooks of people analysing them.

There is also a pandas class you can try: [here](https://www.kaggle.com/learn/pandas)
or create your own:

You're right! Let's correct the first example to demonstrate how to create a DataFrame from a list of lists, where each inner list represents a row, and you can specify the column names separately.

### 1. **Creating a DataFrame from a List of Lists**

If you have a list of lists, where each inner list represents a row of data, you can pass it to `pd.DataFrame()` along with the column names.

```python
import pandas as pd

# Data as a list of lists (each inner list is a row)
data = [
    ['Movie A', 100, 300],
    ['Movie B', 150, 500],
    ['Movie C', 200, 700]
]

# Creating DataFrame by specifying the column names
df_from_lists = pd.DataFrame(data, columns=['Title', 'Budget', 'Box Office'])

# Display the DataFrame
print(df_from_lists)
```

### 2. **Creating a DataFrame from a Dictionary**

If you prefer to create the DataFrame from a dictionary, where the keys are column names, and the values are lists of data for each column:

```python
import pandas as pd

# Data as a dictionary (each key is a column name, and values are the column data)
data = {
    'Title': ['Movie A', 'Movie B', 'Movie C'],
    'Budget': [100, 150, 200],
    'Box Office': [300, 500, 700]
}

# Creating DataFrame
df_from_dict = pd.DataFrame(data)

# Display the DataFrame
print(df_from_dict)
```

### Key Points:
- When using **a list of lists**, each inner list represents a row, and you specify the column names when creating the DataFrame.
- When using **a dictionary**, the keys are column names, and the values are lists representing the column data.