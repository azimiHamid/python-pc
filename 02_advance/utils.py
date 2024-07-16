# This is a testing module used in --> exercise_3.py

def find_max(numbers):
    
    max_num = numbers[0]
    
    for number in numbers:
        if number > max_num:
            max_num = number

    return max_num