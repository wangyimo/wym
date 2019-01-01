import time
from owner import Owner
from car import Car
from record import Record
from order import Order
from carport import Carport

#管理测试类
class Manage():
    while True:
        select = input(
            '''
            请选择功能：
            1.停车
            2.出车 
            '''
        )
        if select == '1':
            #车主进入停车场
            owner1 = Owner('7','18973678899')
            owner1.enter_carport()
            Car.car_license = input('让我记录您的车牌号：')
            #记录进入停车场时间
            record1 = Record(Car.car_license,'','','','')
            record1.enter_time = time.time()
            print('进入停车场时间是：',record1.enter_time)
            #开始停车
            car1 = Car(Car.car_license,'suv','1.6l','Benz','black')
            car1.start_park()
            #记录开始停车时间
            record1.start_time = time.time()
            #开始停车时间
            print('开始停车时间是：',record1.start_time)
            #剩余车位
            Carport.surplus -= 1
            print('剩余车位：',Carport.surplus)

        elif select == '2':
            #停止停车
            car1.end_park()
            car1.end_park()
            #记录停止停车时间
            record1.end_time = time.time()
            #计算停车时间
            delta_T = record1.end_time - record1.enter_time
            #停车时间小于一小时按一小时计算
            if delta_T < 3600:
                print('您需交停车费4元')
                Order.cost = 4
                owner1.pay_money()
                #车主离开停车场
                owner1.leave_carport()
                #记录出停车场时间
                record1.leave_time = time.time()
            else:
                Order.cost = delta_T//3600*4
                print('您需交停车费',Order.cost,'元')
                owner1.pay_money()
                owner1.leave_carport()
                record1.leave_time = time.time()
            Carport.surplus += 1
            print('剩余车位：',Carport.surplus)
        else:
            print('请正确选择')
        time.sleep(2)
        continue
