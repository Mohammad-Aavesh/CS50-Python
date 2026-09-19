def main():
    DueAmount = 50
    ChangeOwed = 0
    while DueAmount > 0:
        print("Amount Due:",DueAmount)
        try:
            coin = int(input("Insert Coin: "))
        except ValueError:
            coin = 0
        if coin == 25 or coin == 10 or coin == 5:
            DueAmount = DueAmount - coin
            if DueAmount <= 0:
                ChangeOwed = abs(DueAmount)
    return ChangeOwed


change = main()
print("Change Owed:",change)
