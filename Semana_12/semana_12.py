## ---------------------------------------------------------------------------------------------

# 1. Cree una clase de `BankAccount` que:
#     1. Tenga un atributo de `balance`.
#     2. Tenga un método para ingresar dinero.
#     3. Tengo un método para retirar dinero.
    
#     Cree otra clase que herede de esta llamada `SavingsAccount` que:
    
#     1. Tenga un atributo de `min_balance` que se pueda asignar al crearla.
#     2. Arroje un error si al intentar retirar dinero, el retiro haría que el `balance` quede debajo del `min_balance`. 
#     Es decir que sí se pueden hacer retiros **siempre y cuando** el `balance` quede arriba del `min_balance`.


# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def enter_money(self,add_amount):
#         self.balance += add_amount
#         return self.balance

#     def withdraw_money(self, deduct_amount):
#         self.balance -= deduct_amount
#         return self.balance


# class SavingsAccount(BankAccount):
#     def __init__(self,min_balance,balance): ### I had to define in the init method of the child class the parameter "balance" and then initialize it from the parent class using the "super(). method"
#         super().__init__(balance)
#         self.min_balance = min_balance

#     def withdraw_money(self, deduct_amount):
#         total_amount = self.balance - self.min_balance
#         if deduct_amount > total_amount:
#             print("You cannot withdraw money")
#         else:
#             self.balance -= deduct_amount
#             print(f"Proceed with withdraw, your remaining balance is {self.balance}")
#             return self.balance

# test = SavingsAccount(100, 2000)
# test.withdraw_money(1000)
# print(test.enter_money(100))
# test.withdraw_money(200)

## ---------------------------------------------------------------------------------------------

# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

### Error while trying to instantiate an abstract method ###
## TypeError: Can't instantiate abstract class Test without an implementation for abstract method 'test_print'
###

# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def calculate_perimeter(self):
#         pass

#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def calculate_perimeter(self):
#         print(f"The perimeter of the circle is {2 * math.pi * self.radius}")

#     def calculate_area(self):
#         print(f"The area of the circle is {math.pi * (self.radius**2)}")

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side

#     def calculate_perimeter(self):
#         print(f"The perimeter of the square is {4 * self.side}")

#     def calculate_area(self):
#          print(f"The area of the square is {self.side ** 2}")

# class Rectangle(Shape):
#     def __init__(self,length, width):
#         self.length = length
#         self.width = width

#     def calculate_perimeter(self):
#         print(f"The perimeter of the rectangle is { 2 * (self.length + self.width)}")

#     def calculate_area(self):
#         print(f"The area of the rectangle is {self.length * self.width}")


# figure1 = Circle(10)
# figure1.calculate_perimeter()
# figure1.calculate_area()

# figure1 = Square(20)
# figure1.calculate_perimeter()
# figure1.calculate_area()

# figure1 = Rectangle(30,20)
# figure1.calculate_perimeter()
# figure1.calculate_area()

## ---------------------------------------------------------------------------------------------
# 3. Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

# class Employee:
#     def __init__(self,name,last_name):
#         self.name = name
#         self.last_name = last_name

#     def email(self):
#         return f"Email address is {self.name.lower()}.{self.last_name.lower()}@company.com"

# class Department(Employee):
#     def __init__(self,name,last_name,code):
#         self.code = code
#         super().__init__(name,last_name) ### No need to add the "self" attribute to execute it###


#     def department_code(self):
#         department_list = ["manufacturing", "sales", "finance", "legal", "corp"]
#         if self.code == 1:
#             department = department_list[0]
#         if self.code == 2:
#             department = department_list[1]
#         if self.code == 3:
#             department = department_list[2]
#         if self.code == 4:
#             department = department_list[3]
#         if self.code == 5:
#             department = department_list[4]
#         return department  ### If I don't return thr value, then it will print "None" ###


# class Pay(Department,Employee):
#     def __init__(self,name,last_name,code,pay=0):
#         self.pay = pay
#         super().__init__(name,last_name,code)
        

#     def payment(self):
#         if self.code == 1:
#             pay = 10000
#         if self.code == 2:
#             pay = 20000
#         if self.code == 3:
#             pay = 30000
#         if self.code == 4:
#             pay = 40000
#         if self.code == 5:
#             pay = 50000
#         print(f"The employee {self.name.title()} {self.last_name.title()} works in the {self.department_code()} department. {self.email()}, Payment of {pay}\n") 
#         ### In the line above (163) I am calling the "self.department_code()" method's attributes value ###
        

# employee1 = Pay("lisa", "simpson", 1)
# employee1.payment()
# employee2 = Pay("john", "doe", 2)
# employee2.payment()

## Got MRO error (Cannot create a consistent method resolution order (MRO) for bases)
## I was calling the class the other way around (Employee, Department) instead of (Department, Employee)
##  https://chatgpt.com/share/6835346f-30c8-800c-a3b8-538e59782c0



## ---------------------------------------------------------------------------------------------