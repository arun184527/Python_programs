t = (1, 2, 3)
rev = ()
for x in t:
    rev = (x,) + rev
print(rev)