def namelist(names):
    str = ''
    if len(names) != 0:
      arr = []
      for i in range(0, len(names) - 1):
          arr.append(names[i]['name'])
      str = ', '.join(arr)
      str += ' & ' + names[-1]['name'] if str != '' else names[-1]['name']
     
    return str
