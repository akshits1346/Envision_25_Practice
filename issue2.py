# Make sure program prints all even numbers from 1 to 40

def main():
    even = 0
    for i in range(20):
        even += 2
        print(even, end="\t")
    print()


if __name__ == "__main__":
    main()
