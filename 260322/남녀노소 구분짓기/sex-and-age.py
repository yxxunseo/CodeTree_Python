s = int(input())
a = int(input())

if 1 <= a <= 100 :
    if s == 0 :
        if a >= 19 :
            print("MAN")
        else :
            print("BOY")
    else : 
        if a >= 19 :
            print("WOMAN")
        else : 
            print("GIRL")