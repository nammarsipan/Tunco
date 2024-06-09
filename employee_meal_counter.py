import pandas as pd
import openpyxl

# fixed costs per meal and max amount of meal per employee
cost_per_meal = 50
max_number_meal = 100
col_employee = 'Employee'
col_emp_id = "Ansattnummer"
col_amount_meal = 'Meal amounts in kr'
col_tot_meal = 'Total number of meals'

print('------------------------------Initiation----------------------------------')
print('Cost per meal:', cost_per_meal)
print('Max number of meal per employee:', max_number_meal)
print(f'The following column names have been initiated: {col_employee}, {col_emp_id}, {col_amount_meal}, {col_tot_meal}')
print('--------------------------------------------------------------------------')

# returns a nested dict with eName as key. Nested dict has eID, nMeals, aMeals as key
# eName = column name for Employee Name
# eID = column name for employeeID
# nMeals = column name for total number of meals
# aMeals = column name for total amount of meals in kr
def create_dict(df, eName, eID, nMeals, aMeals):
    
    dict = {}

    # gets all data in column using column name
    employees = df[eName]
    employeeIDs = df[eID]
    total_meals = df[nMeals]
    amount_meals = df[aMeals]

    # creates a list with all employee names
    list_emp = []
    for emp in employees:
        list_emp.append(emp)

    #creates a list with all employeeID
    list_empID = []
    for empid in employeeIDs:
        list_empID.append(empid)

    #creates a list with total meals
    list_number_meals = []
    for meals in total_meals:
        list_number_meals.append(meals)

    #creates a list with total meals
    list_amount_meals = []
    for amount in amount_meals:
        list_amount_meals.append(amount)

    # creates a nested dict empID
    for emp, empID, numberMeals, amountMeals in zip(list_emp, list_empID, list_number_meals, list_amount_meals):
        temp_dict = {
            eID: empID,
            nMeals: numberMeals,
            aMeals: amountMeals
            }
        dict[emp] = temp_dict
    
    print(dict)



def create_dict_from_file(path, sheetName):
    df_oversikt = pd.read_excel(path, sheet_name=sheetName)
    print(f"Succesfully read file {path}. Dataframe has been created.")
    print(df_oversikt)

    



create_dict_from_file('meals_overview_2024.xlsx', 'Oversikt måltider')