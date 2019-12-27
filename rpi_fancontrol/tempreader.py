import re
import random
import subprocess
from time import sleep


class TempReader:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode

    def read_cpu_temperature(self):
        return self._get_cputemp(self._run_measurement())

    def _get_cputemp(self, str):
        tempstr = re.search(r"[0-9]+.[0-9]+", str).group()
        return float(tempstr)

    def _run_measurement(self):
        if (self.test_mode):
            random_temperature = random.uniform(30, 81)
            return "temp=%f'C" % random_temperature
        else:
            process = subprocess.Popen(
                "/opt/vc/bin/vcgencmd measure_temp", stdout=subprocess.PIPE, shell=True)
            (output, err) = process.communicate()
            return output
