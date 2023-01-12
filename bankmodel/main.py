from bankmodel.bank_modeling import CustomerSavingsAccounts

customerSavings = CustomerSavingsAccounts()

if __name__ == '__main__':

    while True:
        print("\n")
        print("____________CHOICE__________________")
        print("Enter a to create a new account")
        print("Enter b to access an existing account")
        print("Enter x to exit")
        print("____________________________________\n")

        userInput = input()
        if userInput == "a":
            print("Enter customer name: ")
            inputCustomerName = input()
            print("Enter customer initial deposit: ")
            inputInitialDeposit = int(input())
            customerSavings.createNewAccount(inputCustomerName, inputInitialDeposit)
        elif userInput == "b":
            print("Enter your customer name: ")
            inputCustomerName = input()
            print("Enter your customer account number: ")
            inputCustomerAccount = int(input())
            authenticate = customerSavings.customerAuthentication(inputCustomerName, inputCustomerAccount)
            if authenticate:
                while True:
                    print("Enter a to withdraw")
                    print("Enter b to deposit")
                    print("Enter c to display customer information")
                    print("Enter d to go back to the previous menu")
                    userChoice = input()
                    if userChoice == "a":
                        print("Enter withdrawal Amount")
                        inputWithdraw = int(input())
                        customerSavings.customerWithdraw(inputWithdraw)
                    elif userChoice == "b":
                        print("Enter the customer deposit: ")
                        inputCustomerDeposit = int(input())
                        customerSavings.customerDeposit(inputCustomerDeposit)
                    elif userChoice == "c":
                        customerSavings.customerAccountInfo(inputCustomerAccount)
                    elif userChoice == "d":
                        break
        elif userInput == "x":
            quit()
