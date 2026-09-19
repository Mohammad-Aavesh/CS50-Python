import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search("^([0-9]?[0-9]?):?([0-9]?[0-9]?)? (AM|PM) to ([0-9]?[0-9]?):?([0-9]?[0-9]?)? (AM|PM)$", s):
        a = match.group(1)
        b = match.group(2)
        d = match.group(4)
        e = match.group(5)
        HA = int(a)
        HB = int(d)
        try:
            MA = int(b)
        except ValueError:
            MA = 0
        try:
            MB = int(e)
        except ValueError:
            MB = 0
        start, end = s.split(" to ")
        if HA > 12 or HB > 12:
            raise ValueError
        elif HA == 12 and HB == 12:
            HA = 0
            HB = 0
        elif HA == 12:
            HA = 0
        elif HB == 12:
            HB = 0
        if ":" in start and ":" in end:
            if MA > 59 or MB > 59:
                raise ValueError
            elif "AM" in start:
                if MA == 0:
                    MA = "00"
                if MB == 0:
                    MB = "00"
                return f"0{HA}:{MA} to {HB+12}:{MB}"
            else:
                if MA == 0:
                    MA = "00"
                if MB == 0:
                    MB = "00"
                return f"{HA+12}:{MA} to 0{HB}:{MB}"
        elif ":" in start:
            if MA > 59:
                raise ValueError
            elif "AM" in start:
                if MA == 0:
                    MA = "00"
                if MB == 0:
                    MB = "00"
                return f"0{HA}:{MA} to {HB+12}:00"
            else:
                if MA == 0:
                    MA = "00"
                if MB == 0:
                    MB = "00"
                return f"0{HA+12}:{MA} to {HB}:00"
        elif ":" in end:
            if MB > 59:
                raise ValueError
            elif "PM" in end:
                if MA == 0:
                    MA = "00"
                if MB == 0:
                    MB = "00"
                return f"0{HA}:00 to {HB+12}:{MB}"
            else:
                if MA == 0:
                    MA = "00"
                if MB == 0:
                    MB = "00"
                return f"{HA+12}:00 to 0{HB}:{MB}"
        else:
            if "PM" in end:
                if MA == 0:
                    MA = "00"
                if MB == 0:
                    MB = "00"
                return f"0{HA}:00 to {HB+12}:00"
            else:
                if MA == 0:
                    MA = "00"
                if MB == 0:
                    MB = "00"
                return f"{HA+12}:00 to 0{HB}:00"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
