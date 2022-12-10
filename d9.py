#Get Data from File
file = open("./data_d9.txt")
input = file.readlines()
file.close()

# Part 1
# Refernce      [x, y]
# List of rope positions [0] = Head [-1] = Tail

#rope_pos_list = [[0,0] , [0,0]]

rope_pos_list =[[0,0] , [0,0], [0,0], [0,0], [0,0] , [0,0], [0,0] , [0,0], [0,0], [0,0]]

positions = [] 

def record(pos):

    global positions

    i = [pos[0], pos[1]]

    if(pos not in positions):
        positions.append(i)

#Old Solution 
for line in input:

    vector = line.split(' ')
    direction = vector[0]
    speed = int(vector[1])

    # Update Head Position
    # Will Update per frame of movement

    for x in range(speed, 0,  -1):

        if(direction == "U"):
            rope_pos_list[0][1] = rope_pos_list[0][1] + 1

        elif(direction =="D"):

            rope_pos_list[0][1] = rope_pos_list[0][1] - 1

        elif(direction == "R"):

            rope_pos_list[0][0] = rope_pos_list[0][0] + 1

        elif(direction == "L"):

            rope_pos_list[0][0] = rope_pos_list[0][0] - 1
        
        #Update Tail Postion

        for y in range(0, len(rope_pos_list) - 1):

            # Tail Above
            if(rope_pos_list[y][1] == rope_pos_list[y + 1][1] + 2):

                rope_pos_list[y + 1][1] = (rope_pos_list[y + 1][1] + 1)

                # OffSets
                # Shout out to /u/travis373 on reddit for making me impliment code that checked cornner movement
                # Comment thread: https://old.reddit.com/r/adventofcode/comments/zgwhh1/2022_day_9_part_2_cant_believe_i_didnt_see_that/izj1djo/
                if(rope_pos_list[y][0] == rope_pos_list[y + 1][0] + 2):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] + 1)

                elif(rope_pos_list[y][0] == rope_pos_list[y + 1][0] - 2):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] - 1)

                elif(rope_pos_list[y][0] == rope_pos_list[y + 1][0] + 1):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] + 1)

                elif(rope_pos_list[y][0] == rope_pos_list[y + 1][0] - 1):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] - 1)


            # Tail Bellow
            if(rope_pos_list[y][1] == rope_pos_list[y + 1][1] - 2):

                rope_pos_list[y + 1][1] = (rope_pos_list[y + 1][1] - 1)

                #offSets
                if(rope_pos_list[y][0] == rope_pos_list[y + 1][0] + 2):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] + 1)

                elif(rope_pos_list[y][0] == rope_pos_list[y + 1][0] - 2):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] - 1)
                
                elif(rope_pos_list[y][0] == rope_pos_list[y + 1][0] + 1):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] + 1)

                elif(rope_pos_list[y][0] == rope_pos_list[y + 1][0] - 1):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] - 1)


            # Tail to the Left
            if(rope_pos_list[y][0] == rope_pos_list[y + 1][0] + 2):

                rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] + 1)

                #offSets
                if(rope_pos_list[y][1] == rope_pos_list[y + 1][1] + 2):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] + 1)

                elif(rope_pos_list[y][1] == rope_pos_list[y + 1][1] - 2):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] - 1)

                elif(rope_pos_list[y][1] == rope_pos_list[y + 1][1] + 1):
                    rope_pos_list[y + 1][1] = (rope_pos_list[y + 1][1] + 1)

                elif(rope_pos_list[y][1] == rope_pos_list[y + 1][1] - 1):
                    rope_pos_list[y + 1][1] = (rope_pos_list[y + 1][1] - 1)

            # Tail to the Right
            if(rope_pos_list[y][0] == rope_pos_list[y + 1][0] - 2):

                rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] - 1)

                #offSets
                if(rope_pos_list[y][1] == rope_pos_list[y + 1][1] + 2):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] + 1)

                elif(rope_pos_list[y][1] == rope_pos_list[y + 1][1] - 2):
                    rope_pos_list[y + 1][0] = (rope_pos_list[y + 1][0] - 1)

                elif(rope_pos_list[y][1] == rope_pos_list[y + 1][1] + 1):
                    rope_pos_list[y + 1][1] = (rope_pos_list[y + 1][1] + 1)

                elif(rope_pos_list[y][1] == rope_pos_list[y + 1][1] - 1):
                    rope_pos_list[y + 1][1] = (rope_pos_list[y + 1][1] - 1)
        
            #Process new location
            record(rope_pos_list[-1])

    #debug info
    #print(rope_pos_list)
    #print()
            #print("Head: ", rope_pos_list[0])
            #print("Tail: ", rope_pos_list[-1])
            #print([direction, x])
            #print()

print(len(positions))
#print(positions)
