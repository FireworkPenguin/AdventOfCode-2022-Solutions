file = open("./data_d5.txt")
input = file.readlines()
file.close()


crates = []
orders = []


#Split the data into orders and creates
tempCrates = []
lineNum = 0

for n in range(0, 20):

    temp = len(input[n])

    if(temp < 2):
        lineNum = n
        
tempCrates = input[0:lineNum]
orders = input[lineNum + 1 : ]

#Make add placeholder creates into each array
for w in range(0,len(tempCrates) - 1):

    line = tempCrates[w]

    temp = line.strip("\n")

    for x in range(0, len(temp), 4):
        if(temp[x: x + 4] == "    "):
            temp = temp[0:x] + "[0] " + temp[x+4:len(temp)]


    tempCrates[w] = temp


# Needed two copies of the array since python was not allowing me 
# to copy the list without the copy being modified by the first
# part
crates1 = [[],[], [],[], [],[], [],[], []]
crates2 = [[],[], [],[], [],[], [],[], []]

#Make the creates into a double array
for x in range(len(tempCrates) - 2, -1, -1):

    line = tempCrates[x].split(' ')

    for y in range(0, 9):

        if("[0]" not in line[y]):
            crates1[y].append(line[y].strip())
            crates2[y].append(line[y].strip())

#Part 1
for o in orders:

    breakdown = o.strip().split(' ')

    count = int(breakdown[1])

    start = int(breakdown[3]) - 1
    stop = int(breakdown[5]) - 1

    temp = []

    #Remove old creates
    for x in range(0, count):

        temp.append(crates1[start].pop())

    crates1[stop] = crates1[stop] + temp
        

#Create Code word
word = ""
for line in crates1:
    word = word + line[-1].strip("[").strip("]")

print(word)




#Part 2
for o in orders:

    breakdown = o.strip().split(' ')

    count = int(breakdown[1])

    start = int(breakdown[3]) - 1
    stop = int(breakdown[5]) - 1

    temp = []

    #Remove old creates
    for x in range(0, count):

        temp.append(crates2[start].pop())

    #Reverse keeps the order
    temp.reverse()    

    crates2[stop] = crates2[stop] + temp

#Create Code word
word = ""
for line in crates2:
    word = word + line[-1].strip("[").strip("]")

print(word)

