text = input("camelCase: ")
i = 0
j = 1
k = 0
for s in text:
    i += 1
    if s.isupper():
        text = text[:i-j]+"_"+text[i-j:]
        j -= 1
        world = text[i+k].lower()
        text = text.replace(text[i+k],world,1)
        k+=1

print(text)
