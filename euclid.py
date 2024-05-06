a = 10
b = 20

# TODO

def yuguri(a, b):
    if b == 0:
        return a
    return yuguri(b, a % b)

gozyohou = yuguri(a, b)
print("最大公約数:", gozyohou)

a=14
b=91
def yuguri(a, b):
    if b == 0:
        return a
    return yuguri(b, a % b)

gozyohou = yuguri(a, b)
print("最大公約数:", gozyohou)

a=91
b=14
def yuguri(a, b):
    if b == 0:
        return a
    return yuguri(b, a % b)

gozyohou = yuguri(a, b)
print("最大公約数:", gozyohou)