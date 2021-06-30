with open("file.txt", "w") as f:
    f.write("Hello World Python Programming")

with open('file.txt', 'w+') as f:
    f.write("Hello")
    print(f.seek(0))
    data = f.readlines()
    for line in data:
        words = line.split()
        print(words)
