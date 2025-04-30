# Make sure the function reverse actually reverses the string

def reverse(string):
    rev = ""  # Placeholder for reversed string
    size = len(string)
    for i in range(size):
        rev = rev + string[size-i-1]
    return rev


def main():
    string = "Forward"
    string = reverse(string)
    print(string)


if __name__ == "__main__":
    main()
