'''some more string methods'''
# 1 istitle
# x='The Python'
# print(x.istitle()) #true
y='the python'
# print(y.istitle()) #false

#2 isupper
# z='GREEN'
# print(z.isupper()) #true
# a='PyTHOn'
# print(a.isupper()) #false

#3 join 
# x=('harry', 'jhon', 'ram')
# print('hello'.join(x)) #harryhellojhonhelloram

#4 ljust
# v='python'
# print(v.ljust(10), 'is a coding language.') #python     is a coding language.

#5 lower
# z='PyThon'
# print(z.lower()) #python

#6 lstrip
# c='     visualcode    '
# print(c.lstrip() ,'is good for coding' ) #visualcode     is good for coding

# #7 maketrans
# x='hello world'
# print(x.maketrans('l','w')) #{108: 119}

#8 
# x=' i love programming'
# print(x.partition('i')) #(' ', 'i', ' love programming')

#9
# c='i love cars'
# print(c.replace("cars", "bikes")) #i love bikes

#10
# z='python is my coding world'
# print(z.rfind('my')) #10

#11
# z='python is my coding world'
# print(z.rindex('is')) #7

#12
# x="I could eat bananas all day, bananas are my favorite fruit"
# print(x.rpartition('day')) #('I could eat bananas all ', 'day', ', bananas are my favorite fruit')

#13
# z='java, python, logi'
# print(z.rsplit(',')) #['java', ' python', ' logi']

#14
# c='     visualcode    '
# print(c.rstrip() ,'is good for coding' ) #     visualcode is good for coding

#15
# z="welcome to the zoo"
# print(z.split()) #['welcome', 'to', 'the', 'zoo']

#16
# k="Thank you for the music\nWelcome to the jungle"
# print(k.splitlines()) # ['Thank you for the music', 'Welcome to the jungle']

#17
# a='hello, myself ai'
# print(a.startswith('hello')) #true

#18
# z='pYThoN'
# print(z.swapcase()) #PytHOn

#19
# k='visualcode'
# print(k.title()) #Visualcode

#20
# g= 'logitech'
# print(g.upper()) # LOGITECH

#21
# x='100'
# print(x.zfill(10)) #0000000100