import pickle


class Employee():
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.id, '\t', self.name, '\t', self.salary)



with open('../files/employee.txt','wb') as file:
    emp = Employee(2,'sahitya',30000)
    pickle.dump(emp,file)