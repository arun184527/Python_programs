confidences = [0.95, 0.7, 0.2]
i = 0
while i < len(confidences):
    c = confidences[i]
    if c >= 0.9:
        print("High confidence")
    elif c >= 0.6:
        print("Medium confidence")
    else:
        print("Low confidence")
      
    i+=1