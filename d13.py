import json

#Get Data from File
file = open("./data_d13.txt")
data = file.read().split("\n\n")
file.close()

code_pairs = []

for item in data:
    code_pairs.append(item.strip().split('\n'))


# Return values:
#   True - list(s) are in order
#   False - list(s) are out of order
def signalComapre(list_left, list_right):


    # If the left side is bigger, then it is out of order
    if(len(list_left) > len(list_right)):
        return False

    for index in range(0, max(len(list_left), len(list_right))):

        #If we have reached the end of the left side then it is True
        if(index == len(list_left) and len(list_left) < len(list_right)):
            return True

        if(index == len(list_right) and len(list_left) < len(list_right)):
            break


        # Both are ints, see that the left side is smaller
        # If not return false
        if(isinstance(list_left[index], int) and isinstance(list_right[index], int)):

            if(list_left[index] > list_right[index]):
                return False

        elif(isinstance(list_left[index], list) and isinstance(list_right[index], list)):

            # Recurse the function to work on each list
            result_0 = signalComapre(list_left[index], list_right[index])

            # If the lists are out of order then the whole thing is
            # Therefore return that it is out order
            if(not result_0):
                return False

        elif(isinstance(list_left[index], int) and isinstance(list_right[index], list)):

            if(list_right[index] == []):
                return True

            # Recurse the function to work on each list
            result_1 = signalComapre([list_left[index]], [list_right[index][0]])

            # If the lists are out of order then the whole thing is
            # Therefore return that it is out order
            if(not result_1):
                return False

        elif(isinstance(list_left[index], list) and isinstance(list_right[index], int)):

            if(list_left[index] == []):
                return False

            # Recurse the function to work on each list
            result_2 = signalComapre([list_left[index][0]], [list_right[index]])

            # If the lists are out of order then the whole thing is
            # Therefore return that it is out order
            if(not result_2):
                return False

        #Error catching

        else:
            print(type(list_left[index]))
            print(type(list_right[index]))
            print("Error")
            return False

        if(index == len(list_right) - 1):
            break

    return True


print(code_pairs[0])

indices_sum = 0

for x in range(0, len(code_pairs)):

    result = signalComapre(json.loads(code_pairs[x][0]),json.loads(code_pairs[x][1]))

    if(result):
        indices_sum = indices_sum + x + 1

    print(result)

print(indices_sum)







'''
print(signalComapre(json.loads('[[[]]]'),json.loads('[[]]')))

print(signalComapre([1,1,3,1,1],[1,1,5,1,1]))

print(signalComapre([[1],[2,3,4]],[[1],4]))

print(signalComapre([9],[[8,7,6]]))

print(signalComapre([[4,4],4,4],[[4,4],4,4,4]))

print(signalComapre([7,7,7,7],[7,7,7]))

print(signalComapre([],[3]))

print(signalComapre([[[]]],[[]]))

print(signalComapre([1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9]))

print(signalComapre([1,1,3,1,1], [1,1,5,1,1]))

print(signalComapre([[1],[2,3,4]], [[1],4]))

print(signalComapre([9], [[8,7,6]]))

print(signalComapre([], [3]))

print(signalComapre([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))

'''