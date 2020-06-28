print("hello","world","!",sep='-',end='/')

classmates = ['Michael','Bob',"Tracy"]
print('classmates:',len(classmates))
#len:取对象的长度
#print('str:',len('owfj))

#list取值：索引从0开始
print('[0]:',classmates[0])
print('[len(classmates)-1]',classmates[len(classmates)-1])
print('[-1]:',classmates[-1])

#dic
grades = {
    'Michael': 95, 
    'Bob': 75, 
    'Tracy': 85
}

print('grades:',grades)
print('Michael:',grades['Michael'])

grades['Tom'] = 60
grades['Jerry'] = 99

print('grades:',grades)

print(grades.get('Tome','该属性不存在'))

#if语句
age = 20
if age<0:
    print('error')
elif age<=18:
    print('未成年')
elif age<=40:
    print('壮年')
elif age<=60:
    print('中年')
else:
    print('老年')

# Java中的foreach
# for(String str : strs){}
#for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name,'在names中的位置:',names.index(name))

path = 'fsaddddfvfvsaergywtnsjjqgbq'
for str in path:
    print(str,'在path中的位置:',path.index(str))

print(abs(100.1))

pass

