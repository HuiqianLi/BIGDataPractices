from crawler import Bilibili_Uvideo
import time
from getMid import read_csv
import random

def read_breakpoint():
        file = open('save.data', 'r')
        return file.read()

# mids = read_csv('hundred_ups.csv')['mid']
# mids = list(mids)
# mids = mids[int(read_breakpoint()):]
# count = 0
# for mid in mids:
#     count += 1
# print(count)

mids = read_csv('hundred_ups.csv')['mid']
mids = list(mids)
now_mids = mids[int(read_breakpoint()):]
for mid in now_mids:
    B_c = Bilibili_Uvideo(mid)
    # dump csv
    for i in range(B_c.getTotal_page()):
        try:
            B_c.reverse_page(i+1)
        except:
            # print(B_c.up_name)
            # print(i+1)
            B_c.generate_breakpoint(str(list(mids).index(mid)))
            break
        time.sleep(random.randint(100,200)/100)
    print(B_c.up_name + " Finish!")
    B_c.save_as_csv()
# B_c = Bilibili_Uvideo(mids[1])
# # dump csv
# for i in range(B_c.getTotal_page()):
#     B_c.reverse_page(i+1)
#     time.sleep(1)
# B_c.save_as_csv()