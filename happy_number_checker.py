def happy_number(num):
    is_happy_number = False
    sum_squares = 0
    num = [digit for digit in str(num)]
    for digit in num:
        digit = int(digit)
        digit *= digit
        sum_squares += digit
    try:
        happy_number(sum_squares)
        if sum_squares == 1:
            is_happy_number = True
            print(is_happy_number)

    except RecursionError:
        print(is_happy_number)


happy_number(12356)
