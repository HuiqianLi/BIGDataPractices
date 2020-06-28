#
'''
有两个序列a,b，大小都为n,序列元素的值任意整数，无序。
要求：通过交换a,b中的元素，
使[序列a元素的和]与[序列b元素的和]之间的差最小。
例如：  a=[1,2,5,7,2,9]
        b=[5,8,3,2,1,0]
		交换a b元素，然后求abs(sum(a)-sum(b))最小
'''
a=[1,2,5,7,2,9]
b=[5,8,3,2,1,0]
new_list = a + b
new_list.sort()
mid_list = new_list[1:-1]
list1 = mid_list[::2]
list2 = mid_list[1::2]
if sum(list1) < sum(list2):
    list1.append(new_list[-1])
    list2.append(new_list[0])
else:
    list2.append(new_list[-1])
    list1.append(new_list[0])
print(list1,list2)
#print(abs(sum(a)-sum(b)))
