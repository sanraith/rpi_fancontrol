from gpiozero import CPUTemperature, LED


class Fan():
    def __init__(self, fan_pin, test_mode=False):
        self.test_mode = test_mode
        self._powered = None
        if (not test_mode):
            self._fan = LED(fan_pin)

    @property
    def powered(self):
        return self._powered

    def power(self, on):
        self._powered = on
        if (not self.test_mode):
            self._fan.value = 1 if on else 0
        if (on):
            print("Turning fan on")
        else:
            print("Turning fan off")
