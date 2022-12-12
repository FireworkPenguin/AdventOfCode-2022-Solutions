import math


#Get Data from File
file = open("./data_d11.txt")
data = file.read().split("\n\n")
file.close()


#Define a monkey in code
class monkey:

    index = 0

    items = []
    operation = ['+', 0] #= [symbol, amount]
    test = 0
    monkey_true = 0
    monkey_false = 0

    monkey_business = 0

    def __init__(self, i, it, operation, divisor, monkey_1, monkey_2):

        self.index = i

        self.items = it
        self.operation = operation
        self.test = divisor
        self.monkey_true = monkey_1
        self.monkey_false = monkey_2

        pass


#Create the monkeys base on the input

clearing = []

#me = monkey(1)

for x in range(0, len(data)):

    #Make each Line into its own string and clean it
    lines = data[x].split('\n')

    for y in range(0, len(lines)):

        lines[y] = lines[y].strip()

        if(y > 1):

            lines[y] = lines[y].split()

        if(y == 1):

            lines[y] = lines[y].split(': ')

            lines[y][1] = lines[y][1].split(', ')

            for z in range(0, len(lines[y][1])):

                lines[y][1][z] = int(lines[y][1][z])

    
    #Road Map for data extraction
    '''
        index = given

        items = [num] = lines[1][1]
        operation = [symbol, amount] = [lines[2][-2], lines[2][-1]]
        test = num =  lines[3][-1]
        monkey_true = 0 =  lines[4][-1]
        monkey_false = 0 =  lines[5][-1]


    '''

    #Refine Line 3
    focus = lines[2]
    operation = ['', 0]

    #Determine Sign
    if(focus[-2] == "+"):
        operation[0] = 'plus'

    else:
        operation[0] = 'mult'

    #Determine amount
    if(focus[-1] == "old"):
        operation[1] = 'self'

    else:
        operation[1] = int(focus[-1])

    print(operation)

    new = monkey(x, lines[1][1], operation, int(lines[3][-1]), int(lines[4][-1]), int(lines[5][-1]))

    clearing.append(new)

#Part 1

# super max stress value
# Needed due to increasing stress levels
# Max_Stress product of all the test values
# Max_Stress is the modulus of all the test values 
# Since it will retain the relation each denominator when dividing

max_stress = 1

for m in clearing:

    max_stress = max_stress * m.test



for round in range(0, 10000):

    for m in range(0, len(clearing)):

        clearing[m] = clearing[m]

        while(len(clearing[m].items) > 0):

            item = clearing[m].items.pop()
            
            num = clearing[m].operation[1]

            if(num == "self"):
                num = item

            #do operation
            if(clearing[m].operation[0] == "plus"):
                value = item + num

            else:
                value = item * num

            # Divide by 3
            # Part 1
            #value = math.floor(value // 3)

            #Means to manage stress in part 2
            value = value % max_stress


            #Do test
            fact = False 
            
            if((value % clearing[m].test) == 0):
                fact = True


            #print(value)

            # give to next monkey
            if(fact):
                clearing[clearing[m].monkey_true].items.append(value)

            else:
                clearing[clearing[m].monkey_false].items.append(value)

            clearing[m].monkey_business = clearing[m].monkey_business + 1

        #for x in clearing:
        #    print(x.items)
        #print()

#Determine the two highest monkey buiness 
p1_max = 0
p1_max_2 = 0

max_lists = []

for m in clearing:

    max_lists.append(m.monkey_business)

max_lists.sort()

print(max_lists)

print(max_lists[-1] * max_lists[-2])