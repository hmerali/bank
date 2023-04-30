class Bank:
    def __init__(self):
        self.accounts = {}
        self.usernames = {}
        self.admin = {"admin": "adminpass"}
        self.logged_in = False
        self.current_user = None
    
    def create_account(self, name, pin):
        account_num = len(self.accounts) + 1
        self.accounts[account_num-1] = {"name": name, "balance": 0, "pin": pin}
        self.usernames[name] = account_num
        print("Account created successfully!")
        print("Account number:", account_num)
    
    def close_account(self, account_num):
        if account_num in self.accounts:
            del self.usernames[self.accounts[account_num]["name"]]
            del self.accounts[account_num]
            print("Account closed successfully!")
        else:
            print("Account not found.")
    
    def modify_account(self, account_num, name=None, pin=None):
        if account_num in self.accounts:
            if name is not None:
                self.accounts[account_num]["name"] = name
                self.usernames[name] = account_num
            if pin is not None:
                self.accounts[account_num]["pin"] = pin
            print("Account modified successfully!")
        else:
            print("Account not found.")
    
    def login(self, username, pin):
        accountNum = self.usernames[username]
        if accountNum <= len(self.accounts):
            if self.accounts[accountNum-1]["pin"] == pin:
                self.logged_in = True
                self.current_user = accountNum-1
                print("Login successful!")
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")
    
    def logout(self):
        self.logged_in = False
        self.current_user = None
        print("Logout successful!")
    
    def check_balance(self):
        if self.logged_in:
            print("Balance:", self.accounts[self.current_user]["balance"])
        else:
            print("Please login first.")
    
    def deposit(self, amount):
        if self.logged_in:
            self.accounts[self.current_user]["balance"] += amount
            print("Deposit successful!")
            print("Balance:", self.accounts[self.current_user]["balance"])
        else:
            print("Please login first.")
    
    def withdraw(self, amount):
        if self.logged_in:
            if self.accounts[self.current_user]["balance"] >= amount:
                self.accounts[self.current_user]["balance"] -= amount
                print("Withdrawal successful!")
                print("Balance:", self.accounts[self.current_user]["balance"])
            else:
                print("Insufficient funds.")
        else:
            print("Please login first.")
    
    def admin_login(self, username, password):
        if username in self.admin:
            if self.admin[username] == password:
                self.logged_in = True
                print("Admin login successful!")
            else:
                print("Incorrect password.")
        else:
            print("Admin not found.")
    
    def admin_logout(self):
        self.logged_in = False
        print("Admin logout successful!")
    
    def list_accounts(self):
        if self.logged_in:
            for account_num, account_info in self.accounts.items():
                print("Account number:", account_num)
                print("Account name:", account_info["name"])
                print("Account balance:", account_info["balance"])
                print()
        else:
            print("Please login first.")

def main():
    bank = Bank()

    while True:
        print("Welcome to the online banking system!")
        print("1. Login")
        print("2. Create account")
        print("3. Close account")
        print("4. Modify account")
        print("5. Admin login")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")
        print()

        if choice == "1":
            username = input("Enter your account Name: ")
            pin = input("Enter your PIN: ")
            bank.login(username, pin)
            if bank.logged_in:
                print("Login successful!")
        elif choice == "2":
            name = input("Enter your name: ")
            pin = input("Enter your PIN: ")
            bank.create_account(name, pin)
        elif choice == "3":
            account_num = input("Enter the account number to close: ")
            bank.close_account(int(account_num))
        elif choice == "4":
            account_num = input("Enter the account number to modify: ")
            name = input("Enter your new name (leave blank to keep the same): ")
            pin = input("Enter your new PIN (leave blank to keep the same): ")
            bank.modify_account(int(account_num), name, pin)
        elif choice == "5":
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            bank.admin_login(username, password)
            if bank.logged_in:
                print("Admin login successful!")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            print()

        if bank.logged_in:
            while True:
                print("1. Check balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                choice = input("Enter your choice (1-4): ")
                print()

                if choice == "1":
                    bank.check_balance()
                elif choice == "2":
                    amount = float(input("Enter the amount to deposit: "))
                    bank.deposit(amount)
                elif choice == "3":
                    amount = float(input("Enter the amount to withdraw: "))
                    bank.withdraw(amount)
                elif choice == "4":
                    bank.logout()
                    break
                else:
                    print("Invalid choice. Please try again.")
                    print()

        if bank.logged_in and username == "admin":
            while True:
                print("1. List accounts")
                print("2. Logout")

                choice = input("Enter your choice (1-2): ")
                print()

                if choice == "1":
                    bank.list_accounts()
                elif choice == "2":
                    bank.admin_logout()
                    break
                else:
                    print("Invalid choice. Please try again.")
                    print()

if __name__ == '__main__':
    main()
