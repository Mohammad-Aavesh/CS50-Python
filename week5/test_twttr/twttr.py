def main():
    Word = input("Input: ")
    output = shorten(Word)
    print(f"Output: {output}")

def shorten(Word):
    for v in "AaEeIiOoUu":
        Word = Word.replace(v,"")
    return Word

if __name__ == "__main__":
    main()
