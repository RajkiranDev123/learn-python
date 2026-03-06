# p e md as

# arithmetic

x = 10
y = 20

print(x + y)
print(x - y)
print(x * y)
print(x / y)

print(x // y)  # floor division , remove decimal
print(x % y)  # modulo : remainder
print(x**y)  # power


#  comparision : result is boolean : True / False

a = 10
b = 5

print(a == b)
print(a != b)

print(a > b)
print(a < b)

print(a >= b)
print(a <= b)

print("logical ==>")

# logical : combine multiple conditions and perform operation : output is boolean : True/False

age = 20
isStudent = True

print(age > 18 and isStudent)
print(age > 25 or isStudent)
print(not isStudent)

print("more on logical ==.")

m = 10
n = 20
print(m > 5 and n > 10)
print(m < 1 or n == 20)  # atleast one true then true

print(not m == 10)  # single operand , reverse
print(not (m == 10))


# assignment operator : assign values to a variable

#  = , += , -= , *=

c = 10
c = c + 5
c += 5
print(c)


print("identity ==>")

# identity operator : compare objects not value by location : True/False

o1 = [1, 2]
o2 = o1
print(o1 is o2)


print("membership ===>")
# membership operator : whether value exists in sequence data type or not :
# list , string , tuple
# not in , in
# True/False

veg = [1, 2]

print(1 in veg)
print(3 in veg)
print(5 not in veg)

# total operators : 6
"""
arithmetic  : + , - , / , * , // , % , **  : 7
comparision : == , != , >= ,<= , > , < : 6
logical : and , or , not : 3
----------------------------------------------------------------------
assignment : = , += , -+ , *=  : 4
identity : is   : 1
membership : in , not in  : 2

"""
