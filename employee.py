class Employee:

    def __init__(self, empId, empName, totalMeals):
        self.empId = empId
        self.empName = empName
        self.totalMeals = totalMeals
        self.maxAmount = 5000
        self.costMeal = 50
        self.newMeals = 0
        self.maxMeals = self.maxAmount / self.costMeal
        self.totalAmount = self.totalMeals * self.costMeal

    def get_empID(self):
        return int(self.empId)
    
    def get_empName(self):
        return self.empName
    
    def get_totalMeals(self):
        return self.totalMeals
    
    def get_totalAmount(self):
        return self.totalAmount
    
    def get_maxMeals(self):
        return self.maxMeals
    
    def get_newMeals(self):
        return self.newMeals
    
    def get_costMeal(self):
        return self.costMeal

    def __str__(self):
        return(f'Employee ID: {self.empId}, Employee name: {self.empName}, Total meals: {self.totalMeals}, Total amount: {self.totalAmount}')
    
    #update number of total meals
    def update_totalMeals(self, newMeals):
        self.newMeals = newMeals
        self.totalMeals += newMeals
        self.totalAmount = self.totalMeals * self.costMeal
        print(f'{self.empName} has {self.newMeals} added. Total meals: {self.totalMeals}')