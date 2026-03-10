# 3 types of error :

# compile time errors : syntax like colon is missing

# runtime : in the middle of execution : try/except

# logical errors : incorrect output

# Syntax Error  → program doesn't run
# Runtime Error → program crashes
# Logical Error → program runs but wrong output


try:
    num1=int(input(" no1 = "))
    num2=int(input(" no2 = "))

    try:
        res=num1/num2
        print(res)
    except ZeroDivisionError:
        print("cant divide by 0")

except ValueError:
    print("invalid input")