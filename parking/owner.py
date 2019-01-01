import time
#车主类
class Owner():
    def __init__(self,name,contact_way):
        self.name = name
        self.contact_way = contact_way

    #进入停车场
    def enter_carport(self):
        print('欢迎进入pp停车场，前行开始寻找车位')

    #结账
    def pay_money(self):
        print('你已付钱')
        
        
    #离开停车场
    def leave_carport(self):
        print('一路顺风')
        leave_time = time.time()
        print('离开时间',leave_time)
