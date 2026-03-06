"""
numeric type :

    int : whole numbers : 2  50 -20

    float : decimal numbers : 1.25

    complex : real and imaginary part

    a+5j

"""

a = 10
b = 10.20
c = 9 + 7j

print(a, b, c)
print(type(a))

"""
boolean type : for logical operations

True/false

"""

a1 = True
print(a1)

# None : absence of a value

a3 = None  # in future value will come
a3 = 60
print(a3)


# sequence type : list , string , tuple : ordered + index based , orderly stored
# set and dict are not sequence type : no ordered and no index and are hash-based collection. 


l1 = [1, 2]  # list

s1 = "raj"  # string

t1 = (1, 8)  # tuple : immutable  , parenthesis : ()

print(l1, s1, t1)

# set : mutable , {} , unique elements

# types : set : mutable and frozenset : immutable

unique = set([1, 1, 2, 2])  # pass array through set to get unique elements
print(unique)  # {1, 2}

set1 = {8, 9, 7, 6, 8}
print(set1)

ims = frozenset([8, 8, 9])
print(ims)  # frozenset({8, 9})


#####################################################################################################

# mapping data type : dictionary {key:value}

person = {"name": "raj"}


# string and tuple : immutable and rest mutable

# “immutable” means an object cannot be changed after it is created.
# If you try to modify it, Python actually creates a (new object) instead of altering the existing one.

# These built-in types are immutable:

# int – integers

# float – decimal numbers

# bool – True/False

# str – strings

# tuple – ordered collection (like a list but fixed)

# frozenset – immutable version of a set

# bytes
