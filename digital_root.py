def digital_root(n):
    tmp = 0
    num_list = ([char for char in str(n)])
    if len(num_list) == 1:
        return n
    else:
        for i in num_list:
            tmp += int(i)
        n = tmp
        return(digital_root(n))
