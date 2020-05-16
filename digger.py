from gpiozero import Motor
from time import sleep

class Digger:
    right_track = Motor(14,15)
    left_track = Motor(17,18)
    arm1 = Motor(27,22)
    arm2 = Motor(23,24)
    grabber = Motor(9,10)
    body = Motor(25,8)
	
	def stop():
		right_track.stop()
		left_track.stop()
		arm1.stop()
		arm2.stop()
		grabber.stop()
		body.stop()
    
    def test(self, m):
        m.forward()
        sleep(0.5)
        m.backward()
        sleep(0.5)
        m.stop()
        print("done")

