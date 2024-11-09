# pandasdate

`pandasdate 1.0.0`
an extension to pandas dataframe including the created date of the DataFrame.

Here is an example usecase,

```python
import numpy as np
import pandasdate as pdd

df = pdd.DataFrame(
    np.array([1, 2, 3, 4]).reshape((2, 2)),
    index=np.array([1, 2]), columns=['col_1', 'col_2'],
    year=2024,
    month=11,
    day=9
    )

df.to_pickle('npa.pickle')
print(pdd.read_pickle('npa.pickle'), end='\n\n')

df.to_csv('npa.csv')
print(pdd.read_csv('npa.csv'), end='\n\n')

df.to_parquet('npa.parquet')
print(pdd.read_parquet('npa.parquet'), end='\n\n')

df.to_excel('npa.xlsx')
print(pdd.read_excel('npa.xlsx'), end='\n\n')
```
