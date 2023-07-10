class Wallet:
    def __init__(self, color, max_qty):
        self.color = color
        self.max_qty = max_qty
        self.banknotes = {'5': 0, '10': 0, '20': 0, '50': 0, '100': 0}
        self.coins = {'2': 0, '1': 0, '0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0, '0.02': 0, '0.01': 0}

    def add_money(self, type, value, qty):
        if type == 'banknote':
            self.banknotes[value] += qty
        elif type == 'coin':
            self.coins[value] += qty
