# if else

# age = int(input("enter your age = "))

age = 9

if age >= 18:
    print("eligible")
else:
    print("not eligible")


print("if elif else ==>")
print(101 < 101)  # False
# if elif else :when there are more than two condition to check

age1 = 100

if age1 >= 18 and age1 < 101:  # all True then True
    print("yes, you can vote")
elif age1 >= 101:
    print("greater than or equal to 101")
elif age1 <= 0:
    print("invalid : cant be 0 or negative")
else:
    print("must be greater than or equal to 18")
