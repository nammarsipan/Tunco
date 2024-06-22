from employee import *
import pandas as pd
import math
from datetime import datetime


class EmployeeBok:

    def __init__(self, col_empId, col_empName, col_totAmount, col_totMeal):
        self.fileName = input("Insert overview file name:")
        self.col_empId = col_empId
        self.col_empName = col_empName
        self.col_totMeal = col_totMeal
        self.col_totAmount = col_totAmount
        self._lonnart = 1006
        self.empBok = self.create_dict_from_file()
        self._month = None
        self._date = None
        self._year = None


    #Initiate the employee book from a file and creates a dict with all the employees
    def create_dict_from_file(self):
        df_temp = pd.read_excel(self.fileName)
        print(f'Succesfully read file {self.fileName}.')

        # drop rows with NaN for column col_empId
        df_temp = df_temp.dropna(subset=[self.col_empId])

        # gets all data in column using column name
        empNames = df_temp[self.col_empName]
        empIds = df_temp[self.col_empId]
        total_meals = df_temp[self.col_totMeal]

        # creates a dict with employee objects
        dict = {}
        for emp, empId, totMeal in zip(empNames, empIds, total_meals):
            temp_emp = Employee(empId, emp, totMeal)
            dict[empId] = temp_emp

        return dict
    
    
    def __getitem__(self, key):
        return self.empBok[key]
    

    def __setvalue__(self, key, value):
        self.empBok[key] = value


    def __contains__(self, key):
        return key in self.empBok


    def __delitem__(self, key):
        del self.empBok[key]


    # returns a formatted string
    def __str__(self):
        emp_str = '\n'.join(f'{emp}' for empId, emp in self.empBok.items())
        str = (f'The following employees are in the EmployeeBok:\n{emp_str} \n'
               f"--------------------------------------------------------------------------------------------------------------------------------------------------------------"
               )
        return str
    

    # read in a new file and update the employee book with new employees
    def update_from_file(self, col_empID, col_empName):
        fName = input("Insert file name Planday salary export:")
        df_temp = pd.read_excel(fName)
        print(f"Succesfully updated from file {fName}.")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
       
        # get all columns value based on column name
        empIds = df_temp[col_empID]
        empNames = df_temp[col_empName]

        # add new employee to empBok if does not exist in empBok
        for ids, name in zip(empIds, empNames, ):
            if ids not in self.empBok:
                temp_employee = Employee(ids, name, 0)
                self.empBok[ids] = temp_employee

    # calulcate meals
        run = True
        
        # Get month input and check for valid input
        while run:
            month = input("Insert month (1 to 12): ")
            try:
                month_int = int(month)
                if 1 <= month_int <= 12:
                    today = datetime.today()

                    # get year in format yyyy
                    self._year = today.strftime("%Y")
                    self._month = month_int
                    self._date = f'{month}-{self._year}'
                    run = False
                else:
                    print("You must nsert a number between 1 to 12")
            except ValueError:
                print("Invalid input")

        # remove diplucae employee IDs
        unique_empIds = list(set(empIds))

        # update number of meas
        nMonthsLeft = 12 - (month_int-1)
        for id in unique_empIds:
            emp = self.empBok[id] 
            newTotMeals = math.floor((emp.get_maxMeals() - emp.get_totalMeals())/nMonthsLeft)
            emp.update_totalMeals(newTotMeals)
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")

    # write new overview and salary import files
    def write_book_to_file(self):

        # wrie new overview file
        data = {

            self.col_empId: [],
            self.col_empName: [],
            self.col_totAmount: [],
            self.col_totMeal: [],
            self._date: []

        }

        for id, emp in self.empBok.items():
            data[self.col_empId].append(int(id))
            data[self.col_empName].append(emp.get_empName())
            data[self.col_totAmount].append(emp.get_totalAmount())
            data[self.col_totMeal].append(emp.get_totalMeals())
            data[self._date].append(emp.get_newMeals())
            
        df_oversikt = pd.DataFrame(data)
        filename = f'Oversikt måltider {self._date}.xlsx'
        df_oversikt.to_excel(filename, index=False)
        print(f"Successful wrote file: {filename}")


        # Write new salary import file for meals
        data = {

            "År": [],
            "Måned": [],
            "Ansattnummer": [],
            "Lønnsart": [], # always 1106
            "Kommentar": [], # always blank
            "Antall": [],
            "Sats": [],
            "Prosjektnummer": [], # always blank
            "Avdelingsnummer": [] # always 1

        }

        for id, emp in self.empBok.items():
            data["År"].append(self._year)
            data["Måned"].append(self._month)
            data["Ansattnummer"].append(emp.get_empID())
            data["Lønnsart"].append(self._lonnart)
            data["Kommentar"].append(None)
            data["Antall"].append(emp.get_newMeals())
            data["Sats"].append(emp.get_costMeal())
            data["Prosjektnummer"].append(None)
            data["Avdelingsnummer"].append(1)

        # drop all rows where Antall = 0
        df_lonnkjoring = pd.DataFrame(data)
        df_lonnkjoring = df_lonnkjoring[df_lonnkjoring["Antall"] != 0]
        
        filename = f'Lonnskjoring {self._date}.xlsx'
        df_lonnkjoring.to_excel(filename, index=False)
        print(f"Successful wrote file: {filename}")