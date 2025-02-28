# Make sure the sorting algorithm is correct

def sort(a, b):
    for i in range(b):
        for j in range(1, b):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp


def main():
    # Sort in ascending order
    numbers = [4, 2, 3, 1, 8, 7]
    sort(numbers, 6)
    
    for i in range(6):
        print(numbers[i], end="")
    print()


if __name__ == "__main__":
    main()
