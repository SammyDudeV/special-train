reps = int(input())
for i in range(reps):
    txt = input()
    if "cat" in txt:
        x = txt.replace("cat", "parrot")
        print(3*x, end=" ")
    else:
        print(3*txt, end=" ")
    print("and dogs")
    