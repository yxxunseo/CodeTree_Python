import math 

h, w = map(int, input().split())
b = (10000 * w) // (h * h)

if (1 <= h <= 1000) and (1 <= w <= 1000) :
    print(math.trunc(b))  
    if b >= 25 :
        print("Obesity")