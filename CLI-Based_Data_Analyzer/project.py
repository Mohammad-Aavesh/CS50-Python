import sys
import csv


def main():
    lists = input_validation()
    heading = lists[0]
    row, column = lists[1]
    data = lists[2]
    print("******************************************")
    print("              DATA   ANALYZER             ")
    print("******************************************")
    print(f"        Columns : {column}")
    print(f"           rows : {row}")
    print("******************************************")
    i = 0
    for d in data:
        print_data(d, heading[i])
        i += 1
    print("*****************************************")


def input_validation():
    if len(sys.argv) != 2:
        sys.exit("Error: Program expects 1 csv file as argument")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("InvalidFileError: Program expects a csv file")
    try:
        with open(sys.argv[1]) as file:
            lines = csv.reader(file)
            # Storing heading
            heading = next(lines)
            # Counting columns
            columns = len(heading)
            data = []
            rows = 0
            # Getting data in a list
            for line in lines:
                rows += 1
                data.append(line)
            try:
                _ = data[0]
            except IndexError:
                sys.exit(f"EmptyFileError: {sys.argv[1]} File is Empty")
            # Sorting data in a list
            lists = []
            for _ in range(columns):
                li = []
                for d in data:
                    try:
                        li.append(d[_])
                    except IndexError:
                        li.append("")
                lists.append(li)
            # Getting Important Data
            results = []
            for l in lists:
                result = calculations(l)
                results.append(result)
            output = []
            output.append(heading)
            dimension = [rows, columns]
            output.append(dimension)
            output.append(results)
            return output
    except FileNotFoundError:
        # Handeling File not found Error
        sys.exit(f"FileNotFoundError: {sys.argv[1]} doesn't exit in current folder/directory")


def calculations(lists):
    listz = []
    for l in lists:
        if l != "":
            listz.append(l)
    try:
        listz = [float(l) for l in listz]
        return numerical_calculations(sorted(listz))
    except ValueError:
        return categorical_calculations(sorted(listz))


def numerical_calculations(lists):
    data = []
    element = len(lists)
    if element == 0:
        data.append("None")
        return data
    data.append("Numeric")
    data.append(str(element))
    total = 0
    for l in lists:
        total += l
    data.append(str(total))
    Mean = str(total/element)
    data.append(Mean)
    Median = median_calculator(lists)
    data.append(Median)
    data.append(str(max(lists)))
    data.append(str(min(lists)))
    return data


def categorical_calculations(lists):
    data = []
    data.append("Categoric")
    unique = []
    for l in lists:
        if l not in unique:
            unique.append(l)
    data.append(f"{len(unique)}")
    data.append(unique)
    occurance = []
    for u in unique:
        occ = []
        occ.append(u)
        count = 0
        for l in lists:
            if l == u:
                count += 1
        occ.append(str(count))
        occurance.append(occ)
    data.append(occurance)
    return data


def median_calculator(lists):
    element = len(lists)
    element -= 1
    if element % 2 == 0:
        i = int(element/2)
        median = str(lists[i])
        return median
    else:
        i = int(element/2)
        median = str((lists[i] + lists[i+1])/2)
        return median


def print_data(lists, heading):
    if lists[0] == "Numeric":
        print("__________________________________________\n")
        print(f"    Column Name : {heading}   Type({lists[0]})")
        print("__________________________________________\n")
        print(f"     Number of Values : {lists[1]}")
        print(f"     Sum of Value : {lists[2]}")
        print(f"     Mean : {lists[3]}")
        print(f"     Median : {lists[4]}")
        print(f"     Maximum Value : {lists[5]}")
        print(f"     Minimum Value : {lists[6]}")
    elif lists[0] == "Categoric":
        print("__________________________________________\n")
        print(f"    Column Name : {heading}   Type({lists[0]})")
        print("__________________________________________\n")
        print(f"     Unique Values : {lists[1]}")
        for u in lists[2]:
            print(f"     {u}")
        print(f"    Value and their occurance")
        for count in lists[3]:
            print(f"     {count[0]}  {count[1]}")
    elif lists[0] == "None":
        print("__________________________________________\n")
        print(f"    Column Name : {heading}   Type({lists[0]})")
        print("__________________________________________\n")
        print(f"         This Column is Empty.")


if __name__ == "__main__":
    main()
