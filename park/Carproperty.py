class Carproperty():
    #车的型号
    model = 'SUV'
    #排量
    displacemeng = '1.6L'
    #车的品牌
    brand = 'Benz'
    #车的颜色
    color = 'orange'
    #车主联系方式
    information = '15967899999'

    #进入停车场
    def enter_park(self):
        print('欢迎停车，前行开始寻找车位')

    #开始停车
    def parking(self):
        print('停车成功')
    
    #离开停车场
    def leave(self):
        print('您已交钱')
        print('一路顺风')

