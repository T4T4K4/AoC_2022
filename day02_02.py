file = open('day02_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

score = 0
for line in lines:
    if line[:3] == "A Y" or line[:3] == "B Y" or line[:3] == "C Y":
        score += 3
    elif line[:3] == "A Z" or line[:3] == "B Z" or line[:3] == "C Z":
        score += 6

    if line[:3] == "A Y" or line[:3] == "B X" or line[:3] == "C Z":
        score += 1
    elif line[:3] == "A Z" or line[:3] == "B Y" or line[:3] == "C X":
        score += 2
    elif line[:3] == "A X" or line[:3] == "B Z" or line[:3] == "C Y":
        score += 3

print(score)
