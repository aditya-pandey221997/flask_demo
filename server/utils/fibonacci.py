def fibonacci(n):
    if n == 0:
        return 0
    if n <= 1:
        return 1
    return n + fibonacci(n - 1)


def main():
    fibonacci(5)


if __name__ == '__main__':
    main()
