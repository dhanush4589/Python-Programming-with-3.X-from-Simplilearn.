# Input from user:
'''
name = input('What is your name?:')
print('Hello', name)
'''

import statistics

exList = [5,3,2,9,7,4,3,1,8,9]

x = statistics.mean(exList)
print(x)

x = statistics.median(exList)
print(x)

x = statistics.mode(exList)
print(x)

x = statistics.stdev(exList)
print(x)

x = statistics.variance(exList)
print(x)
