import random

def main():
    level = get_level()
    points = 10
    que = 10
    while que != 0:
        x = generate_integer(level)
        y = generate_integer(level)
        cz = x+y
        chance = 3
        while chance != 0:
            try:
                uz = int(input(f"{x} + {y} = "))
            except ValueError:
                uz = -1
            if cz == uz:
                que -= 1
                chance = 3
                break
            else:
                chance -= 1
                print("EEE")
            if chance == 0:
                print(f"{x} + {y} = {cz}")
                que -= 1
                points -= 1
    print(f"Score: {points}")

def get_level():
    while (True):
        level = input("Level: ")
        if level in ["1","2","3"]:
            level = int(level)
            return level

def generate_integer(level):
    if level == 1:
        return random.randrange(0,10)
    elif level == 2:
        return random.randrange(10,100)
    else:
        return random.randrange(100,1000)

if __name__ == "__main__":
    main()
