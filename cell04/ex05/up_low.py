def main():
    try:
        user_input = input()
        swapped = user_input.swapcase()
        print(swapped)
    except Exception as e:
        print("Error:", e)
if __name__ == "__main__":
    main()