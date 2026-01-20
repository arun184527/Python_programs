n = 12345
while n > 0:
    d = n % 10
    if d % 2 == 0:
        print(d, "is Even")
    else:
        print(d, "is Odd")
    n //= 10