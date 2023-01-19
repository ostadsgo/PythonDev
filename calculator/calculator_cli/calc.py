def add(x, y):
    return x + y


def minus(x, y):
    return x - y

    
def mul(x, y):
    return x * y


def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return None
        

def main():
    # a simple test
    res = div(10, 2)
    print(res)


if __name__ == "__main__":
    main()
