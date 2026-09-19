def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 6 >= len(s) >= 2:
        if s.isdigit():
            return False
        else:
            if s.isalpha():
                return True
            for i in range(len(s)):
                if s[i].isdigit():
                    s1 = s[0:i]
                    s2 = s[i:len(s)]
                    if s2.isdigit() and s2[0] != "0":
                            return True
                    else:
                        return False
    else:
        return False

main()
