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


'''
reading from excel file
Use pd.read_excel('file.xlsx') to read an Excel file.
Use sheet_name to specify which sheet to read.
Additional parameters such as header, names, usecols, and skiprows can help customize the reading process.

'''

# Reading an Excel file
df2 = pd.read_excel('path_to_your_file.xlsx')

# Displaying the first few rows of the DataFrame
print(df2.head())

# Reading a specific sheet by name
df2 = pd.read_excel('path_to_your_file.xlsx', sheet_name='Sheet1')

# Reading a specific sheet by index (0-based)
df2 = pd.read_excel('path_to_your_file.xlsx', sheet_name=0)

# Displaying the first few rows of the DataFrame
print(df2.head())

# Reading all sheets
dfs = pd.read_excel('path_to_your_file.xlsx', sheet_name=None)

# Displaying the names of the sheets and the first few rows of each DataFrame
for sheet_name, df in dfs.items():
    print(f"Sheet name: {sheet_name}")
    print(df.head())

'''
header: Row (0-indexed) to use for the column labels. Defaults to 0.
names: List of column names to use. If file contains no header row, then you should explicitly pass header=None.
usecols: String or list of columns to parse.
skiprows: List of rows to skip (0-indexed) or number of rows to skip (int) at the start of the file.
'''

# Reading an Excel file with additional parameters
'''
'path_to_your_file.xlsx':
This is the path to the Excel file you want to read. It could be a relative or absolute path to the file on your filesystem.

sheet_name='Sheet1':
This parameter specifies the name of the sheet in the Excel file to read. Here, it reads the sheet named 'Sheet1'. If this parameter were omitted, pandas would read the first sheet by default.

header=0:
This parameter specifies which row to use as the column names. The row index is 0-based, so header=0 means that the first row of the specified sheet will be used as the column names. If the header is not specified, pandas uses the first row by default.


usecols='A:C':
This parameter specifies which columns to read. 'A:C' means that pandas will read columns A, B, and C from the sheet. You can also use a list of column names or a range of indices to specify the columns.
skiprows=2:
This parameter specifies the number of rows to skip at the beginning of the sheet. Here, skiprows=2 means pandas will skip the first two rows of the sheet. This is useful if there are metadata or irrelevant rows at the top of the sheet that you do not want to include in your DataFrame.
'''
df2 = pd.read_excel('path_to_your_file.xlsx', sheet_name='Sheet1', header=0, usecols='A:C', skiprows=2)

# Displaying the first few rows of the DataFrame
print(df2.head())

# Reading the Excel file
df2 = pd.read_excel('example.xlsx', sheet_name='Data')

# Displaying the first few rows of the DataFrame
print(df2.head())


'''
Creating dataframe using loops
'''
# Initialize an empty dictionary to store the data
data = {
    'name': [],
    'age': [],
    'city': []
}

# Use a for loop to generate data
for i in range(5):
    data['name'].append(f'Person {i}')
    data['age'].append(20 + i)
    data['city'].append(f'City {i}')

# Create the DataFrame from the dictionary of lists
df = pd.DataFrame(data)
print(df)


# Initialize an empty list to store the data
data = []

# Use a for loop to generate data
for i in range(5):
    row = [f'Person {i}', 20 + i, f'City {i}']
    data.append(row)

# Define the column names
columns = ['name', 'age', 'city']

# Create the DataFrame from the list of lists
df = pd.DataFrame(data, columns=columns)
print(df)



'''
Writing to file

'''

# Sample DataFrames
data1 = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
df1 = pd.DataFrame(data1)

data2 = {
    'product': ['Apples', 'Oranges', 'Bananas'],
    'price': [1.2, 2.5, 0.8]
}
df2 = pd.DataFrame(data2)

# Writing DataFrames to an Excel file
with pd.ExcelWriter('example_output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='People', index=False)
    df2.to_excel(writer, sheet_name='Products', index=False)

# Writing with custom options
df1.to_excel('example_custom_output.xlsx', sheet_name='Sheet1', startrow=1, startcol=2, na_rep='NA')


# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'age': [25, 30, 35, 40, 45],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)

# Writing to an Excel file
df.to_excel('output.xlsx', sheet_name='Sheet1')


'''
Sum row
'''
data = {
    'X': [0, 0, 0, 0, 0, 0],
    'MyColumn': [84, 0, 0, 0, 0, 84],
    'Y': [13.0, 77.0, 69.0, 28.0, 20.0, 193.0],
    'Z': [69.0, 127.0, 16.0, 31.0, 85.0, 70.0]
}

df = pd.DataFrame(data)

# sum value for index 0
col_total = df.loc[0].sum()


'''
Sum column
'''

# Create a sample dataframe
data = {
    'X': ['A', 'B', 'C', 'D', 'E', 'F'],
    'MyColumn': [84, 76, 28, 28, 19, 84],
    'Y': [13.0, 77.0, 69.0, 28.0, 20.0, 193.0],
    'Z': [69.0, 127.0, 16.0, 31.0, 85.0, 70.0]
}

df = pd.DataFrame(data)

# Calculate the sum of the 'MyColumn'
total = df['MyColumn'].sum()

# Print the total
print(f"Total of 'MyColumn': {total}")

