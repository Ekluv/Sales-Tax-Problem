from lib.product import Product
from lib.bill import Bill

try:
    lines = [line.strip() for line in open('input/tax_input1.txt')]
except FileNotFoundError as e:
    print('File Not Found', e)

def init():
    products = []
    for line in lines:
        if line:
            line = line.split(' ')
            quantity = line[0]
            is_imported = False
            if 'imported' in line:
                is_imported = True
                line.remove('imported')
            item = ' '.join(line[1:-2])
            price = line.pop()
            product = Product(quantity=quantity, price=price, item=item, is_imported=is_imported)
            print(product)
            products.append(product)
    bill = Bill(products)
    bill.print_bill()

if __name__ == '__main__':
    init()
