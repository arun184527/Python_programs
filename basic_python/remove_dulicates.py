t = (1, 2, 2, 3)
unique = ()
for x in t:
    if x not in unique:
        unique += (x,)
print(unique)