file = open("./data_d6.txt")
input = file.readlines()
file.close()

data = input[0].strip()

def compare(input1):

    for y in range(0, len(input1)):

        for z in range(0, len(input1)):

            if(y != z):

                if(input1[y] == input1[z]):

                    return False

    return True

#Part 1

for x in range(0, len(data) - 4):

    sample = data[x : x + 4]
    flag = compare(sample)

    if(flag):
        print(x + len(sample))
        break

#Part 2

for x in range(0, len(data) - 14):

    sample = data[x : x + 14]
    flag = compare(sample)

    if(flag):
        print(x + len(sample))
        break
