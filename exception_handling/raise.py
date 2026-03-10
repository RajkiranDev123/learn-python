# custom error
def checkPass(password):
    if len(password) < 8:
        raise Exception("Error : password must be >=8 characters")
    print("Password is strong")


try:
    password = "python"
    checkPass(password)
except Exception as e:
    print(e)


# 

try:
    x = -5
    if x < 0:
        raise ValueError("Negative number not allowed")
except ValueError as e:
    print(e)

# ValueError :	correct type but wrong value  :	int("abc")

# TypeError happens when an operation is done on the wrong data type :	"5" + 5

