def main(dates):
    while(True):
        Input = input("Date: ").strip()
        mon = Input.split()
        if "/" in Input:
            try:
                month,day,year = Input.split("/")
                day = int(day)
                month =int(month)
                year = int(year)
                if month <= 12 and day <= 31:
                    print(f"{year}-{month:0>2}-{day:0>2}")
                    break
            except Exception:
                continue
        elif mon[0] in dates:
            if "," in Input:
                day = int(mon[1].replace(",",""))
                if day <= 31:
                    month = dates.index(mon[0]) + 1
                    year = mon[2]
                    print(f"{year}-{month:0>2}-{day:0>2}")
                    break

dates = [
    "January",
    "Februrary",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

main(dates)
