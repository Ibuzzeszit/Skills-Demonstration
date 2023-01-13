def square(n):
    n = n*n
    return n

def highest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b > a and b >= c:
        return b
    else:
        return c


def main():
    print(square(20))
    print(highest(5, 4, 10))

if __name__ == "__main__":
    main()
