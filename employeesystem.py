from abc import ABC, abstractmethod

#Abstract class for Role

class Role(ABC):
    abstractmethod
    def get_salary(self):
        pass

    abstractmethod
    def get_title(self):
        pass


# class for specific roles
class Developer(Role):
    def __init__(person, salary):
        person.salary = salary
        person.title = "Developer"

    def get_salary(person):
        return person.salary

    def get_title(person):
        return person.title


class Manager(Role):
    def __init__(person, salary):
        person.salary = salary
        person.title = "Manager"

    def get_salary(person):
        return person.salary

    def get_title(person):
        return person.title


# Employee class
class Employee:
    def __init__(self, name, employee_id, role):
        self.__name = name  # private attribute
        self.__employee_id = employee_id  # private attribute
        self.role = role  # role is an instance of Role

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        return f"Name: {self.get_name()}, ID: {self.get_employee_id()}, Role: {self.role.get_title()}, Salary: {self.role.get_salary()}"


# Subclass for Manager
class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, Manager(salary))

    def display_info(self):
        return f"Manager - {super().display_info()}"


# Subclass for Intern
class Intern(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, Developer(salary))

    def display_info(self):
        return f"Intern - {super().display_info()}"


# Department class
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.get_employee_id() != employee_id]

    def display_employees(self):
        for employee in self.employees:
            print(employee.display_info())


if __name__ == "__main__":
    dev_role = Developer(60000)
    manager_role = Manager(90000)

    emp1 = Manager("Alice", 1, manager_role.get_salary())
    emp2 = Intern("Bob", 2, dev_role.get_salary())

    department = Department("Engineering")
    department.add_employee(emp1)
    department.add_employee(emp2)

    print(f"Employees in {department.name} department:")
    department.display_employees()

    # Removing an employee
    department.remove_employee(1)
    print("After removing employee with ID 1:")
    department.display_employees()
