dic = {'a': 2, 'b': 5, 'c':8, 'd': 4}

print(sorted(dic.items(), key= lambda x: (-x[1], x[0])))