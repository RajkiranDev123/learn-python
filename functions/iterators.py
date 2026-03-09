

# handle data step by step without loading data into memory at once

l=[1,2]

it=iter(l)

try:
    while True:
        print(next(it))
except StopIteration:
    print("stop")