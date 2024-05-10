a = 61
b = 10

# TODO

prime_a = True

for i in range(2,a):
    if a % i == 0:
        prime_a = False
        break
    
if prime_a:
        print("aは素数です")
else:
        print("aは素数ではありません")

prime_b = True

for i in range(2,b):
    if b % i == 0:
        prime_b = False
        break
    
if prime_b:
        print("bは素数です")
else:
        print("bは素数ではありません")
    
