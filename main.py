from employee_bok import *

# initiate column names
empId = "Employee ID"
empName = 'Employee'
totalMeal = 'Total number of meals'
totalAmount = "Total amount in kr"


print("**************************************************************************************************************************************")

# creates an employee book dictionary from reference file
ansBok = EmployeeBok(empId, empName, totalAmount, totalMeal)
print(ansBok)

# add new employees from planday export, and calculate new amount of meals
ansBok.update_from_file("Ansattnummer", "Ansattnavn")
# print(ansBok)

# remove André Evju
del ansBok[2]
print("Andre Evju has been removed.")

# write to files
ansBok.write_book_to_file()