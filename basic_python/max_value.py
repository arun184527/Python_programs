marks = {"math": 80, "science": 90, "english": 85}
max_marks = 0
for m in marks.values():
    if m > max_marks:
        max_marks = m
print(max_marks)