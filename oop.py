# def customer():
#     customerList = {
#         "name": "Jame Ben",
#         "address": "56 Avenue",
#         "account": "65473652"
#     }
#     return customerList

customerDetails = {
    "name": "John Ben",
    "address": "56 Avenue",
    "account": 65473652,
    "balance": 1000
}


# Display customer account information
def customerInfo():
    print("CUSTOMER INFO")
    print("#####################################")
    print("Name:", customerDetails.get("name"), "\nAddress:", customerDetails.get("address"), "\nAccount Number:",
          customerDetails.get("account"), "\nAccount Balance:", "$", customerDetails.get("balance"))
    print("#####################################")


# customer deposit
def deposit(deposit):
    new_balance = deposit + customerDetails.get("balance")
    customerDetails.update({"balance": new_balance})
    # customerDetails["balance"] = new_balance
    print("You have deposit", "$", format(deposit), "into Account:", customerDetails.get("account"),
          "\nYour new balance is", "$", customerDetails.get("balance"))


# customer withdraw
def withdraw(withdraw):
    if customerDetails.get("balance") - withdraw < 0:
        print("You have insufficient fund in your account")
    else:
        new_balance = customerDetails.get("balance") - withdraw
        customerDetails.update({"balance": new_balance})
        print("You have withdraw", "$", withdraw, " your new balance is", "$", customerDetails.get("balance"))


if __name__ == "__main__":
    customerInfo()  # Display customer information
    # deposit(2000)  # Customer deposit $1000
    # withdraw(700)  # Customer withdraw $700
    get_deposit = int(input("Enter the deposit amount: "))
    deposit(get_deposit)
    get_withdraw = int(input("Enter the withdraw amount: "))
    withdraw(get_withdraw)

    print("\n---when a customer deposit or withdraw the balance from the dictionary is updated accordingly---")
    print(customerDetails)  # monitoring account balance when customer deposit/withdraw
