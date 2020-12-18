def find_short(s):
    s = s.split(' ')
    l = 1000
    for i in s:
        tmp = len(i)
        if tmp < l:
            l = tmp
    return l # l: shortest word length
