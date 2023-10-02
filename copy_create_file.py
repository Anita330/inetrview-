with open("first.txt") as f:
    conetnt = f.read()
with open("copy.txt", 'w') as f:
    f.write(conetnt)
