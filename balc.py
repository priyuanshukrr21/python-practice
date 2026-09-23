savings = SavingsAccount("Priyanshu", 5000)
current = CurrentAccount("Rahul", 10000)

savings.deposit(2000)
savings.withdraw(3000)

current.withdraw(9500)

savings.show_balance()
current.show_balance()