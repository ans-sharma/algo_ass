# # Assignment 2
# # Write a program to perform Integer Multiplication using Divide and Conquer technique. 
# # Plot the graph showing time taken for running the program for different sizes of input integer numbers. 
# # Compare the curve with the curve of n^2 and n^1.6 and give your comments.


# Algorithm DC_CLEVER_MULTIPLICATION(A, B)
# // Description : Perform multiplication of large numbers using divide and conquer strategy.
# // Input : Number A and B, where A = an-1…a1a0, and B = bn-1...b1b0
# // Output : Multiplication of A and B as C, i.e. C = A * B

# if |a| == 1 or |b| == 1 then
#   return A * B
# else
#   n ← max(|A|, |B|)	
#   c2 ← DC_ CLEVER_MULTIPLICATION(a1, b1)
#   c0 ← DC_ CLEVER_MULTIPLICATION(a0, b0)
#   x ← DC_ CLEVER_MULTIPLICATION(a1 + a0, b1 + b0)
#   return c2*10n + (x – c2 – c0) * 10n/2 + c0
# end


    #  Algorithm Karatsuba(a,b):
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

def integerMultiplication(A, B):
    if len(str(A))==1 or len(str(B))==1:
        return A*B
    else:
        if len(str(A)) > len(str(B)):
            pass
        # if len(str(A))%2 != 0:
        #     pass
        # if len(str(B))%2 != 0:
        #     pass
        n = max(len(str(A)),len(str(B)))
        nLen = len(str(A))//2
        dConst = 10**nLen
        # dConst = 10**nLen
        a0 = A // dConst # a left part
        a1 = A % dConst # a right part
        nLen = len(str(B))//2
        dConst = 10**nLen
        # dConst = 10**nLen
        b0 = B // dConst  # b left part
        b1 = B % dConst # b right part
        x1 = integerMultiplication(a0, b0)
        x2 = integerMultiplication(a0 + a1, b0 + b1)
        x3 = integerMultiplication(a1, b1)
        # return x1*(10**n) + (x2-x1-x3)*(10**(n/2)) + x3
        return x1*(2**n) + (x2-x1-x3)*(2**(n/2)) + x3

print(integerMultiplication(10, 10))
print(int(0b10))
print(int(0b10))
