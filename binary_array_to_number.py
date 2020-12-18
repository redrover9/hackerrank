def binary_array_to_number(arr):
    arr.reverse()
    print(arr)
    tmp = 1
    final_num = 0
    for i in arr:
        if i == 1:
            final_num += tmp
        tmp = tmp * 2
    return final_num

print(binary_array_to_number([0,0,0,1]))
