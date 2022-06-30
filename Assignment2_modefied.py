# # Assignment 2
# # Write a program to perform Integer Multiplication using Divide and Conquer technique. 
# # Plot the graph showing time taken for running the program for different sizes of input integer numbers. 
# # Compare the curve with the curve of n^2 and n^1.6 and give your comments.

    #  Algorithm intMul(a,b):
    # if a or b has one digit, then:
    #     return a * b.
    # else:
    #     Let n be the number of digits in max{a, b}.
    #     Let aL and aR be left and right halves of a.
    #     Let bL and bR be left and right halves of b.
    #     Let x1 hold Karatsuba(aL, bL).
    #     Let x2 hold Karatsuba(aL + aR, bL + bR).
    #     Let x3 hold Karatsuba(aR, bR).
    #     return x1*10n + (x2 - x1 - x3)*10n/2 + x3.
    # end of if 

import math
import time
import random
import matplotlib.pyplot as plt
MAXSIZE = 2000
STEPS = 100

def integerMultiplication(A, B):
    if len(str(A))==1 or len(str(B))==1:
        return A*B
    else:
        n = max(len(str(A)),len(str(B)))
        nLen = len(str(A))//2
        dConst = 10**nLen
        aL = A // dConst # a left part
        aR = A % dConst # a right part
        nLen = len(str(B))//2
        dConst = 10**nLen
        bL = B // dConst  # b left part
        bR = B % dConst # b right part
        x1 = integerMultiplication(aL, bL)
        x2 = integerMultiplication(aL + aR, bL + bR)
        x3 = integerMultiplication(aR, bR)
        return x1*(10**n) + (x2-x1-x3)*(10**math.ceil(n/2)) + x3

n = []
et = []
n16_x = []
n16_y = []
n159_x = []
n159_y = []
for i in range(0,MAXSIZE+1, STEPS):
    x = random.randint(i, 10**i)
    y = random.randint(i, 10**i)
    start = time.time_ns()
    z = integerMultiplication(x, y)
    end = time.time_ns()
    n.append(len(str(x)))
    executionTime = end - start
    et.append(executionTime/1700)
    n16_x.append(len(str(x)))
    n159_x.append(len(str(x)))
    n16_y.append(i**(1.6)) 
    n159_y.append(i**(1.59)) 

print(n)
print(et)
print(n16_y)
print(n159_y)

plt.plot(n, et, label="Integer Multiplication")
plt.plot(n16_x, n16_y, label="n^1.6")
plt.plot(n159_x, n159_y, label="n^1.59")
plt.xlabel('no. of digits')
plt.ylabel('execution time (ns)')
plt.title('Integer Multiplication')
plt.legend()
plt.show();