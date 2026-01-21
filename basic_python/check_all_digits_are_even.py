n = 2486
flag = True
for ch in str(n):
    if int(ch) % 2 != 0:
        flag = False
        break
if flag:
    print("All digits are even")
else:
    print("Not all digits are even")