# ordered
# mutable
# dynamic
# heterogeneous


#  4 ways of creating

# square brackets

lis = [1, 2, True, "raj", 3.2]

# list constructor

lis2 = list((1, 2, True, "raj", 3.2))

# list comprehension and range()

ran = list(range(1, 11, 1))

print(ran)

# list comprehension

sq = []

for i in range(1, 12):
    sq.append(i)
print(sq)

#
w = [i * 1 for i in range(1, 6) if i % 2 == 0]
print(w)
