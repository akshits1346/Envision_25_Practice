# Make sure the function sum_list actually sums the numbers in the list

def sum_list(numbers):
    total = 0  # Placeholder for sum
    for num in numbers:
        total += num  # Incorrect accumulation
    return total


def main():
    numbers = [1, 2, 3, 4, 5]
    result = sum_list(numbers)
    print(result)


if __name__ == "__main__":
    main()
