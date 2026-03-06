num1 = float(input("enter no 1 "))
num2 = float(input("enter no 2 "))

choice = input(" enter the choice + * - ")

if choice == "+":
    print(f"added : {num1+num2}")
elif choice == "-":
    print(f"subtracted : {num1-num2}")
elif choice == "*":
    print(f"multiplied : {num1*num2}")
else :
    print("invalid choice")
