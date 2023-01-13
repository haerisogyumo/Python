class Account:

    def __init__(self, bank, id, name, balance):
        self.__bank = bank
        self.__id  = id
        self.__name = name
        self.__balance = balance


    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        self.__balance -= money

    def show(self):
        print('은행명 :', self.__bank)
        print('계좌번호 :', self.__id)
        print('입금주 :', self.__name)
        print('현재잔액 :', self.__balance)