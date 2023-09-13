npt = [int(i) for i in input().split()]
n, m = npt

for i in range(1, 1 + n):
    if i == (int((n / 2) + 1)):
        print("WELCOME".center(m, "-"))
    elif i > n/2:
        print((".|." * (n + 1 - i + n - i)).center(m, "-"))
    else:
        print((".|." * (2 * i - 1 )).center(m, "-"))