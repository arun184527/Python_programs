nums = [1, 2, 2, 3, 4, 1]
X = []

for n in nums:
    if n not in X:
        X.append(n)
print(X)