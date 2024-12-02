with open("Day 2\InputTest.txt") as file_in:
    input = []
    for line in file_in:
        input.append([int(x) for x in line.split()])

answer = 0
counter = 0

for row in input:
    numberToTest = row[0]
    for number in row:
        if(numberToTest > number and not(numberToTest >= number + 3)):
            counter += 1
        if(numberToTest < number and not(numberToTest <= number - 3)):
            counter += 1
        
        if(counter == len(row) - 1):
            answer += 1
        numberToTest = number
    counter = 0    

print(answer)