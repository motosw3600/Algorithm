from collections import Counter

t_list = [1, 1, 1, 2, 2, 3, 4]

c_list = Counter(t_list)
print(c_list)

cm_list = Counter(t_list).most_common()
print(cm_list)
