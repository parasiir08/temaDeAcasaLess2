class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_account_holder_name(self):
        return self._account_holder_name

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate):
        super().__init__(account_number, account_holder_name, balance)
        self._interest_rate = interest_rate

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit):
        super().__init__(account_number, account_holder_name, balance)
        self._overdraft_limit = overdraft_limit

def test_bank_account():
    # Test BankAccount class
    account_number = "123456"
    account_holder_name = "John Doe"
    balance = 5000

    # Create a BankAccount instance
    bank_account = BankAccount(account_number, account_holder_name, balance)

    # Test get_account_number() method
    assert bank_account.get_account_number() == account_number
    # Test get_account_holder_name() method
    assert bank_account.get_account_holder_name() == account_holder_name
    # Test get_balance() method
    assert bank_account.get_balance() == balance

    # Test deposit() method
    bank_account.deposit(500)
    assert bank_account.get_balance() == balance + 500

    # Test withdraw() method
    bank_account.withdraw(200)
    assert bank_account.get_balance() == balance + 500 - 200

    # Test withdraw() with insufficient balance
    bank_account.withdraw(5500)
    assert bank_account.get_balance() == balance  # Balance should remain unchanged

    # Test deposit() with negative amount
    bank_account.deposit(-300)  # This should not change the balance
    assert bank_account.get_balance() == balance - 200


def test_savings_account():
    # Test SavingsAccount class
    account_number = "789012"
    account_holder_name = "Jane Smith"
    balance = 2000
    interest_rate = 0.5

    # Create a SavingsAccount instance
    savings_account = SavingsAccount(account_number, account_holder_name, balance, interest_rate)

    # Test get_balance() method from BankAccount (inherited method)
    assert savings_account.get_balance() == balance

    # Test deposit() method from BankAccount (inherited method)
    savings_account.deposit(1000)
    assert savings_account.get_balance() == balance + 1000

    # Test withdraw() method from BankAccount (inherited method)
    savings_account.withdraw(500)
    assert savings_account.get_balance() == balance + 1000 - 500

def test_current_account():
    # Test CurrentAccount class
    account_number = "345678"
    account_holder_name = "Bob Johnson"
    balance = 3000
    overdraft_limit = 1000

    # Create a CurrentAccount instance
    current_account = CurrentAccount(account_number, account_holder_name, balance, overdraft_limit)

    # Test get_balance() method from BankAccount (inherited method)
    assert current_account.get_balance() == balance

    # Test deposit() method from BankAccount (inherited method)
    current_account.deposit(800)
    assert current_account.get_balance() == balance + 800

    # Test withdraw() method from BankAccount (inherited method)
    current_account.withdraw(2000)
    assert current_account.get_balance() == balance + 800 - 2000

    # Test withdraw() with overdraft limit
    current_account.withdraw(3000)  # This should print "Insufficient balance" and not modify the balance
    assert current_account.get_balance() == balance + 800 - 2000

if __name__ == "__main__":
    test_bank_account()
    test_savings_account()
    test_current_account()
    print("All tests passed successfully!")
