# Print correct factorial of the variable "num"

def factorial(n):
    if n == 2:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    num = 8
    print(factorial(num))

if __name__ == "__main__":
    main()