import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match := re.search(r'^<iframe(?:.*)? src="(.+)(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})"(.*)?></iframe>',s):
        return "https://"+"youtu.be/"+match.group(2)
    else:
        return "None"

if __name__ == "__main__":
    main()
