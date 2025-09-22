# main.py
import pricing


net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

import pricing as selling_price

net_price = selling_price.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)

# main.py
from pricing import get_net_price

net_price = get_net_price(price=100, tax_rate=0.01)
print(net_price)

from pricing import get_net_price as calculate_net_price

net_price = calculate_net_price(
    price=100,
    tax_rate=0.1,
    discount=0.05
)


from pricing import *
from product import *

tax = get_tax(100)
print(tax)

#-----------------------------------

import sys

for path in sys.path:
    print(path)

#-----------------------------------

from mail import *


send('test@example.com','Hello')