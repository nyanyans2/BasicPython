a = 61
b = 10

# TODO

if a == 1:
   prime_a = False

else:
        prime_a = True
        for i in range(2,a):
            if a % i == 0:
                prime_a = False
                break
    
if prime_a:
        print("aは素数です")
else:
        print("aは素数ではありません")


if b == 1:
   prime_b= False

else:
        prime_b = True
        for i in range(2,b):
            if b % i == 0:
                prime_b = False
                break
    
if prime_b:
        print("bは素数です")
else:
        print("bは素数ではありません")
    
