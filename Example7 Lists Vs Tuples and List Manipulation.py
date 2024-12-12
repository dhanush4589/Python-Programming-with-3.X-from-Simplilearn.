def example():
    return 15,19

a,b = example()

print(a)
print(b)

x = [6,2,3,6,8,9,4,3]

print(x)
print(x[5])

x.append(12)
print(x)

x.insert(5,7)
print(x)

x.remove(7)
print(x)

print(x.index(12))

print(x.count(3))

x.sort()
print(x)

x = ['Spot','Cam','Jan','Dave','Zack']

print(x)
x.sort()
print(x)

x.reverse()
print(x)
