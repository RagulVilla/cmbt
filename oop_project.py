from bank_accounts import *

ragul=bankaccount(6000,'Ragul')
ragul.get_balance()
print('')

gokul=bankaccount(10000,"Gokul")

ragul.deposit(500)

gokul.deposit(100)

ragul.withdraw(6400)

gokul.withdraw(10000)

ragul.transfer(100,gokul)

gokul.get_balance()

minnu=intrestrewardacc(200,'Minnu')
minnu.get_balance
minnu.deposit(100)

print('\n')

swetha=savingsacc(100,'swetha')
swetha.get_balance

swetha.withdraw(50)
swetha.transfer(40,minnu)