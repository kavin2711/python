l1 = [1, 2, 3, 4, 5]
reversed_list = []
for i in l1:
    reversed_list = [i] + reversed_list
print(reversed_list)