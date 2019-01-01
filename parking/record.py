#停车记录类
import time

class Record():
    name = 'pp停车场'
    def __init__(self, car_license, enter_time=0, start_time=0,end_time=0,leave_time=0):
        #车牌号
        self.car_license = car_license
        #进入停车场时间
        self.enter_time = enter_time
        #开始停车时间
        self.start_time = start_time
        #结束停车时间
        self.end_time = end_time
        #离开停车场时间
        self.leave_time = leave_time

    #计时
    def timer(self):
        park_time = (self.end_time-self.start_time)//3600
        print('停车时间是',park_time)