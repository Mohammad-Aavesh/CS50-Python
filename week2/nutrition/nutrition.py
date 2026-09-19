def main():
    Input = input("Items: ").lower()
    dict1 = {"apple":130, "avocado":50, "kiwifruit":90, "pear":100, "sweet cherries":100}
    for d in dict1:
        if Input == d:
            print("Calories:",dict1[d])

main()
