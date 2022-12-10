#Get Data from File
file = open("./data_d10.txt")
input = file.readlines()
file.close()


def part1_run(instruct):

    #inportant values
    milestones = range(20, 10000, 40)
    milestone_Sum = 0

    #Numbers
    cycle = 1
    index = 0
    value = 1

    queue = []

    while(True):

        cycle = cycle + 1

        #Work per operation
        if(len(queue) == 0): 

            operation = instruct[index].split(" ")
            
            #empty queue do the Next instuction
            if(operation[0] == "addx"):
                queue.append(int(operation[1]))

            index = index + 1

        else:
           value = value + queue.pop()

        if(cycle in milestones):
            milestone_Sum = milestone_Sum + (cycle * value)


        if(index >= len(instruct) and len(queue) == 0):
            break


    return milestone_Sum

def part2_run(instruct):

    #inportant values
    milestones = range(40, 10000, 40)
    milestone_Sum = 0

    #Numbers
    cycle = 0
    index = 0
    value = 1

    queue = []
    
    display = ""

    pixel = 0

    while(True):

        #See if pixel should be drawn
        if ((value - pixel) > -2 and (value - pixel) < 2 ):
            display = display + "#"
        else:
            display = display + "."

        pixel = pixel + 1

        #Work per operation
        if(len(queue) == 0): 

            operation = instruct[index].split(" ")
            
            #empty queue do the Next instuction
            if(operation[0] == "addx"):
                queue.append(int(operation[1]))

            index = index + 1

        else:
            value = value + queue.pop()

        cycle = cycle + 1

        if(cycle in milestones):

            milestone_Sum = milestone_Sum + (cycle * value)

            print(display)
            pixel = 0
            display = ""

        if(index >= len(instruct) and len(queue) == 0):
            break
        
        

    return milestone_Sum


print(part1_run(input))
part2_run(input)