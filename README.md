# home-automation

Repo for my Raspberry Pi home automation projects. The initial use case is a blind controller to shut the blinds given threshold temperature and sunlight values. Already at this early stage the project has mutated and evolved with my growing understanding. In this repo I will put all inforation relevant for setting up a Raspberry Pi, connecting it with Sensors and most importantly my (ever-changing) code.

## Setting up the Raspberry Pi

Here is a list of what I started with:
* Raspberry Pi Zero W
* Micro SD Card (with card adapter to write from Macbook Pro)
* Micro USB Cable
* USB Power Adapter with 5V 1A

Based on the tutorial from https://desertbot.io/blog/setup-pi-zero-w-headless-wifi I setup the Pi to be headless. Just in case **desertbot** no longer provides the great resource I am recapping here and adding my additional installations.

Step 1: Download a lite Raspbian image
https://www.raspberrypi.org/downloads/raspbian/

Step 2: Plug a micro SD card into your Mac
Identify the micro SD card
```
diskutil list
```

Step 3: Unmount the micro SD card
```
diskutil unmountDisk /dev/disk2
```

Step 4: Burn the image to the micro SD card
* Download Raspbian stretch since z-wave currently only supports this version
* https://z-wave.me/z-way/download-z-way/
* https://downloads.raspberrypi.org/raspbian/images/raspbian-2019-04-09/
```
sudo dd bs=1m if=~/Downloads/2019-04-08-raspbian-stretch.img of=/dev/disk2
```
This can take several minutes

Step 5: Enable ssh
```
touch /Volumes/boot/ssh
```

Step 6: Add network info
Create a new empty file for the credentials
```
touch /Volumes/boot/wpa_supplicant.conf
```
Edit country, ssid and psk
```
country=CH
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}
```

Step 7: Eject the micro SD card
```
diskutil eject /dev/disk2
```

Step 8: Boot the Pi Zero W
* Put the SD card in the Pi
* Plug a Micro-USB power cable into the port closest to the end of the board
* Give the Pi Zero plenty of time to bootup

Step 9: Login over Wifi
Open terminal and type
```
ssh-keygen -R raspberrypi.local
ssh pi@raspberrypi.local
```
* Don't worry if you get a host not found error for the first command, this just clears out any previous references to raspberrypi.local
* If the pi won't respond, press Ctrl-C and try the last command again
* If prompted with a warning just hit enter to accept the default (yes)
* Type in the password -- by default this is **raspberry**

Step 10: Configure your Pi
```
sudo raspi-config
```
* Change User Password
* Set timezone (Localisation Options)
* Enable I2C (Interfacing Options)
* Expand the file system (Advanced Options)
* Reboot once the changes are made

Step 10b: Locale Settings
If a Perl error message appears warning about locale settings, check available locales
```
locale -a
```
Then either install a new locale or check spelling of existing ones and set
```
export LANGUAGE=en_GB.utf8
export LC_ALL=en_GB.utf8
export LC_CTYPE=en_GB.utf8
export LANG=en_GB.utf8
```

Step 11: Get the updates
```
sudo apt-get update -y
sudo apt-get upgrade -y
```

Step 12: Install vim
```
sudo apt-get install vim
```
How to use vim:
* `vim filename.extension`
* [I] (to insert text)
* [esc] (to stop inserting)
* :q to quit or :wq to write & quit

Step 13: Change hostname
```
sudo vim /etc/hostname
sudo vim /etc/hosts
```
Change raspberrypi to something else

Step 14: Install I2C tools
```
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
```
Check that the tools are installed
```
sudo i2cdetect -y 1
```

Step 15: Python Settings
Raspbian comes with two versions of Python:
```
python --version
python3 --version
```
To set a specific version as default
```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
```
Now calling `python` will automatically use Python 3.7

Step 16: Cloning Github
```
sudo apt-get install git
git clone https://github.com/steinbock/home-automation.git
```

Step 17: Install pip
```
sudo apt-get install python3-pip
```

Step 18: Install Razberry for Z-Wave communication
```
wget -q -O - https://storage.z-wave.me/RaspbianInstall | sudo bash
sudo reboot
```
* http://find.z-wave.me/
* Lists ip of raspberry
* Set admin password

* Enable uart in raspy-config
* add enable_uart=1 to boot/config.txt
* add dtoverlay=pi3-disable-bt to boot/config.txt
* http://forum.z-wave.me/viewtopic.php?f=3419&t=24108#p65526
* Update firmware:
* sudo apt-get install rpi-update
* sudo rpi-update
* wget -q -O - razberry.z-wave.me/install | sudo bash
* remove plymouth.ignore-serial-consoles from boot/cmdline.txt
* reset locale after rpi-update

-> It works! 










