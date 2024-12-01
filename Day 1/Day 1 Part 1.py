with open("Day 1\Input.txt") as file_in:
    input = []
    for line in file_in:
        input.append(line)

firstColumn = []
secondColumn = []
distanceList = []
answer = 0

for row in input:
    splitRow = row.split()
    firstColumn.append(int(splitRow[0]))
    secondColumn.append(int(splitRow[1]))
    
firstColumn = sorted(firstColumn)
secondColumn = sorted(secondColumn)

counter = 0

while counter < len(firstColumn):
    if firstColumn[counter] < secondColumn[counter]:
        distanceList.append(secondColumn[counter] - firstColumn[counter])
    else:
        distanceList.append(firstColumn[counter] - secondColumn[counter])
    counter += 1

for row in distanceList:
    answer += row

print(answer)

    
    
