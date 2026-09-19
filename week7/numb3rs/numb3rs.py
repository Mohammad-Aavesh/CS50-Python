import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        for _ in range(1,5):
            m = match.group(_)
            n = int(m)
            if len(m) > 3:
                return False
            elif len(m) > 1 and m.startswith("0"):
                return False
            elif n > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
