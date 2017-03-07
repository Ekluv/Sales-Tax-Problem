import math

class Product(object):
    FOOD_ITEMS = ['chocolate bar', 'box of chocolates', 'chocolates']
    MEDICAL_ITEMS = ['headache pills']
    FOOD = 'food'
    BOOK = 'book'
    MEDICAL = 'medical'
    OTHERS = 'others'
    NORMAL_TAX = 10
    IMPORT_TAX = 5
    ciel = 1/ 0.05

    def __init__(self, quantity, price, item, is_imported=False):
        self._quantity = int(quantity)
        self._price = float(price)
        self._item = item
        self._is_imported = is_imported

    @property
    def is_imported(self):
        return self._is_imported

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = int(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = float(value)

    def get_type(self):
        if self._item in Product.FOOD_ITEMS:
            return Product.FOOD
        elif self._item == Product.BOOK:
            return Product.BOOK
        elif self._item in Product.MEDICAL_ITEMS:
            return Product.MEDICAL
        return Product.OTHERS

    def get_sales_tax(self, Total=False):
        _type = self.get_type()
        tax = 0
        if _type == Product.OTHERS:
            tax = (self._price * Product.NORMAL_TAX) / 100
        if self._is_imported:
            tax += (self._price * Product.IMPORT_TAX) / 100
        tax = math.ceil(tax * self.ciel) / self.ciel
        return tax * self.quantity if Total else tax

    def get_total_price(self):
        amt = (self._price + self.get_sales_tax()) * self.quantity
        return amt

    def __str__(self):
        return '{0} {1} : {2}'.format(self._quantity, self._item, self._price)
