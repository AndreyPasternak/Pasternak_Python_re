class Light:
    color = 'red'
    def __init__(self, color_2, color_3, color_1=color):
        self.color_2 = color_2
        self.color_3 = color_3
        self.color_1 = color_1

running = Light('yellow', 'green', 'red')
print(type(running))
print(running.color_1)
import time
sec = 0
while True:
    print(sec)
    time.sleep(1)
    sec +=1
    if sec == 7:
        print(running.color_2)
    elif sec == 9:
        print(running. color_3)
    elif sec == 16:
        print(running.color_1)
        break