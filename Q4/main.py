from multiples import is_one_multiple_of_other

def main():
    while True:
        a = int(input("Enter first number (-1 to stop): "))
        if a == -1:
            break

        b = int(input("Enter second number (-1 to stop): "))
        if b == -1:
            break

        if is_one_multiple_of_other(a, b):
            print("Yes - one number is a multiple of the other.")
        else:
            print("No - neither number is a multiple of the other.")

if __name__ == "__main__":
    main()