"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Nabin Niroula
Date:   04/19/2021
"""

import currency
import math

src = input("3-letter code for original currency: ")
dst = input("3-letter code for the new currency: ")
amt = input("Amount of the original currency: ")
val = currency.exchange(src, dst, amt)
val2 = round(val, 3)
# print("You can exchange", amt, src, "for", val, dst,".")
print("You can exchange", amt, src, "for", val2, dst,".")
