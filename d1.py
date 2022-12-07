#Day 1 Input
 
#Get Data from File
file = open("./data_d1.txt")
input = file.readlines()
file.close()


#Data Processing
data = []
temp = []

for x in range(0, len(input)):

    line = input[x]

    if(line == "\n"):

        data.append(temp)
        temp = []

    else:
        temp.append(int(line.strip()))



#Task 1
"""
Task is to find the Elf with most Calories and what that number is

Loop through each Elf, the count the total calories for each one

"""

T1_mostCalories = 0

for elf in range(0, len(data)):

    temp_CalorieTotal = 0

    for item in range (0, len(data[elf])):

        temp_CalorieTotal = temp_CalorieTotal + data[elf][item]

    if (temp_CalorieTotal > T1_mostCalories):

        T1_mostCalories = temp_CalorieTotal


#Display Result
print("Part 1 - Total Calories:")
print(T1_mostCalories)
print()


#Task 2

"""
Task is to find the Elf with most Calories and what that number is

Loop through each Elf, the count the total calories for each one

Have a list of the top three, add the new highest to a list of three and remove the lowest in that list

"""

T2_mostCalories_List = [0, 0, 0] 

for elf in range(0, len(data)):

    temp_CalorieTotal = 0

    for item in range (0, len(data[elf])):

        temp_CalorieTotal = temp_CalorieTotal + data[elf][item]

    if (temp_CalorieTotal > T2_mostCalories_List[2]):

        T2_mostCalories_List.append(temp_CalorieTotal)
        T2_mostCalories_List.sort()
        T2_mostCalories_List.reverse()
        T2_mostCalories_List.pop(3)

#Calculate the Total of the total

superTotal = 0

for item in range(0, len(T2_mostCalories_List)):
    superTotal = superTotal + T2_mostCalories_List[item]



print("Part 2 - Top 3 Total Calories:")
print(T2_mostCalories_List)
print("Super Total of the Top 3: ", superTotal)
print()