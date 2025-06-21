class phone:
    def __init__(self):
        print("This is the constructor of phone class")
        self.screen_size = 6.7
        self.battery = 5000
        self.front_camera = 20
        self.rear_camera = 120

    def zoom(self,zoom):
        print(f"Zoom level is {zoom}")




s23_ultra = phone()
print(f"Screen size :{s23_ultra.screen_size}")
print(f"Battery size : {s23_ultra.battery}")
print(f"Front camera magapixel : {s23_ultra.front_camera}")
print(f"Rear camera magapixel : {s23_ultra.rear_camera}")

s23_ultra.zoom(10)
s23_ultra.zoom(50)
s23_ultra.zoom(100)