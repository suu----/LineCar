import Adafruit_BBIO.PWM as PWM
import time

PWM.start("P9_22", 100)

for i in range(100, 0, -1):
        PWM.set_duty_cycle("P9_22", i) # Passing duty cycle as an int
        time.sleep(.1)

PWM.stop("P9_22")
PWM.cleanup()