import sys

def main():
    if len(sys.argv) > 2:
        print("Too many command-line arguements")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        if not sys.argv[1].endswith(".py"):
            print("Not a Python file")
            sys.exit(1)
        try:
            file = open(sys.argv[1])
            l = 0
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line.startswith("#") and len(line) > 0:
                    l += 1
            print(l)
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)


if __name__ == "__main__":
    main()
