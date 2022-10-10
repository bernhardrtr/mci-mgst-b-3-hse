import utime

from lib import HCSR04


sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print(f"Distance: {distance} cm")
    utime.sleep_ms(1000)
