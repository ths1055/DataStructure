import copy

a=[1,2,3,4,5]

c=copy.deepcopy(a)

c.append(6)

print(a, c)