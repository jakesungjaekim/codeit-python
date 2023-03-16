for a in range(1, 1000):
    for b in range(1,1000):
        c = 1000 - b - a
        if a * a + b * b == c * c and a < b < c and a + b + c == 1000:
            print(a * b * c)
