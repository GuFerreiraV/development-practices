import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):
    
    def test_create_account_zero_balance(self):
        account = BankAccount()
        self.assertEqual(account.balance, 0)
    
    def test_deposit_value(self):
        account = BankAccount()
        account.deposit(300)
        self.assertGreaterEqual(account.balance, 100) # o depósito precisar ter um valor positivo, igual ou maior à 100

    def test_deposit_negative_value(self):
        account = BankAccount()

        with self.assertRaises(ValueError):
            account.deposit(-10)
        
        with self.assertRaises(ValueError):
            account.deposit(0)

    def test_transfer_between_accounts_with_sufficient_funds(self): 
        origin_account = BankAccount()
        destiny_account = BankAccount()

        origin_account.deposit(200)
        origin_account.transfer_value(destiny_account, 150)

        self.assertEqual(origin_account.balance, 50)
        self.assertEqual(destiny_account.balance, 150) 

    # teste para depositar valor ao saldo
    def test_withdraw_value(self):
        account = BankAccount()
        account.deposit(100)
        account.withdraw_money(50)        
        self.assertEqual(account.balance, 50)

    # teste para verificar o saque com valor maior que o saldo
    def test_insufficient_balance(self):
        account = BankAccount()
        account.deposit(50)
        with self.assertRaises(ValueError):
            account.withdraw_money(60)

    def test_transfer_to_a_fraudulent_account(self):
        origin_account = BankAccount()
        destiny_account = BankAccount(is_fraudulent=True)

        origin_account.deposit(100)
        with self.assertRaises(ValueError):
            origin_account.transfer_value(destiny_account, 50)

if __name__ == "__main__": 
    unittest.main()