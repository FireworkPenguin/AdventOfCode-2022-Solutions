#Open file with input data
file = open("./data_d7.txt")
input = file.readlines()
file.close()


directories = []
stack = []

SubTotal = 0

# Function to change the postion within the directory struture
# "/" To goto root
# ".." go up a level, remove newest item in stack list
# [folderName] go into this folder, add new item to the end of the stack list

def cd(input):

    if(input == "/"):

        stack.clear()

    elif(input == ".."):

        if(len(stack) > 0):
            stack.pop()

    else:
        stack.append(input)

# Adds a file or directory to the file structure, 
# goes down the stack as determined by 'cd' fucntion
# At the end the new entry is added
def insert(input):

    obj = []

    if(input[0] == "dir"):
        obj = [input[1], []]
    
    else:
        obj = [input[1], int(input[0])]

    folder = directories

    for sub in stack:

        for x in folder:

            if(x[0] == sub):

                folder = x[1]
                break

    folder.append(obj)

# Goes through each command provided in the input
# Commands:
#   $ cd: change the active directory
#   $ ls: [ignored]
#   [Other]: treated as a file/folder location, once reached it is added to the current directory
def execute():

    for x in input:
        
        s = x.strip().split(" ")

        if(x[0 : 4] == "$ ls"):
            continue

        elif(x[0 : 4] == "$ cd"):

            cd(s[2])

        else:
            insert(s)

#Creates whitespace of 4 spaces times 'num' (used to represent the depth in the directory) 
def spacer(num):

    output = ""

    for x in range(0, num):

        output = output + "    " 

    return output

#Recursive fuction that calculates the total size of a folder by adding up ALL files inside
def calFolderTotalSize(folders): 

    out = 0

    if(isinstance(folders[1], int)):

        return folders[1]

    if(isinstance(folders[1], list)):

        total = 0 

        for x in folders[1]:

            total = total + calFolderTotalSize(x)

        return total

    return out

# Recursive Function that creates a string output of the directory structure created by the provided input
# Used as a way to develop to show that the process worked
# Solutions are simplified to remove string functions
def printStruct(folders, depth):

    output = ""
    
    #Second item is the file size
    if(isinstance(folders[1], int)):

        return spacer(depth) + "[" + folders[0] + " , " + str(folders[1]) + "]\n"

    if(isinstance(folders[1], list)):

        for x in folders[1]:

            if not isinstance(x[1], int):

                value  = calFolderTotalSize(x)

                if(value <= 100000):

                    output = output + spacer(depth) + "{ " + str(x[0]) + " " + str(value) + " \n"

                else:

                    output = output + spacer(depth) + "{ " + str(x[0]) + " ** " + str(value) + " ** \n"

                output = output + printStruct(x, depth + 1)

                output = output + spacer(depth) + "}, \n"

            else:

                output = output + printStruct(x, depth + 1)

    return output

def part1_calc(folders, depth):

    output = ""

    if(isinstance(folders[1], list)):

        for x in folders[1]:

            if not isinstance(x[1], int):

                value  = calFolderTotalSize(x)

                if(value <= 100000):

                    global SubTotal 
                    
                    SubTotal = SubTotal + value

            part1_calc(x, depth + 1)

    return output

diskSpace = 0
min_diskSize = 111111111111111111111111111111

def part2_calc(folders):

    output = ""

    if(isinstance(folders[1], list)):

        for x in folders[1]:

            if not isinstance(x[1], int):

                value  = calFolderTotalSize(x)

                global min_diskSize
                global diskSpace

                if(value < min_diskSize and (value + diskSpace) > 30000000):

                    min_diskSize = value


            part2_calc(x)


    return output


def part1():

    output = part1_calc(["root", directories], 0)
    print(SubTotal)

def part2():

    global min_diskSize
    global diskSpace

    diskSpace = 70000000 - calFolderTotalSize(["root", directories])

    part2_calc(["root", directories])
    print(min_diskSize)




execute()
part1()
part2()

