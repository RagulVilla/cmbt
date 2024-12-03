class balanceexception(Exception):
    pass
class bankaccount:
    def __init__(self,initial_amount,acc_name):
        self.balance=initial_amount
        self.name=acc_name
        print(f'Account {self.name} Created\nBalance:{self.balance:.2f}')
    def get_balance(self):
        print(f'\nAccount {self.name} Balance = ${self.balance:.2f}')
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f'\nAccount {self.name} Deposit Complete')
        self.get_balance()
    
    def viable_transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise balanceexception(f'\nSorry, Account {self.name} only has ${self.balance:.2f}.')
    
    
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            print(f'\nAccount {self.name} Withdrawel Complete')
            self.get_balance()
        except balanceexception as error:
            print(f'\nWithdraw interrupted:{error}') 
    
    def transfer(self,amount,account):
        try:
            print(f'\n*********\nBegining Transfer...!')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f'\nTranscation Complete...!!!\n***********')
        except balanceexception as error:
            print(f'\n********\nTransfer Interrupted.{error}')
            
class intrestrewardacc(bankaccount):
    def deposit(self,amount):
        self.balance=self.balance+(amount*1.05)
        print('\nDeposit complete.')
        self.get_balance()
    
class savingsacc(intrestrewardacc):
    def __init__(self,initial_amount,acc_name):
        super().__init__(initial_amount,acc_name)
        self.fee=5
        
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print('\nWithdraw completed.')
            self.get_balance()
        except BaseException as error:
            print(f'Withdraw interrupted:{error}')