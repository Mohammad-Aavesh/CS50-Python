def main():
    while True:
        text = input("Fraction: ")
        try:
            percentage = convert(text)
            fuel = gauge(percentage)
            print(fuel)
            return
        except (ValueError,ZeroDivisionError):
            pass

def convert(fraction):
    if fraction.find("/") > 0:
        int1,int2 = fraction.split("/")
        int1 = int(int1)
        int2 = int(int2)
        if int1 > int2 or int1 < 0:
            raise ValueError
        fuel = round((int1/int2)*100)
        return fuel
    else:
        raise ValueError

def gauge(percentage):
    if percentage == 1 or percentage == 0 :
        return "E"
    elif percentage == 100 or percentage == 99 :
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

