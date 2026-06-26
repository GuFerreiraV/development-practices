class BankAccount:
    def __init__(self, is_fraudulent=False):
        self.balance = 0
        self.is_fraudulent = is_fraudulent
    
    def deposit(self, value):
        if value <= 0:
            raise ValueError("Valor de depósito não pode ser negativo e nem 0!")
        self.balance += value
    
    def withdraw_money(self, value): 
        if value > self.balance:
            raise ValueError("Saldo insuficiente!")
        self.balance -= value

    def transfer_value(self, destiny_account, value):
        if destiny_account.is_fraudulent: 
            raise ValueError("Transferência Bloqueada: conta de destino suspeita de fraude.")    
        self.withdraw_money(value)    
        destiny_account.deposit(value)
