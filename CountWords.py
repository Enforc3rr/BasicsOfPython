words = []
lines = []
wordsCount = {}

with open("./file.txt") as file:
    lines = file.readlines()

for line in lines:
    for word in line.split(" "):
        words.append(word)

for word in words:
    if word in wordsCount:
        wordsCount[word] += 1
    else:
        wordsCount[word] = 1

print(list(sorted(wordsCount.items(),
      key=lambda x: x[1],  reverse=True))[0][0])
