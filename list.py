'''
a = ['nnn', 67, 7.8, True]
h = [9]
a.extend(h)
print(a)
a.pop(2)
print(a)
print(a.index(67))
'''
#0
'''
a=[]
b=((1, 2.1), (True, '12', 8.9))
a.extend(b)
print(a)
'''
#1
'''
a=(1, 2.3, True)
print(a[::])
'''

#2
'''
a=[1, 2.3, True, 'hi', (5.5, False)]
print(a)
'''

#3
'''
a=['Askar', 'Aidar', 'Ansar', 'Aman','Asyl']
b=' '
print(b.join(a))
'''
#4
'''
a=[1, 5.5, True, 'hi']
b=[False, 7.7, 'by']
a.extend(b)
print(a)
'''
#5
'''
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(names.count('Jack'))
'''
#6
'''
names = ['Oskar', 'Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
names.remove('Oskar')
print(names)
'''

#7
'''
a=[]
b=['Askar', 1991, 'Python']
a.extend(b)
print(a)
'''

#8
'''
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList.index('loop'))
print(pythonList.pop(6))
print(pythonList)
'''

#9
'''
numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
a=str(numbers)
b=input()
print(b.join(a))
'''
#10

s = ['Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23]
num = []
let = []
if type(s[0])==str:
	let.append(s[0])
elif type(s[0])==int:
	num.append(s[0])
if type(s[0])==str:
        let.append(s[0])
elif type(s[0])==int:
        num.append(s[0])
if type(s[0])==str:
        let.append(s[0])
elif type(s[0])==int:
        num.append(s[0])
if type(s[0])==str:
        let.append(s[0])
elif type(s[0])==int:
        num.append(s[0])
if type(s[0])==str:
        let.append(s[0])
elif type(s[0])==int:
        num.append(s[0])
if type(s[0])==str:
        let.append(s[0])
elif type(s[0])==int:
        num.append(s[0])
