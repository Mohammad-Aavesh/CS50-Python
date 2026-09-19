ans = input("What is the Answer to the Greatest Question of Life, the Universe, and Everything? ").lower().strip()
match ans:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
