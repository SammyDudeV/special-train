reps = int(input())
x = ""
for i in range(reps):
    p = input()
    x = p.split()
    if len(x) > 1 and len(x[1]) > 1:
        print(x[1][1])
    else:
        print(x[0])
        