import math
def main():
    try:
        number = float(input("Give me a number: "))
        print(math.ceil(number))
    except ValuaError:
        print("That 's not a valid number.")
if __name__ == "__main__":
    main()