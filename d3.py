#Get Data from File
file = open("./data_d3.txt")
input = file.readlines()
file.close()

data = input

#Process Data

def splitLine(line):

    temp = str(line.strip())

    line_length = len(temp)
    compart_length = line_length // 2

    part1 = temp[0 : compart_length]
    part2 = temp[compart_length : line_length]

    return [part1, part2]

def pirorityNum(letter):

    if(letter >= "a"):

        return ord(letter) - 96

    return ord(letter) - 38

def findPriorities(strA, strB):

    for x in strA:
        for y in strB:

            if(x == y):
                return x

    return ''

def findCommon(strA, strB, strC):

    for x in strA:
        for y in strB:
            for z in strC:
                if(x == y and y == z):
                    return x



    return ''


#Part 1

total = 0

for x in data:

    input = splitLine(x)

    total = total + pirorityNum(findPriorities(input[0], input[1]))

print(total)

#Part 2

total = 0

for value in range(0, len(data), 3):

    total = total + pirorityNum(findCommon(data[value], data[value + 1], data[value + 2]))

print(total)

