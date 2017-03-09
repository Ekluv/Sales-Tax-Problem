from .product import Product

class Bill(object):

    def __init__(self, products):
        if isinstance(products, list) and all(isinstance(obj, Product) for obj in products):
            self._products = products
        else:
            raise ValueError('products must be instance of %s' % Product.__name__)

    @property
    def products(self):
        self._products

    def add_product(self, product):
        if isinstance(product, Product):
            self._products.append(product)
        else:
            raise ValueError('product must be instance of %s' % Product.__name__')

    def remove_product(self, product):
        self._products.remove(product)

    def get_total_tax(self):
        tax = 0
        for product in self._products:
            tax += product.get_sales_tax(Total=True)
        return tax

    def get_bill_price(self):
        price = 0
        for product in self._products:
            price += product.get_total_price()
        return price

    def print_bill(self):
        for product in self._products:
            print(product)
        print('Sales Taxes %s' % self.get_total_tax())
        print('Total %s' % self.get_bill_price())
