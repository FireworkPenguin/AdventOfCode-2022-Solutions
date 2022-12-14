import math

#Get Data from File
file = open("./data_d12.txt")
fileData = file.readlines()
file.close()


map = []

#Map preparation

for section in fileData:

    map.append(section[0:-1].strip())


#print(map)



#Start = [0, 20]

#get value at [x,y] position
def evlationAt(pos_1_x, pos_1_y):
    
    #global map

    if(not checkInBounds(pos_1_x, pos_1_y)):
        return "-"

    else:
        return map[pos_1_y][pos_1_x]

def evlationValue(mark):

    if(mark == 'S'):
        return 0
    
    elif(mark == 'E'):
        return 25

    elif(mark == '-'):

        return -2

    else:

        return ["a","b","c","d","e","f","g","h","i","j","k",
        "l","m","n","o","p","q","r","s","t","u"
        ,"v","w","x","y","z"].index(mark)


#Elvation Comaprison function
# input: pos_1_x pos_2_x pos_1_y pos_2_y 
#

def evlationCompare(pos_1_x, pos_1_y, pos_2_x, pos_2_y):

    if(checkInBounds(pos_1_x, pos_1_y) and checkInBounds(pos_2_x, pos_2_y)):

        if(evlationValue(evlationAt(pos_1_x, pos_1_y)) > evlationValue(evlationAt(pos_2_x, pos_2_y))):

            return (evlationValue(evlationAt(pos_1_x, pos_1_y)) - evlationValue(evlationAt(pos_2_x, pos_2_y)))

        return  evlationValue(evlationAt(pos_2_x, pos_2_y)) - evlationValue(evlationAt(pos_1_x, pos_1_y))

    return -100


#Bounds check
def checkInBounds(x, y):

    #print(x, " ", y)

    if(x > -1 and y > -1 and x < len(map[0]) - 1 and y < len(map) - 1):
        #print(True)
        return True

    #print(False)
    return False


max_depth = 450 #Height * Width - the count of Every tile in the map

#path finding alogrim

def pathFinder(x, y, path):

    #print(path)
    
    global max_depth
    
    #if(not checkInBounds(x, y)):
    #    return []

    point = [x,y]

    #add point to path
    #path.append(point)

    new_path = path.copy()

    new_path.append(point)

    
    #new_path = path + [point]
    
    if(len(path) > max_depth):
        return []

    #Check if at the end
    if(evlationAt(x,y) == "E"):
        max_depth = len(new_path)
        return new_path

    # Recurse into the ajsent squares (left, right, up, and down)
    # - Check not in path list
    # - Check that it is in bounds
    # - Check that there is less than two difference between ponits [-1, 0, 1]
    foundPaths = []

    #UP
    if(checkInBounds(x, y + 1)):
        if(([x, y + 1] not in new_path) and (evlationCompare(x, y , x, y + 1) < 2)):
            foundPaths.append(pathFinder(x, y + 1, new_path))

    #Down
    if(checkInBounds(x, y - 1)):
        if(([x, y - 1] not in new_path) and (evlationCompare(x, y , x, y - 1) < 2)):
            foundPaths.append(pathFinder(x, y - 1, new_path))

    #Left
    if(checkInBounds(x - 1, y)): 
        if(([x - 1, y] not in new_path) and (evlationCompare(x, y , x - 1, y) < 2)):
            foundPaths.append(pathFinder(x - 1, y, new_path))

    #Right
    if(checkInBounds(x + 1, y)): 
        if(([x + 1, y] not in new_path) and (evlationCompare(x, y , x + 1, y) < 2)):
            foundPaths.append(pathFinder(x + 1, y, new_path))

    # Return the smallest path that goes to the end point
    
    finalPath = []
    #max_length = 7200

    if(len(foundPaths) > 0):

        for np in foundPaths:

            #If empty use first path provided as base
            #keep a path if it has elements in it
            if(len(np) > 0):
                #if (len(new_path) > 0):
                #    finalPath = path

                #continue

                if(evlationAt(np[-1][0], np[-1][1]) == "E"):
                    
                    
                    finalPath = np
                    max_depth = len(finalPath)
            
                    return np
                
    return finalPath

#route = pathFinder(0,0,[])

route = pathFinder(0, 20,[])

print(len(route))
print(route[0])
print(route[-1])