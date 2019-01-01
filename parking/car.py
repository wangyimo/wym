#车类
class Car():
    def __init__(self,car_license,model,displacemeng,brand,color):
        #车牌号
        self.car_license = car_license
        #车型号
        self.model = model
        #车排量
        self.displacemeng = displacemeng
        #车品牌
        self.brand = brand
        #车颜色
        self.color = color

    def start_park(self):
        print('开始停车')

    def end_park(self):
        print('结束停车')
        