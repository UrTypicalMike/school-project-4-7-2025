score = int(input("Enter your score: "))
if 70 <= score <= 100:
    print("A")
elif 60 <= score < 70:
    print("B")
elif 50 <= score < 60:
    print("C")
elif 45 <= score < 50:
    print("D")
elif 40 <= score < 45:
    print("E")
elif 0 <= score < 40:
    print("F")
else:
    print("Invalid score")
