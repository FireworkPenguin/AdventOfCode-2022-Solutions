
#Get Data from File
file = open("./data_d2.txt")
data = file.readlines()
file.close()


# First Coloum is the oponent (a)
# Second is you (b)


def compare(a,b):

    if(b == "X"):

        if(a == "A"):

            return 0

        elif(a == "B"):

            return -1

        elif(a == "C"):

            return 1

    elif(b == "Y"):

        if(a == "A"):

            return 1

        elif(a == "B"):

            return 0

        elif(a == "C"):

            return -1

    elif(b == "Z"):

        if(a == "A"):

            return -1

        elif(a == "B"):

            return 1

        elif(a == "C"):

            return 0

def item_Score(a):

    if(a == "X"):

        return 1

    elif(a == "Y"):

        return 2

    else:

        return 3


#Part 1

Total_Score = 0

for x in range(0, len(data)):

    item = data[x]
    p1_move = item[0]
    p2_move = item[2]


    #Determine Winner
    result = compare(p1_move, p2_move)
    if(result == 0):

        Total_Score = Total_Score + 3

    elif(result == 1):

        Total_Score = Total_Score + 6


    #Add points for Item used
    Total_Score = Total_Score + item_Score(p2_move)

print(Total_Score)

#Part 2

Total_Score = 0

for x in range(0, len(data)):

    item = data[x]
    p1_move = item[0]
    p2_move = item[2]


    #Determine Winner
    if(p2_move == "X"):

        Total_Score = Total_Score + 0

        if(p1_move == "A"):

            Total_Score = Total_Score + item_Score("Z")

        elif(p1_move == "B"):

            Total_Score = Total_Score + item_Score("X")

        elif(p1_move == "C"):

            Total_Score = Total_Score + item_Score("Y")
        

    elif(p2_move == "Y"):

        Total_Score = Total_Score + 3 
        
        if(p1_move == "A"):

            Total_Score = Total_Score + item_Score("X")

        elif(p1_move == "B"):

            Total_Score = Total_Score + item_Score("Y")

        elif(p1_move == "C"):

            Total_Score = Total_Score + item_Score("Z")

    elif(p2_move == "Z"):

        Total_Score = Total_Score + 6 
        
        if(p1_move == "A"):

            Total_Score = Total_Score + item_Score("Y")

        elif(p1_move == "B"):

            Total_Score = Total_Score + item_Score("Z")

        elif(p1_move == "C"):

            Total_Score = Total_Score + item_Score("X")


print(Total_Score)