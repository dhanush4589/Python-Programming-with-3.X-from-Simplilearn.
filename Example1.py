x = 2
y = 7
z = 10

if x > y:
    print(x, 'is greater than', y)
if x < y:
    print(x, 'is less than', y)
if x == y:
    print(x, 'is the same as', y)

# cannot do this:
# if x < '2':
# print(x, 'is less than 2')

if x <= y:
    print(x,'is less than or equal to', y)

if z > y > x <= z > y:
    print(z,'is greater than',y,'which is greater than',x)
    
# if else Statements

x = 6
y = 13

if x < y:
    print(x,'is less than',y)
if x > y:
    print(x,'is greater than',y)
else:
    print(x,'is not less than',y)

# If Elif Else Statements

x=3
y=7
z=10

if x<y and x<z:
    print('something here was the case')
elif x<z:
    print(x,'is less than',z)
elif y<z:
    print(y,'is less than', z)
else:
    print('nothing was the case')

# Functions

def example():
    x = 1
    y = 3
    print(x+y)

    if x < y:
        print(x,'is less than',y)

def main():
    example()

# Function Parameters

def website(font='TNR', background_color='white'):

    print('font:',font)
    print('bg:',background_color)
    print('Font size:',font_size)
    print('Font color:',font_color)

website('TNR', 'Grey')

# Global and Local Variables

x=6

def example3():
    global x
    x += 1
    print(x)

def example():
    z=5
    print(z)

def example2():
    z=7
    print(z)
    y=x+1
    print(y)
    return y

x=example2()
print(x)

# Writing to a File

writeMe = 'Example text'
saveFile = open('exampleWrite.txt','w')
saveFile.write(writeMe)
saveFile.close()

# Appending to a File

appendMe = 'even more text'

saveFile = open('exampleFile.txt','a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()

