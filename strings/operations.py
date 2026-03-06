# count total characters
a = "str"
print(len(a))  # 3

b = "st r"
print(len(b))  # 4 , space is counted too

password = "hhhhhhh"

if len(password) > 5:
    print("done")
else:
    print("not done")


print("slicing ==========>")
# slicing : access multiple characters
# text[start,stop,step]
# range(start,stop,step)

t="python is"
  #012345678
print(t[0:2+1:1]) # pyt

t1="python is"
   #012345678
print(t1[::]) # python is

t2="python is"
   #012345678
print(t2[::1]) # python is

t3="python is"
   #012345678
print(t3[::-1]) # si nohtyp


print("repeat strings =========>")

s="h-"
print(5*s)

s2="3"
print(5*s2)

print("concatenation ==>")

# print(9+"tt")  TypeError

print("uuu"+"ppp")


print("membership ==>")

cc="python is"

print("is" in cc) # True

print("si" in cc) # False

print("si" not in cc) # True

print("on" in cc) # True


print("e.g.1 ===>")





