def main():
    greeting = input("Greeting:")
    money = value(greeting)
    print(f"${money}")

def value(greet):
    if "hello" in greet or "Hello" in greet:
        return 0
    elif "H" in greet:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
