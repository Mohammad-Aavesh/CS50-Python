from datetime import datetime, date
import re
import sys
import inflect


def main():
    Bday = input("Date of Birth: ")
    try:
        print(convert(Bday))
    except ValueError:
        sys.exit("Invalid date")


def convert(Bday):
    if not re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", Bday):
        raise ValueError
    Bday = datetime.strptime(Bday, "%Y-%m-%d").date()
    today = date.today()
    minutes = int(((today - Bday).days)*1440)
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"


if __name__ == "__main__":
    main()
