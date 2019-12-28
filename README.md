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
