import json
import os

class Employee:
    def __init__(self, emp_id, name, position, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def calculate_salary(self, allowances=0, bonus=0):
        return self.base_salary + allowances + bonus

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "position": self.position,
            "base_salary": self.base_salary
        }

class EmployeeManager:
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.employees = self.load_employees()

    def load_employees(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return [Employee(**emp) for emp in json.load(file)]
        return []

    def save_employees(self):
        with open(self.filename, "w") as file:
            json.dump([emp.to_dict() for emp in self.employees], file)

    def add_employee(self, emp):
        self.employees.append(emp)
        self.save_employees()

    def update_employee(self, emp_id, name=None, position=None, base_salary=None):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                if name: emp.name = name
                if position: emp.position = position
                if base_salary: emp.base_salary = base_salary
                self.save_employees()
                return True
        return False

    def delete_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                self.employees.remove(emp)
                self.save_employees()
                return True
        return False

    def display_employees(self):
        for emp in self.employees:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Position: {emp.position}, Base Salary: ₹{emp.base_salary}")

    def calculate_employee_salary(self, emp_id, allowances=0, bonus=0):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                total_salary = emp.calculate_salary(allowances, bonus)
                print(f"Total Salary for {emp.name}: ₹{total_salary}")
                return total_salary
        print("Employee not found.")
        return None

manager = EmployeeManager()
manager.add_employee(Employee(1, "Vinit Sharma", "Developer", 50000))
manager.add_employee(Employee(2, "Yuvraj Sharma", "Manager", 70000))
manager.display_employees()
manager.update_employee(1, base_salary=55000)
manager.calculate_employee_salary(1, allowances=5000, bonus=3000)
manager.delete_employee(2)
manager.display_employees()
