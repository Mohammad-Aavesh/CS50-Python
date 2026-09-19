import sys
import csv

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        try:
            with open(sys.argv[1]) as file1:
                reader = csv.DictReader(file1)
                with open(sys.argv[2],"w") as file2:
                        writer = csv.DictWriter(file2, fieldnames=["first","last","house"])
                        writer.writeheader()
                        for row in reader:
                            last,first = row["name"].split(",")
                            first = first.strip()
                            last = last.strip()
                            house = row["house"]
                            writer.writerow({
                                "first":first,
                                "last":last,
                                "house":house
                            })
        except FileNotFoundError:
            print(f"could not read {sys.argv[2]}")
            sys.exit(1)

if __name__ == "__main__":
    main()
