class bank:
    def __init__(self,name:str,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,add):
        self.balance+=add
    def withdraw(self,vivod):
        if self.balance < vivod:
            print("Not enough money in balance")
        else:
            self.balance-=vivod
            print(self.name,'on your account left',self.balance)
# x=bank('Dauren',500)
# x.deposit(500)
# x.withdraw(200)
