data = [10, 20, 30, 40, 50]
min_val = min(data)
max_val = max(data)
normalized = []
for x in data:
  normalized.append((x-min_val)/(max_val - min_val))
print(normalized)