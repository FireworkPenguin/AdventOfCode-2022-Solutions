#Get Data from File
file = open("./data_d4.txt")
input = file.readlines()
file.close()

data = []

#Input perperation
for line in input:

    temp_line = line.strip().split(',')
    part1 = temp_line[0].split('-')
    part2 = temp_line[1].split('-')

    result = [[int(part1[0]), int(part1[1])], [int(part2[0]), int(part2[1])]]
    data.append(result)


def contains(input1, input2):

    group1_min = input1[0]
    group1_max = input1[1]

    group2_min = input2[0]
    group2_max = input2[1]


    if(group1_min >= group2_min and group1_max <= group2_max):
        return True

    if(group1_min <= group2_min and group1_max >= group2_max):
        return True

    return False

def overlaps(input1, input2):

    group1_min = input1[0]
    group1_max = input1[1]

    group2_min = input2[0]
    group2_max = input2[1]


    if(group1_min in range(group2_min, group2_max + 1)):
        return True

    if(group1_max in range(group2_min, group2_max + 1)):
        return True

    if(group2_min in range(group1_min, group1_max + 1)):
        return True

    if(group2_max in range(group1_min, group1_max + 1)):
        return True
        
    return False

#PArt 1

Total = 0

for x in data:

    if(contains(x[0], x[1])):
        Total = Total + 1

print(Total)


#PArt 1

Total = 0

for x in data:

    if(overlaps(x[0], x[1])):
        Total = Total + 1

print(Total)

