file = open('day04_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    temp1 = temp.split(",")
    temp2 = temp1[0].split("-")
    temp3 = temp1[1].split("-")
    source.append([ int(temp2[0]), int(temp2[1]), int(temp3[0]), int(temp3[1]) ])

resume = 0
for elf_pair in source:
    cond1 = elf_pair[2] <= elf_pair[0] <= elf_pair[1] <= elf_pair[3]
    cond2 = elf_pair[0] <= elf_pair[2] <= elf_pair[3] <= elf_pair[1]
    if cond1 or cond2:
        resume += 1

print("Count of pair is", resume)