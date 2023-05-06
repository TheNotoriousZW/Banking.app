while True:
    class Bank:

        def __init__(self):
            global balance
            global transfers
            self.transfers = [0]
            self.balance = sum(self.transfers)
            balance = self.balance
            transfers = self.transfers

        def withdraw(self, amount):
            global balance
            while amount <= 0:
                try:
                    amount = int(input("How much would you like to withdraw today: "))
                except Exception:
                    print("invalid Entry")
                if self.balance - amount > -100:
                    self.balance = self.balance - amount
                    self.transfers.append(- amount)
                    balance = self.balance
                    print(f"You have withdrawn {amount}")
                    print(f"You have a remaining balance of {self.balance}")

                else:
                    print("Insufficient Funds")

        def deposit(self, amount):
            while amount <= 0:
                try:
                    amount = int(input('Enter amount you would like to deposit: '))
                except Exception:
                    print("Invalid input")
            self.transfers.append(amount)
            self.balance = sum(self.transfers)
            balance = self.balance
            return balance


    class Account(Bank):
        def __init__(self, firstname, lastname, password):
            self.firstname = firstname
            self.lastname = lastname
            self.transfers = [0]
            self.balance = sum(self.transfers)
            self.password = password

        def Check(self):
            transfers = self.transfers
            print(f"Here are your latest transactions - ")
            for elem in transfers:
                print(elem)

        def account(self):
            print(f"Welcome {self.firstname} You have a remaining balance of {self.balance}")


    user = Account('Zaphon', 'Wray', 'Z123')
    user.firstname = user.firstname.lower()
    passw = user.password

    while True:

        ask = input("Withdraw or deposit:  (w, d or c) for transaction history: ")
        ask = ask.lower()
        amount = 0

        if ask == 'd':
            password = input("Enter password here: ")
            if passw == password:
                user.account()
                user.deposit(amount)


            else:
                print('Incorrect password or Name not in our system')

        if ask == 'w':
            password = input("Enter password here: ")
            if passw == password:
                user.account()
                user.withdraw(amount)
                print(user.transfers)

        if ask == 'c':
            password = input("Enter password here: ")
            if passw == password:
                user.account()
                user.Check()
































