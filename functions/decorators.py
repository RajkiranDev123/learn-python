

# enhance function without modifying original function

def dec(func):
    def wrapper():
        print(1)
        func()
        print(2)
    return wrapper

@dec
def hel():
    print(66666)

hel()