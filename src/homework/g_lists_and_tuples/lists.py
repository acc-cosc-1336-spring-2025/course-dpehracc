#
def get_lowest_list_value(numbers):
    lowest = numbers[0]
    for num in numbers[1:]:
        if num < lowest:
            lowest = num
    return lowest

def get_highest_list_value(numbers):
    highest = numbers[0]
    for num in numbers[1:]:
        if num > highest:
            highest = num
    return highest