import math
from math import sqrt
a = int(input('Enter the number:'))
for i in range(2, 1 + int(sqrt(a))):
    if a % i == 0:
        print(a,'is not prime because',
              i,'x',a//i,'=',a)
        break
else:
    print(a,'is prime')
