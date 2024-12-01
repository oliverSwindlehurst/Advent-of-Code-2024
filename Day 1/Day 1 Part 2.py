with open("Day 1\Input.txt") as file_in:
    input = []
    for line in file_in:
        input.append(line)

firstColumn = []
secondColumn = []
similarityScores = []
score = 0
answer = 0

for row in input:
    splitRow = row.split()
    firstColumn.append(int(splitRow[0]))
    secondColumn.append(int(splitRow[1]))
    
firstColumn = sorted(firstColumn)
secondColumn = sorted(secondColumn)

for firstColumnRow in firstColumn:
    for secondColumnRow in secondColumn:
        if firstColumnRow == secondColumnRow:
            score += 1
    similarityScores.append(firstColumnRow * score)
    score = 0
    
for row in similarityScores:
    answer += row

print(answer)

    
    
