# resusability
# modularity
# scoping


# positional arguments


def f1(name, city):
    print(name, city)


f1(1, 2)


# default arguments and keyworded arguments , return statement


def f2(name="r", city="c"):
    print(f"{name} and {city}")

    return 66


v = f2(city="c", name="n")
print(v)


# local and global variables

def msg():
    # local
    b=4
    print(b)
    print(ch)

ch=99

msg()