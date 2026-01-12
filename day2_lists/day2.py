lst = [1, 2,3,4,5,6,7,8,9,3]
contains = 2 in lst
index = lst.index(2)
print(contains, index)
print(lst.count(3))
lst.sort(reverse=True)
print(lst)

print(sorted(lst))


lst2 = lst[:]
lst2[0] = 10000
print(lst, lst2)
