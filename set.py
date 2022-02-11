#0
'''
a = {3,10,11,13,31,21,1,10,3,5,6,6}
a.remove(3)
print(a)
'''
#1
'''
a = {"dog", "cat", "mouse", "sheep"}
b = {"cow", "horse", "donkey", "cat", "dog"}
c = a.intersection(b)
print(c)
'''
#2
'''
a = {"dog", "cat", "mouse", "sheep"}
b = {"cow", "horse", "donkey", "cat", "dog"}
j = a.difference(b)
print(j)
'''
#3
'''
a={1, 1.2, 'jack', 'hi',5}
a.add('python')
print(a)
print(a.pop())
print(a)
'''
#000
'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'besh_barmak':130})
print(menu)
menu.update({'borsh':135})
print(menu)
print(menu.pop('borsh'))
print(menu)
'''

#10
'''
menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'drinks':['Coca-Cola', 'Sprite', 'Fanta']})
print(menu)
'''

#011
'''
a = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
a.remove('Suriname')
print(a)
'''
#020

a={'add', 'remove', 'clear','update', 'difference', 'discard','intersection', 'intersection_update','pop'}
b={'clear','keys','items','get','values','update'}
c=a.intersection(b)
print(c) 
