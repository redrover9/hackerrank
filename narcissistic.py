def narcissistic(value):
    digits = []
    value = str(value)
    for i in value:
        digits.append(i)
    num_digits = len(digits)
    num_digits = int(num_digits)
    num_sum = 0
    for j in digits:
        j = int(j)
        tmp = j ** num_digits
        num_sum += tmp
    if num_sum == int(value):
        return True
    else:
        return False

narcissistic(153)
