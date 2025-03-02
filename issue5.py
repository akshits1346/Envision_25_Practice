# Only print the given string, nothing more
# Bonus if you don't count the number of characters in the string manually

def main():
    str_val = "Welcome to IEEE\n"
    l=len(str_val)
    for i in range(l):
        print(str_val[i], end="")
    print()


if __name__ == "__main__":
    main()
