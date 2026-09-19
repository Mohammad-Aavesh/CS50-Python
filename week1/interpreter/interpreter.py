text = input("Expression: ")

words = text.split()
x = float(words[0])
y = words[1]
z = float(words[2])

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
