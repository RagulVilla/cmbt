# # class vehicle:
# #     def __init__(self,make,model):
# #         self.make=make
# #         self.model=model
        
# #     def moves(self):
# #         print('move along..')
        
# #     def get_make_model(self):
# #         print(f'I\'m a {self.make} {self.model}')
        
# # mycar=vehicle('tesla','model S')
# # mycar.moves()
# # print(mycar.make)
# # print(mycar.model)
# # mycar.get_make_model()

# # yourcar=vehicle('tata','punch')

# # yourcar.moves()
# # yourcar.get_make_model()
# # print(yourcar.make)


# # class vehicle:
# #     def __init__(self,make,model,types):
# #         self.make=make
# #         self.model=model
# #         self.types=types

# #     def moves(self):
# #         print('move along..')
        
# #     def get_make_model(self):
# #         print(f'I\'m a {self.make} {self.model}')
        
# #     def abc(self):
# #         print(f'Im the {self.types}')

# # mycar=vehicle('tesla','model s','foreign')
        
# # print(mycar.types)
# # mycar.abc()


# class bike:
    
#     def __init__(self,tyre,name):
#         self.tyre=tyre
#         self.name=name
    
#     def details(self):
#         print(f'i am having {self.tyre} tyre and im from {self.name}')
    
#     def moves(self):
#         print('I MOVE FAST')
        
        
# mybike=bike('ceat','royal enfield ')

# mybike.moves()
# mybike.details()

# yourbike=bike('michelin','yahama')

# print(yourbike.name)
# print(yourbike.tyre)

# yourbike.details()

class students:
    
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std=std
        
    def ages(self):
        print(f'{self.name}\'s age is {self.age}')
        
ragul=students('ragul','22','12')

print(ragul.age)
print(ragul.std)

ragul.ages()
print('')

gokul=students('gokul','28','college final year')

print(gokul.age)
print(gokul.std)

gokul.ages()