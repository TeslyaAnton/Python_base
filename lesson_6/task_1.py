from time import sleep

class Traffic_Light:
    __color = 'Pink'

    def switching(self):
        while True:
            print('Attention is red now')
            sleep(7)
            print('Attention is yellow now')
            sleep(2)
            print('Attention is green now')
            sleep(7)
            print('Attention is yellow now')
            sleep(2)

traffic_light = Traffic_Light()
traffic_light.switching()