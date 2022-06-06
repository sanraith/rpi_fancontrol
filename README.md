# rpi_fancontrol

Python module to turn the fan of a Raspberry Pi on-off based on its CPU temperature.

## Configure in a virtual environment

`requirements-rpi.txt` only have to be installed on the Raspberry Pi.

    git clone https://github.com/sanraith/rpi_fancontrol.git
    cd rpi_fancontrol
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements-rpi.txt
    pip install --editable .
    deactivate

## Run in the virtual environment

Edit parameters in `__main__.py`.

    source venv/bin/activate
    python3 -m rpi_fancontrol
    deactivate

## Notes for running on x64 Ubuntu instead of Raspbian

- To use python, might need to `sudo apt install python3-dev`
- To use venv, might need to `sudo apt install python3.9-venv`
- To use vcgencmd, might need to `sudo apt install libraspberrypi-bin`
- To install raspberry specific requirements, use this command instead:  
`env CFLAGS="-fcommon" pip install -r requirements-rpi.txt`
- The temp reader command is located in `/usr/bin/vcgencmd` instead of `/opt/vc/bin/vcgencmd`. Update `tempreader.py` if needed.
- To run at system boot, use ```crontab -e``` to edit your cron and add line ```@reboot /path/to/script```.
