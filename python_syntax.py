import pandas as pd

# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 45],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
print("---------------The data frame-----------------")
print(df)

'''
iloc
- df.iloc[row_selection, column_selection] is a powerful way to access rows and columns in a DataFrame based on their integer positions.
- row_selection and column_selection can be integers, lists of integers, slice objects, or boolean arrays.
- : selects all rows or columns in the respective position
'''

# Accessing the first and second rows
print("---------------Accessing the first to second third rows-----------------")
first_two_rows = df.iloc[0:3]
print(first_two_rows)

print("---------------Accessing the 2nd row, data presented as a column-----------------")
print(df.iloc[1])

print("---------------Accessing Row index 0 and 1, and Column index 1 and 2-----------------")
print(df.iloc[0:2,1:2])

print("---------------Accessing the first row (name)-----------------")
print(df.iloc[:1,:])

print("---------------Accessing the first, third and fourth rows, and the first and third columns-----------------")
print(df.iloc[[0, 2, 3], [0, 2]])

print("---------------Accessing specific cell second row, third column-----------------")
print(df.iloc[1, 2])

'''
loc
- df.loc[row_label]: Selects rows by label.
- df.loc[:, column_label]: Selects columns by label.
- df.loc[row_label, column_label]: Selects specific rows and columns by label.
- row_label and column_label can be single labels, lists of labels, slices of labels, or boolean arrays.
'''

# Sample DataFrame with custom index
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 45],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df2 = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# 1. Selecting a single row
print("Single row (row 'a'):")
print(df2.loc['a'])

# 2. Selecting multiple rows
print("\nMultiple rows (rows 'a' and 'c'):")
print(df2.loc[['a', 'c']])

# 3. Selecting a range of rows
print("\nRange of rows (from 'a' to 'c'):")
print(df2.loc['a':'c'])

# 4. Selecting a single column
print("\nSingle column (name):")
print(df2.loc[:, 'name'])

# 5. Selecting multiple columns
print("\nMultiple columns (name and age):")
print(df2.loc[:, ['name', 'age']])

# 6. Selecting a subset of rows and columns
print("\nSubset of rows and columns (rows 'a' to 'c', columns 'name' and 'age'):")
print(df2.loc['a':'c', ['name', 'age']])

# 7. Boolean indexing
print("\nBoolean indexing (selecting rows with a boolean array):")
bool_array = [True, False, True, False, True]
print(df2.loc[bool_array, :])
