# 1. Cree una clase de `Circle` con:
#     1. Un atributo de `radius` (radio).
#     2. Un método de `get_area` que retorne su área.

# class Circle():

#     def get_area(self,radius):
#         self.radius = radius 
#         pi = float(3.14159265)
#         print(f"The area of the circle is {pi * (radius**2)}")

# circle_1 = Circle()
# circle_1.get_area(50)

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

# 2. Cree una clase de `Bus` con:
#     1. Un atributo de `max_passengers`.
#     2. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). 
# **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
#     3. Un método para bajar pasajeros uno por uno (en cualquier orden).


# class Person:
#     def __init__(self,name):
#         self.name = name

#     def __repr__(self):
#         return f"Person(name={self.name})"

# class Bus:
#         passenger_list = []
#         max_passenger = 3
#         def add_passengers(self):
#             while len(self.passenger_list) < self.max_passenger:
#                 name = input("Who's getting on the bus? ")
#                 self.passenger_list.append(Person(name))
#             else:
#                 print("Bus capacity reached. No more passengers allowed")
#             print(self.passenger_list)
#             return self.passenger_list
        
#         def remove_passengers(self,passenger_list):
#             name = input("Enter a name for a user you want to delete: ")
#             for passenger in self.passenger_list:
#                 if name == passenger.name:
#                     self.passenger_list.remove(passenger)
#             print(self.passenger_list)
        

# passenger_1 = Bus()
# passenger_1.add_passengers()
# passenger_2 = Bus()
# passenger_2.remove_passengers(passenger_1)

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


# class Torso:
#     def __init__(self, right_arm, left_arm, right_leg, left_leg):
#         self.right_arm = right_arm
#         self.left_arm = left_arm
#         self.right_leg = right_leg
#         self.left_leg = left_leg


# class Arm:
#     def __init__(self,hand, elbow, shoulder):
#         self.hand = hand
#         self.elbow = elbow
#         self.shoulder = shoulder


# class Hand:
#     def __init__(self,fingers, knuckles):
#         self.fingers = fingers
#         self.knuckles = knuckles


# class Leg:
#     def __init__(self,feet, knee):
#         self.feet = feet
#         self.knee = knee
        


# class Feet:
#     def __init__(self,toes,anckle):
#         self.toes = toes
#         self.anckle = anckle


# class Human:
#     def __init__(self,head, torso):
#         self.head = head
#         self.torso = torso
    
#     def __repr__(self):
#         return f"Human(self.head = {self.head}, self.torso = {self.torso}"



# person_hand = Hand("five", "five")
# person_right_arm = Arm(person_hand, "one", "one")
# person_left_arm = Arm(person_hand, "one", "one")

# person_feet = Feet("five", "one")
# person_right_leg = Leg(person_feet, "one")
# person_left_leg = Leg(person_feet, "one")

# person_torso = Torso(person_right_arm,person_left_arm,person_right_leg,person_left_leg)
# person_head = Head("a", "b", "c", "d")

# person_body = Human(person_head, person_torso)
# print(person_body)
