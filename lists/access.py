lis = [9, 8, 7, 6, 5]

print(lis[0])

# update element : mutable

lis[0] = 55

print(lis)  # [55, 8, 7, 6, 5]
# ..............0  1  2  3  4

# multiple elements access

print(lis[0 : 2 + 1 : 1])  # [55, 8, 7]


# update multiple
lis[0:2:1] = 4, 7, 1, 1
print(lis)  # [4, 7, 1, 1, 7, 6, 5]
