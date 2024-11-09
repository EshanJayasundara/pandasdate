### `pandasdate` - Version 1.0.2

![GitHub release (latest by date)](https://img.shields.io/github/v/release/EshanJayasundara/pandasdate)
![GitHub Repo stars](https://img.shields.io/github/stars/EshanJayasundara/pandasdate?style=social)
![GitHub license](https://img.shields.io/github/license/EshanJayasundara/pandasdate)
![GitHub contributors](https://img.shields.io/github/contributors/EshanJayasundara/pandasdate)

This package, `pandasdate`, is a custom wrapper around `pandas.DataFrame` that introduces a date attribute to track a specified date associated with the dataset. The `DataFrame` subclass is designed to work seamlessly with common data formats while preserving metadata about the date, making it particularly useful for applications that require associating data with a specific timestamp.

Access git-repository via: https://github.com/EshanJayasundara/pandasdate

#### Key Features

1. **Custom Date Attribute**:

   - `DataFrame` objects now include a `date` attribute, which defaults to September 19, 2000, but can be specified upon instantiation.
   - This attribute provides a reference date to keep metadata within the data frame object, enhancing temporal tracking.

2. **Custom String and HTML Representations**:

   - The `__str__` method has been overridden to display the `date` alongside the data when printed in the terminal.
   - `_repr_html_` provides a similar enhancement for Jupyter Notebook environments, appending the date for a more informative display.

3. **File I/O with Date Preservation**:

   - `to_csv`, `to_parquet`, `to_excel`, and `to_pickle` methods automatically include the `date` attribute as a new column, `__date`, before saving the data.
   - When reading files back into memory using `read_csv`, `read_parquet`, `read_excel`, or `read_pickle`, the date is restored from the `__date` column, reconstructing the DataFrame in its original state.

4. **Intelligent Index Handling**:
   - The `_reconstruct` function handles unnamed columns in CSV and Excel files (e.g., `Unnamed: 0`), commonly introduced by default index columns.
   - If `Unnamed: 0` is detected as the first column, it is used as the index, and the column is subsequently removed, resulting in a cleaner DataFrame.

#### Functions in `pandasdate`:

- `DataFrame`: Extends `pd.DataFrame` to include date tracking, custom display, and enhanced I/O.
- `_reconstruct`: Reconstructs DataFrames by restoring the date and intelligently handling unnamed index columns.
- `read_csv`, `read_parquet`, `read_excel`, `read_pickle`: Read functions that reconstruct the DataFrame with the `date` attribute from saved files.

#### Example Usage

```python
import pandasdate as pd_date

# Create a DataFrame with a custom date
df = pd_date.DataFrame({'A': [1, 2, 3]}, year=2024, month=11, day=9)
print(df)

# Save the DataFrame with date information
df.to_csv('data.csv')
df.to_parquet('data.parquet')

# Read back into memory, with date automatically restored
new_df = pd_date.read_csv('data.csv')
print(new_df.date)  # Outputs: 2024-11-09
```

### Release Notes for 1.0.2

- Initial release of `pandasdate`.
- Introduces `DataFrame` subclass with date attribute.
- Custom `__str__` and `_repr_html_` for enhanced displays.
- File I/O methods (`to_csv`, `to_parquet`, `to_excel`, `to_pickle`) that preserve the date.
- `read` methods for all major file formats, reconstructing DataFrames with original date information.

This release lays a robust foundation for future enhancements, including potentially adding custom date operations and compatibility with additional file formats.

```
Release 1.0.0 and release 1.0.1 was removed due to some inconsistancies.
```
