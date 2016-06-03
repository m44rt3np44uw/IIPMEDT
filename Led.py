from time import sleep
from threading import Thread
import RPi.GPIO as GPIO


class Led:
    def __init__(self, output_pin: int) -> None:
        self.__led_output_pin = output_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__led_output_pin, GPIO.OUT)

    def blink(self, seconds: float):
        GPIO.output(self.__led_output_pin, True)
        sleep(seconds)
        GPIO.output(self.__led_output_pin, False)
        sleep(seconds)

    def blink_in_thread(self, seconds: float):
        t = Thread(target=self.blink, args=(seconds,))
        t.start()


def main() -> None:
    led = Led(2)  # input pin
    led.blink_in_thread(1.0)

if __name__ == '__main__':
    main()
