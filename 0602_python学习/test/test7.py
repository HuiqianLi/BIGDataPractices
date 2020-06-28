#数字配对
"""
人类的数字是：1、2、3、4、5、6、7、8、9、10、11、12、13、14、15、16、17、18、19、20、21、22、23、24、25、26、27、28、29、30。。。。。
外星人数字是：1、2、4、5、6、7、9、10、11、12、14、15、16、17、19、20、21、22、24、25、26、27、29、41、42、44、45、46、47、49。。。。。
需求：输入一个外星人数字，输出对应的人类数字，比如外星人9数字，对应人类数字7
"""
alien_str = input()
alien_num = int(alien_str)
human_list = range(1,10000)
human_list = [x for x in human_list if x != 3 or x % 10 != 8]
if alien_num == 3:
    human_num = None
elif alien_num % 10 == 8:
    human_num = None
else:
    human_num = human_list.index(alien_num) + 1
print(human_num)
