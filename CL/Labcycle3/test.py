# # List of lists (matrix)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# trasns = [list(column) for column in zip(*matrix)]
    
# print(trasns)

import pandas as pd
from tabulate import tabulate

# Create a DataFrame
data = pd.DataFrame(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
    columns=['Column1', 'Column2', 'Column3'],  # Column names
    index=['Row1', 'Row2', 'Row3']             # Row names
)
# print(tabulate(data, tablefmt="grid", headers="keys"))
# print(data.index.to_list())
# print(data.columns.to_list())

# data.drop('Row1', inplace=True)
# data.drop('Column1', axis=1, inplace=True)
# print(tabulate(data, tablefmt="grid", headers="keys"))

print(data.iloc[:,0])
print(data.iloc[0])
print(data['Column1'])
print(data.loc['Row1'])

