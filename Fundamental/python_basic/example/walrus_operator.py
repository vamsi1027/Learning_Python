# TODO: walrus operators

text = "hellooooooooooo"
if (n := len(text)) > 10:
    print(f"to many value {n}")

while (n := len(text)) > 1:
    print(n)
    text = text[:-1]

print(text)
