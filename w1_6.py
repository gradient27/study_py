import time

class TrafficLight():

    def running(self):
        cnt = 0

        def switch_color(i):
            my_color = ["Красный", "Желтый", "Зеленый"]
            my_sleep = [7, 2, 3]
            __color = my_color[i]
            __sleep = my_sleep[i]
            print(f'Светофор демонстрирует свет: {__color}')
            time.sleep(__sleep)

        while cnt < 4:
            for i in range(0, 3):
                switch_color(i)
                i += 1
                cnt += 1
        print('stop')

new_trafficLight = TrafficLight()
new_trafficLight.running()


