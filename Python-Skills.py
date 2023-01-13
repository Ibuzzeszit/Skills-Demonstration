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

def charInString(char, string):
    for x in string:
        if x == char:
            return True
    return False

def multiple(list):
    count = []
    for x in list:
        for y in count:
            if x == y:
                return y
        count.append(x)
    return "No numbers appear multiple times"


def main():
    print("Square: %s" % square(20))
    print("")

    print("Highest number: %s" % highest(5, 4, 10))
    print("")

    print("The character is in the String: %s" % charInString('s', "faster"))
    print("")

    print("Number that appears multiple times: %s " % multiple([12, 8, 55, 23, 12]))
    print("")

if __name__ == "__main__":
    main()
