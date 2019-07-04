from array import *
vals = array('i',[6,4,3,7,5])

newarr = array(vals.typecode,(a*a for a in vals))

for e in newarr:
    print(e)

input()
