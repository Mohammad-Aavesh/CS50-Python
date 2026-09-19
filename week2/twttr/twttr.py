Input = input("Input: ")
for s in Input:
    for a in "AaEeIiOoUu":
        if s == a:
            Input = Input.replace(s,"")
print("Output:",Input)
