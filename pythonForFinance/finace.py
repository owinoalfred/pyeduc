#this is teaching how to import functions

import math as m

prices  = 64
finals = m.acos(prices)
try:
    print(finals)
except ValueError:
    print("this is not in the math domain")
