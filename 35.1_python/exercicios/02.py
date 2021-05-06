def calculate_average(*args):
    NUMBER_OF_ARGUMENTS = len(args)
    number_sum = 0
    
    for each in args:
        number_sum += each
    
    RESULT = number_sum / NUMBER_OF_ARGUMENTS
    
    print(RESULT)
    return RESULT
    
calculate_average(16, 78, 9, 0, 34)
