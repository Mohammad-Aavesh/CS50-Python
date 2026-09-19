from PIL import Image
from PIL import ImageOps
import sys

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        if not sys.argv[1].endswith((".jpg",".png",".jpeg")) or not sys.argv[2].endswith((".jpg",".png",".jpeg")):
            print("Invalid output")
            sys.exit(1)
        ext1 = sys.argv[1][-4:]
        ext2 = sys.argv[2][-4:]
        if ext1 != ext2:
            print("Input and output have different extensions")
            sys.exit(1)
        try:
            bg = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            size = shirt.size
            bg = ImageOps.fit(bg,size)
            bg.paste(shirt,shirt)
            bg.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit(1)

if __name__ == "__main__":
    main()
