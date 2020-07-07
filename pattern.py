def patt (n):
    while(n==0) :
        return 0


    return (n % 10 + patt(int(n / 10)))




# Driven code to check above
num = 100
result = patt ( num )
print ( "Sum of digits in", num, "is", result )