import datetime
from pprint import pprint


class Invoice:

    def __init__(self, number, product_name, quantity, piece_price, series='MS'):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.piece_price = piece_price
        self.series = series

    def change_quantity(self, quantity):
        self.quantity = quantity

    def change_price(self, piece_price):
        self.piece_price = piece_price

    def change_product_name(self, product_name):
        self.product_name = product_name

    def generate_invoice(self):
        invoice = [['--------------------------------------------'],
                   ['|', 'Invoice', '|', f'Series: {self.series}', '|', f'Number: {self.number}', '     |'],
                   ['--------------------------------------------'],
                   ['|', f'Date: {datetime.date.today()}', '                        |'],
                   ['--------------------------------------------'],
                   ['|', 'Product', '|', 'Quantity', '|', 'Price/piece', '|', 'Total', '|'],
                   ['--------------------------------------------'],
                   ['|', self.product_name, '|     ', self.quantity, '   |   ', self.piece_price, '    |', self.quantity*self.piece_price, ' |'],
                   ['--------------------------------------------'],
                   ]
        for element in invoice:
            print(*element)
        print()
