# ordered
# mutable
# dynamic

# add ==> key-value : 1  pair

a = {5: [8, 9], "name": "raj"}
a[6] = 20
print(a)

# update

a["name"] = "yog"
print(a)

# delete

del a[6]
print(a)


# methods

print("methods ==>")

# get

p = {"id": 1, "name": "raj", "roll": 20}
n=p.get("idm","not found")
print(n)

# keys

v=p.keys()

print(v)
print(list(v))
print(list(p.values()))


# items

print(list(p.items())) # [('id', 1), ('name', 'raj'), ('roll', 20)]


# pop

popped=p.pop("roll","not found")
print(popped)
print(p)

# 
