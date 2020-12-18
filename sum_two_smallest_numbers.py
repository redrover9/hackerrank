def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    smallest_num = numbers[0]
    second_smallest_num = numbers[1]
    sum_of_two = smallest_num + second_smallest_num
    return sum_of_two
