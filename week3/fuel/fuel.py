def main():
    while True:
        text = input("Fraction: ")
        if(text.find("/") > 0):
            int1,int2 = text.split("/")
            if int1.isdecimal() and int2.isdecimal():
                int1 = int(int1)
                int2 = int(int2)
                if int1 <= int2 and int2 != 0:
                    fuel = round((100/int2)*int1)
                    if fuel == 1 or fuel == 0 :
                        print("E")
                        return
                    elif fuel == 100 or fuel == 99 :
                        print("F")
                        return
                    else:
                        print(f"{fuel}%")
                        return

main()

