from .tempreader import TempReader
from .fancontrol import Fan
from time import sleep

temp_max = 70
temp_min = 40
test_mode = True
fan_pin = 17


def main():
    reader = TempReader(test_mode)
    fan = Fan(fan_pin, test_mode)
    while True:
        temp = reader.read_cpu_temperature()
        print(temp)
        if (temp > temp_max and not fan.powered):
            fan.power(True)
        elif (temp < temp_min and fan.powered):
            fan.power(False)
        sleep(1)


if (__name__ == "__main__"):
    main()
