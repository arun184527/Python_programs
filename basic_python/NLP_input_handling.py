token_count = 1025
if token_count > 1024:
     print("Reject input")
elif token_count > 512:
     print("Truncate input")
else:
     print("Input acceptable")