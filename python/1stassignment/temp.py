temp = float(input())
scale = input()
if scale == "C":
    print((temp * 9 / 5) + 32)
elif scale == "F":
    print((temp - 32) * 5 / 9)
