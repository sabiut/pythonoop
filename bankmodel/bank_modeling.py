from abc import ABCMeta, abstractmethod, ABC
from random import randint


# abstract class(blueprint)
class CustomerAccount(ABC):
    @abstractmethod
    def createNewAccount(self, customer_name, initial_deposit):
        return 0

    @abstractmethod
    def customerAuthentication(self, customer_name, account_number):
        return 0

    @abstractmethod
    def customerDeposit(self, deposit_amount):
        return 0

    @abstractmethod
    def customerWithdraw(self, withdraw_amount):
        return 0

    @abstractmethod
    def customerAccountInfo(self, customer_account):
        return 0


# class that implements the abstract class
class CustomerSavingsAccounts(CustomerAccount):

    def __init__(self):
        self.account_number = None
        self.customerSavingsAccounts = {12144: ["ken", 400]}

    def createNewAccount(self, customer_name, initial_deposit):
        self.account_number = randint(10000, 99999)
        self.customerSavingsAccounts[self.account_number] = [customer_name, initial_deposit]
        print("The customer account number {} has been created successfully".format(self.account_number))

    def customerDeposit(self, deposit_amount):
        self.customerSavingsAccounts[self.account_number][1] += deposit_amount
        print("You have deposited ${}".format(deposit_amount))
        print("Your new account balance is ${}".format(self.customerSavingsAccounts.get(self.account_number)[1]))

    def customerWithdraw(self, withdraw_amount):
        if withdraw_amount > self.customerSavingsAccounts[self.account_number][1]:
            print("sorry You have Insufficient balance")
        else:
            self.customerSavingsAccounts[self.account_number][1] -= withdraw_amount
            print("Your account has been debited with ${}".format(withdraw_amount))
            print("Your available balance is ${}".format(self.customerSavingsAccounts.get(self.account_number)[1]))

    def customerAccountInfo(self, customer_account_num):
        if customer_account_num in self.customerSavingsAccounts.keys():
            print("-----------Account Details-----------")
            print("Customer Name: {}".format(self.customerSavingsAccounts[customer_account_num][0]))
            print("Account Number: {}".format(customer_account_num))
            print("Current Balance: ${}".format(self.customerSavingsAccounts[customer_account_num][1]))
            print("-----------Account Details-----------\n")
        else:
            print("Account number does not exist")

    def customerAuthentication(self, customer_name, account_number):
        if account_number in self.customerSavingsAccounts.keys():
            if self.customerSavingsAccounts[account_number][0] == customer_name:
                print("successfully authenticated\n")
                self.account_number = account_number
                return True
            else:
                print("Fail to authenticate\n")
                return False
        else:
            print("Fail to authenticate\n")
            return False
