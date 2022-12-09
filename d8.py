#Open file with input data
file = open("./data_d8.txt")
input = file.readlines()
file.close()

trees = []

#Setup
for line in input:

    row = []

    columns = line.strip()

    for num in columns:

        row.append(int(num))

    trees.append(row)

trees_x_max = len(trees[0])
trees_y_max = len(trees)

#debug
for x in trees:

    print(x)


#Get Tree
def findTreeFunction(x, y):

    if(x < 0 or x > trees_x_max):

        return 0

    if(y < 0 or y > trees_y_max):

        return 0

    return trees[x][y]

#Recursive Function that checks a line of trees
def treeLineCheck(x, y, x_step, y_step, tree_h_max):

    #Edge cases
    if(x < 0 or x > trees_x_max - 1 or y < 0 or y > trees_y_max - 1):

        return 0

    #Main Fucntion
    value = findTreeFunction(x, y)

    next_height = max(tree_h_max, value)

    next_value = treeLineCheck(x + x_step, y + y_step, x_step, y_step, next_height)

    return max(next_height, next_value)



#
def isVisable(x, y):

    treeHeight = findTreeFunction(x, y)

    #Edge Cases
    if(x == 0 or x == trees_x_max - 1 or y == 0 or y == trees_y_max - 1):
        return True

    #check up y = +1

    up = treeLineCheck(x, y + 1, 0, 1, 0)
    if(treeHeight > up):
        return True

    #check down y = -1

    down = treeLineCheck(x, y - 1, 0, -1, 0)
    if(treeHeight > down):
        return True

    #check left x = -1

    left = treeLineCheck(x - 1, y, -1, 0, 0)
    if(treeHeight > left):
        return True

    #check right x = +1

    right = treeLineCheck(x + 1, y, 1, 0, 0)
    if(treeHeight > right):
        return True

    #Not Visable from any side
    return False

def visablityScoreCheck(x, y, x_step, y_step, treeheight):

    print([x, y, x_step, y_step, treeheight])

    #Edge cases
    if(x < 0 or x >= trees_x_max or y < 0 or y >= trees_y_max):
        return 0

    value = findTreeFunction(x, y)
    
    #Check if the next tree is taller
    if(value >= treeheight):
        return 1

    #Else check the next one over
    return visablityScoreCheck(x + x_step, y + y_step, x_step, y_step, treeheight) + 1 

def visablityScore(x,y):

    treeHeight = findTreeFunction(x, y)
    
    print([x, y, treeHeight])

    #check up y = +1
    up = visablityScoreCheck(x, y + 1, 0, 1, treeHeight)

    #check down y = -1
    down = visablityScoreCheck(x, y - 1, 0, -1, treeHeight)

    #check left x = -1
    left = visablityScoreCheck(x - 1, y, -1, 0, treeHeight)

    #check right x = +1
    right = visablityScoreCheck(x + 1, y, 1, 0, treeHeight)

    #Not Visable from any side
    print([up, down, left, right])
    return up * down * left * right

    



Total = 0
max_Score = 0

for x in range(trees_x_max):
    for y in range(trees_y_max):

        #Part 1
        if(isVisable(x, y)):

            Total = Total + 1

        #Part 2
        #I do not know why it works when reversed?
        max_Score = max(max_Score, visablityScore(y,x)) 

   

print(Total)
print(max_Score)






















