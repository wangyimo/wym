import time
import datetime
from Carproperty import *
class Manager():
    cost = 0
    def __init__(self, car_license, enter_time=0, start_time=0,end_time=0):
        #车牌号
        self.car_license = car_license
        #进入停车场时间
        self.enter_time = enter_time
        #开始停车时间
        self.start_time = start_time
        #结束停车时间
        self.end_time = end_time
        

    #停车场收费方法
    def pay_money(self):
        self.end_time = time.time()
        cost = (self.end_time-start_time)//3600*4
        #停车时间小于一小时的按照一小时算
        if self.end_time-start_time < 3600:
            print('您停车的费用是:4元')
        else:
            print(self.end_time-start_time)
            print('您停车的费用是:',cost,'元')
        

carproperty = Carproperty()
while True:
    select = input(
        '''
        请选择功能：
        1.停车
        2.出车 
        '''
    )
    if select == '1':
        license = input('输入车牌号：')
        enter_time = time.time()
        print('欢迎停车，前行开始寻找车位')
        start_time = time.time()
        print(start_time)
        carproperty.enter_park()
        carproperty.parking()
        
    elif select == '2':
        lic = input('输入车牌号：')
        carr = Manager(lic)
        carr.pay_money()
        carproperty.leave()
    else:
        print('请正确选择')
    time.sleep(2)
    continue