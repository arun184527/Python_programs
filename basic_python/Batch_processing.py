data = list(range(1,21))
batch_size = 5
for i in range (0, len(data), batch_size):
    batch = data[i:i+batch_size]
    print(batch) 