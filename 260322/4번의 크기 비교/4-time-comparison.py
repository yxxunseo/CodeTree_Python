a = int(input())
b, c, d, e = map(int, input().split(" "))

if 1 <= a<= 100 and 1 <= b <= 100 and 1 <= c  <= 100 and 1 <= d <= 100 and 1 <= e <= 100:
    print(int(a > b))
    print(int(a > c))
    print(int(a > d))
    print(int(a > e))
