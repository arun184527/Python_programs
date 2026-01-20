num = int(input("Enter Number: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print("Prime")
else:
    print("Not Prime")