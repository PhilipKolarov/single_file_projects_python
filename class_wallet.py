class Wallet:
    @staticmethod
    def _details_calc(my_dict):
        my_list = []
        for key, value in my_dict.items():
            key_as_int = float(key)
            my_sum = value * key_as_int
            my_list += f'{value} x {key}lv -> {my_sum}lv (total)'

        return my_list
    
    @staticmethod
    def _sum_calc_single(my_dict):
        total = 0
        for key, value in my_dict.items():
            key_as_int = float(key)
            total += value * key_as_int
        
        return total
        
    @staticmethod
    def _sum_calc_both(banknotes, coins):
        total = Wallet._sum_calc_single(banknotes) + Wallet._sum_calc_single(coins)
        return total

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

    def money_details(self, type):
        if type == '' or type == 'banknotes':
            Wallet._details_calc(self.banknotes)
        if type == '' or type == 'coins':
            Wallet._details_calc(self.coins)

    def __repr__(self):
        total = Wallet._sum_calc_both(self.banknotes, self.coins)
        return f'This wallet is {self.color} and contains {total}lv.'
