def main(dict1):
    while(True):
        try:
            text = input().upper()
        except EOFError:
            print()
            dict1 = dict(sorted(dict1.items()))
            for d in dict1:
                print(f"{dict1[d]} {d}")
            return
        if text in dict1:
            dict1[text] = dict1[text]+1
        else:
            dict1[text] = 1

dict1 ={}
main(dict1)


