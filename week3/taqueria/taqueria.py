def main(dic):
    Total = 0.0
    while(True):
        try:
            text = input("Item: ").title()
        except EOFError:
            print()
            return
        else:
            for d in dic:
                if text == d:
                    Total = Total + dic[d]
                    print(f"Total: ${Total:.2f}")

dict1 ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
main(dict1)
