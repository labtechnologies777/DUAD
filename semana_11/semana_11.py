# 1. Cree una clase de `Circle` con:
#     1. Un atributo de `radius` (radio).
#     2. Un método de `get_area` que retorne su área.

# import math

# class Circle():
#     def __init__(self,radius):
#         self.radius = radius 

#     def get_area(self):
#         return f"The area of the circle is {math.pi * (self.radius**2)}"

# circle_1 = Circle(50)
# print(circle_1.get_area())

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

# 2. Cree una clase de `Bus` con:
#     1. Un atributo de `max_passengers`.
#     2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). 
# **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#     3. Un método para bajar pasajeros uno por uno (en cualquier orden).


# class Person:
#     def __init__(self):
#         name = input("Who's getting on the bus? ")
#         self.name = name

#     def __repr__(self):
#         return f"Person(name={self.name})"


# class Bus:
#         def __init__(self,max_passenger):
#             self.passenger_list = []
#             self.max_passenger = max_passenger
            

#         def add_passengers(self,passenger):
#                 if len(self.passenger_list) < self.max_passenger:
#                     self.passenger_list.append(passenger)
#                 else:
#                     print("Bus capacity reached. No more passengers allowed")
#                 print(self.passenger_list)
#                 return self.passenger_list

        
#         def remove_passengers(self,passenger_list):
#             name = input("Enter a name for a user you want to delete: ")
#             for passenger in self.passenger_list:
#                 if name == passenger.name:
#                     self.passenger_list.remove(passenger)
#             print(self.passenger_list)

# passenger_1 = Person()
# passenger_2 = Person()
# passenger_3 = Person()
# passenger_4 = Person()
# bus = Bus(3)
# bus.add_passengers(passenger_1)
# bus.add_passengers(passenger_2)
# bus.add_passengers(passenger_3)
# bus.add_passengers(passenger_4)
# bus.remove_passengers(passenger_1)
# bus.remove_passengers(passenger_2)

#-----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# 3. Duplique el proyecto [Sistema de Control de Estudiantes]
# y modifíquelo para usar objetos para guardar la información de los estudiantes (creando una clase de `Student`).
#     1. Hay que cambiar los estudiantes de diccionarios a objetos.
#     2. Hay que convertir la data del csv de diccionario a objeto al importar.
#     3. Hay que convertir los objetos a diccionario al exportar a csv.
#     4. Hay que modificar el acceso a los keys para accesar a atributos.
#         1. student[’Name’] → student.name

# from menu import menu
# menu()


#-----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# 4. Cree las siguientes clases:
#     1. `Head`
#     2. `Torso`
#     3. `Arm`
#     4. `Hand`
#     5. `Leg`
#     6. `Feet`
#     7. Ahora cree una clase de `Human` y conecte todas las clases de manera lógica por medio de atributos.


# class Head:
#     def __init__(self, eyes, ears, mouth, nose):
#         self.eyes = eyes
#         self.ears = ears
#         self.mouth = mouth
#         self.nose = nose

#     def __str__(self):
#         return f"The head has {self.eyes} eyes, {self.ears} ears, {self.mouth} mouth and {self.nose} nose"

# class Torso:
#     def __init__(self, right_arm, left_arm, right_leg, left_leg):
#         self.right_arm = right_arm
#         self.left_arm = left_arm
#         self.right_leg = right_leg
#         self.left_leg = left_leg

#     def __str__(self):
#         return f"The torso has two arms. {self.right_arm}. The torso also has two legs. {self.right_leg}"

# class Arm:
#     def __init__(self,hand):
#         self.hand = hand

#     def __str__(self):
#         return f"Each arm has a hand. {self.hand}"

# class Hand:
#     def __init__(self,fingers):
#         self.fingers = fingers

#     def __str__(self):
#         return f"The hand has {self.fingers} fingers"

# class Leg:
#     def __init__(self,feet):
#         self.feet = feet

#     def __str__(self):
#         return f"Each leg has a foot. {self.feet}"

# class Feet:
#     def __init__(self,toes):
#         self.toes = toes

#     def __str__(self):
#         return f"The foot has {self.toes} toes."

# class Human:
#     def __init__(self,head, torso):
#         self.head = head
#         self.torso = torso

#     def __str__(self):
#         return f"""Human body is commposed as follows: 
#         1. {self.head}
#         2. {self.torso}
#         """

# person_right_hand = Hand("five")
# person_left_hand = Hand("five")
# person_right_arm = str(Arm(person_right_hand))
# person_left_arm = Arm(person_left_hand)

# person_right_feet = Feet("five")
# person_left_feet = Feet("five")
# person_right_leg = Leg(person_right_feet)
# person_left_leg = Leg(person_left_feet)

# person_torso = Torso(person_right_arm,person_left_arm,person_right_leg,person_left_leg)
# person_head = Head("two", "two", "one", "one")

# person_body = Human(person_head, person_torso)
# print(person_body)
