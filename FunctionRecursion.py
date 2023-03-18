o = 1
 
 
def factorial(n):
    global o
    if n != 1:
        m = n
        o *= m
        n -= 1
    else:
        print(o)
        quit()
    factorial(n)
 
 
factorial(int(input()))
