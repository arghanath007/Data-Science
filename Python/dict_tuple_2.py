def add_and_multiply(a, b):
    return {a + b, a * b}


a = int(input("Enter a: "))
b=int(input("Enter b: "))


add_multiply=add_and_multiply(a, b)
print(add_multiply)

