import math
import time
import random
import matplotlib.pyplot as plt
from numpy import append
MAXSIZE = 10000
STEPS = 500

def multiply(x, y):

    # Convert x into it's binary form
    xb = bin(x)
    xb = xb[2:] # Omit the prefix 0b

    # Convert y into it's binary form
    yb = bin(y)
    yb = yb[2:] # Eliminate the prefix 0b

    len_y = len(yb)
    len_x = len(xb)

    if x > y :
        n = len(xb)
        while(len_y < len_x):
            yb = '0' + yb
            len_y = len_y + 1
    
    else:
        n = len(yb)
        while(len_x < len_y):
            xb = '0' + xb
            len_x = len_x + 1
    
    # Base Condition 
    if n == 1:
        return x * y
   
    len_xL = len_x//2
    len_yL = len_y//2

    xL = xb[:len_xL] # Extracting the left most significant digits
    xR = xb[len_xL:] # Extracting the right most significant digits
    yL = yb[:len_yL] # Extracting the left most significant digits
    yR = yb[len_yL:] # Extracting the right most significant digits

    # Multiply xL and yL
    mul = int(xL,2) * int(yL,2)
    P1 = bin(mul)
    P1 = P1[2:]

    # Multiply xR and yR
    mul = int(xR,2) * int(yR,2)
    P2 = bin(mul)
    P2 = P2[2:]

    # Multiply xL+xR and yL+yR
    add1 = int(xL,2) + int(xR,2)
    add2 = int(yL,2) + int(yR,2)
    mul = add1 * add2
    P3 = bin(mul)
    P3 = P3[2:]

    mul = int(P1,2) * 2**(2*math.ceil(n/2)) + (int(P3,2) - int(P1,2) - int(P2,2)) * 2**(math.ceil(n/2)) + int(P2,2)
    return mul


n = []
et = []
n2_x = []
n2_y = []
n16_x = []
n16_y = []
for i in range(0,MAXSIZE+1, STEPS):
    x = random.randint(i, 10**i)
    y = random.randint(i, 10**i)
    start = time.time_ns()
    z = multiply(x, y)
    end = time.time_ns()
    n.append(len(str(x)))
    executionTime = end - start
    et.append(executionTime)
    # print("x, y, executionTime", x, y, executionTime)
    n2_x.append(len(str(x)))
    n2_y.append((i*i)/10)
    n16_x.append(len(str(x)))
    n16_y.append(i**(1.6))
print(n)
print(et)
print(n2_y)
print(n16_y)

plt.plot(n, et, label="mul")
plt.plot(n2_x, n2_y, label="n^2")
plt.plot(n16_x, n16_y, label="n^1.6")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('integer multiplication')
plt.legend()
plt.show();