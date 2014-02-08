WiPi
====

An easy way to find and setup wifi on a Raspberry Pi. 

###Installation

Add `wipi_service.py` and `wipiserver.py` to your startup: 
    
    sudo crontab -e

    @reboot python /home/pi/greenwater/wipi_service.py &
    @reboot python /home/pi/wipiserver.py &

###Usage

Whenever your RPi starts up, it will start a Bonjour client. Use a Bonjour browser (Google this) to get the IP address of your browser, then go to `http://<your IP>:8880/form`, fill our your SSID and password and reboot your RPi. 
