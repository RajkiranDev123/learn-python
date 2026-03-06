print("methods ===>")

s1 = "SRK"

print(s1.lower())

s2 = "ser".upper()

print(s2)

# inp=input(" name = ").lower()


print(" capitalize ,  and swapcase() ==>")

str = "aaaaa bbb"
print(str.capitalize())  # Aaaaa bbb

print(str.title())  # Aaaaa Bbb

str2 = "Ab"
print(str2.swapcase())  # aB


print("find() ==>")

h = "python"

print(h.find("y"))  # first occurence of substring , gives index


print("replace() ==>")

h2 = "python is"
print(h2.replace("python", "java"))

print("split() and join() ==>")

v = "a,b,c"

vo = v.split(",")  # ['a', 'b', 'c']
print(vo)
no = "-".join(vo)

print(no)


print("checking methods==========>")


g="python"

print(g.startswith("P")) # False
print(g.startswith("p"))

print(g.endswith("n"))

print(g.isalpha()) # check all are alphabets

print(g.isdigit())

print(g.isalnum())




