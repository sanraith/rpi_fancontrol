# rpi_fancontrol

Python project to turn the fan of my Raspberry Pi 4 on-off based on its CPU temperature.

## Configure in a virtual environment

    git clone https://github.com/sanraith/rpi_fancontrol.git
    cd rpi_fancontrol
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install --editable .
    deactivate

## Run in the virtual environment

    source venv/bin/activate
    python3 -m rpi_fancontrol
    deactivate
