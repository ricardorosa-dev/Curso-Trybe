numbers = [5, 9, 3, 19, 70, 8, 100, 2, 35, 27]

def find_smaller_number(list):
    result = 0
    
    for each in range(len(list)):
        if list[each] == list[0]:
            print("{0} is the first element".format(list[each]))
            result = list[each]
        else:
            print(list[each])
            if list[each] < result:
                result = list[each]
    
    print("The smallest number is {0}, which is the item {1} of the array called list"
      .format(result, list.index(result) + 1))

find_smaller_number(numbers)
