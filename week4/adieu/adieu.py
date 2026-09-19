import inflect

def main():
    L1 = []
    while(True):
        try:
            Name = input("Name: ")
            L1.append(Name)
        except EOFError:
            print()
            goodbye(L1)
            return

def goodbye(List):
    p = inflect.engine()
    print(f"Adieu, adieu, to {p.join(List)}")

main()
