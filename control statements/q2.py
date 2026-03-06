

# which no to skip on user input

start=int(input("enter start = "))
stop=int(input("enter stop = "))

skip=int(input("enter no you want to skip = "))

for i in range(start,stop):
    if i ==skip:
        continue
    print(i)


# enter start = 1
# enter stop = 11
# enter no you want to skip = 5
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

