a = [1,2,3,4,5] 
b = ['apple', 'banana', 'cherry']
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)



x = list((1,2,3,'apple',4.5))
print(x)

y = [6]*5
print(y)


z = []
z.append(10)
z.insert(0,5)
z.extend([15,20,25])
print(z)

z.clear()
print("After clear(): ", z)



p = [10,20,30,40,50]
p.remove(20)
print(p)
popped_val = p.pop(2)
print(popped_val)
print(p)

del p[1]
print(p)



q = ['apple', 'banana', 'cherry']

for item in q:
    print(item)


w = [[1,2,3],[4,5,6],[7,8,9]]
print(w[1][2])


squares = [x**2 for x in range(1,6)]
print(squares)