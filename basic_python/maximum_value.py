marks = {"math": 78, "science": 92, "english": 85}
max_key = ""
max_val = 0
for k, v in marks.items():
    if v > max_val:
        max_val = v
        max_key = k
print(max_key, max_val)