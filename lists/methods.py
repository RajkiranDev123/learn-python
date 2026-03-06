# copy

a = [1, 2]
b = a.copy()  # changes on b wont impact a

b[0] = 2

print(a, b)

print("welcome to more methods on lists ===>")

a1 = [1]
a1.append(99)
print(a1)

# extend

a2 = [6]
a3 = [5]
a2.extend(a3)
print(a2)

# insert : at position

a4 = [8, 9]
a4.insert(0, "hi")
print(a4)  # ['hi', 8, 9]

# remove element : remove(element)

a4.remove("hi")
print(a4)


# remove with position : pop
a4.pop(1)
print(a4)


# clear : []

d = [7, 8]
d.clear()
print(d)

# know index of element

d1 = [7, 8]
print(d1.index(7))  # 0


# count
e=[7,8,9,8]
counter=e.count(8)
print(counter)

# sort

f=[5,4,3]

f.sort()
print(f)

# reverse

k=[1,2,3]
k.reverse()

print(k)



