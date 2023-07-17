class Wallet:
    @staticmethod
    def _details_calc(my_dict):
        my_list = []
        for key, value in my_dict.items():
            key_as_int = float(key)
            my_sum = value * key_as_int
            my_list.append(f'{value} x {key}lv -> {my_sum}lv (total)')

        return my_list

    @staticmethod
    def _sum_calc_value_single(my_dict):
        total = 0
        for key, value in my_dict.items():
            key_as_int = float(key)
            total += value * key_as_int

        return total

    @staticmethod
    def _sum_calc_value_both(banknotes, coins):
        total = Wallet._sum_calc_value_single(banknotes) + Wallet._sum_calc_value_single(coins)
        return total

    @staticmethod
    def _sum_calc_qty(my_dict):
        total = 0
        for key, value in my_dict.items():
            total += my_dict[key]

        return total

    def __init__(self, color, max_qty_coins, max_qty_bankotes):
        self.color = color
        self.max_qty_coins = max_qty_coins
        self.max_qty_banknotes = max_qty_bankotes
        self.banknotes = {'5': 0, '10': 0, '20': 0, '50': 0, '100': 0}
        self.coins = {'2': 0, '1': 0, '0.50': 0, '0.20': 0, '0.10': 0, '0.05': 0, '0.02': 0, '0.01': 0}

    def add_money(self, type, value, qty):
        if type == 'banknote':
            if Wallet._sum_calc_qty(self.banknotes) + qty <= self.max_qty_banknotes:
                self.banknotes[value] += qty
                print('Banknotes added successfully!')
            else:
                print('You do not have enough space in your wallet!')
        elif type == 'coin':
            if Wallet._sum_calc_qty(self.coins) + qty <= self.max_qty_coins:
                self.coins[value] += qty
                print('Coins added successfully!')
            else:
                print('You do not have enough space in your wallet!')

    def take_money(self, type, value, qty):
        if type == 'banknote':
            if self.banknotes[value] - qty >= 0:
                self.banknotes[value] -= qty
                print('Banknotes removed successfully!')
            else:
                print('You do not have enough such banknotes in your wallet!')
        elif type == 'coin':
            if self.coins[value] - qty >= 0:
                self.coins[value] -= qty
                print('Banknotes removed successfully!')
            else:
                print('You do not have enough such coins in your wallet!')

    def money_details(self, type):
        if type == 'all' or type == 'banknotes':
            banknotes_list = Wallet._details_calc(self.banknotes)
            print(banknotes_list)
        if type == 'all' or type == 'coins':
            coins_list = Wallet._details_calc(self.coins)
            print(coins_list)

    def __repr__(self):
        total = Wallet._sum_calc_value_both(self.banknotes, self.coins)
        return f'This wallet is {self.color} and contains {total}lv.'


my_wallet = Wallet('black', 50, 50)
my_wallet.add_money('coin', '0.50', 4)
my_wallet.add_money('coin', '0.02', 7)
my_wallet.add_money('banknote', '50', 1)
my_wallet.add_money('banknote', '20', 3)
my_wallet.add_money('banknote', '5', 3)
my_wallet.take_money('coin', '0.50', 10)
my_wallet.take_money('banknote', '20', 1)
my_wallet.add_money('banknote', '100', 80)
my_wallet.money_details('all')
print(my_wallet.__repr__())

your_wallet = Wallet('brown', 80, 40)
your_wallet.add_money('coin', '0.01', 6)
your_wallet.add_money('coin', '0.02', 2)
your_wallet.add_money('coin', '0.05', 4)
your_wallet.add_money('coin', '0.10', 5)
your_wallet.add_money('coin', '0.20', 4)
your_wallet.add_money('coin', '0.50', 2)
your_wallet.add_money('coin', '1', 7)
your_wallet.add_money('coin', '2', 2)
your_wallet.money_details('coins')
your_wallet.take_money('coin', '0.01', 2)
your_wallet.take_money('coin', '0.02', 3)
your_wallet.take_money('coin', '1', 7)
your_wallet.add_money('banknote', '5', 2)
your_wallet.add_money('banknote', '5', 1)
your_wallet.add_money('banknote', '10', 10)
your_wallet.add_money('banknote', '20', 15)
your_wallet.add_money('banknote', '50', 11)
your_wallet.add_money('banknote', '100', 1)
your_wallet.money_details('banknotes')
