# The Tell-a-Tree NYC codebase

Welcome to the TAT-NYC project code, which was created during ITP Camp 2013 at NYU.

It's a very simple prototype to demo the functionality of the project and it's proposed interaction.

## The concept

Trees surround us, even in the city ; the insight behind this project is that our parks have witnessed our collective history and carry memories through time of our comings-and-goings, our first dates, our secret encounters and random wanderings. 

Park-goers will come upon special birdhouses attached to trees that incite them to share a secret of theirs by speaking into them.
At another end of the park, other types of birdhouses will playback people's secrets in randomly assembled forms, unbeknownst to the one's who shared secrets. 

Like a physical version of [ PostSecret ](http://www.postsecret.com/), or maybe a pun on magpies that might be living in the birdhouses, these objects attract and diffuse secrets throughout a park in various patterns and narrative threads depending on how they are placed among the trees, creating endless possibilities for new experiences.

This project is about bringing out these memories, and letting new ones take form by letting people connect in their most natural surroundings.

## The prototype

The idea was to create a network of Raspberry Pi's, with one master that allowed users to record audio snippets, and many slaves that could playback those recordings.

For the initial prototype that we have here, there is only 1 master (which records when the user presses a button) and 1 slave (which does playback of secrets). The code is laughably simple, only a few lines, really. But it's a start, and it works! (except a few hiccups, see below)

### How it works

All the code is in 2 python files (1 each for the master and slave Pi's).

Audio recording and playback uses the very basic ALSA linux library.
File synching between Pi's uses RSYNC over SSH.
The recording, playback, and synching commands are sent to, and run by, the linux shell using SUBPROCESS.
The code runs on startup thanks to CRON.

This could be used as a beginner level intro to: audio recording, audio playback, and synching files between two Raspberry Pi's (or any linux systems).

## Installation

Here's what you need to have on your Raspberry Pi's to make it work.

### The Master Pi

1.	put 'tellatree_master.py' in your home folder
2.	make a directory called 'audio_recordings/' in your home folder
3.	connect a push button to GPIO pin 25 on your Pi (see below)
4.	connect an led to GPIO pin 24 (see below)
5.	connect a router to your Pi's ethernet port
6.	connect a USB audio input adapter to the Pi with a 3.5mm microphone on it
7.	connect your Pi and router to power / a portable battery

### The Slave Pi

1.	put 'tellatree_slave.py' in your home folder
2.	make a directory called 'audio_playback/' in your home folder
3.	connect a push button to GPIO pin 25 on your Pi (see below)
4.	connect a USB wireless adapter to your Pi
6.	connect USB speakers to your Pi's audio jack
7.	connect your Pi and speakers to power / a portable battery

### The wireless network

Setup your wireless network for your Pi's by visiting your router's admin interface (for my mine, it's at 192.168.0.254).
I got a tiny TP-Link router (that fits nicely in my master birdhouse) that I had to first [ set up to work in AP mode ] (http://www.tp-link.com/CA/article/?id=393) (wireless access point mode). Then, I started by disabling wireless security to make my life easier for testing.
Under the Advanced Settings, I enabled the DHCP Server, then went to my router's nifty section for DHCP Address Reservation, where I added both Pi's to the list to give them static IP's (so I can always address them by the same IP's for SSH'ing and in my python code). 
(NB: giving my Pi's static IP's on the router means I don't have to make their IP's static on the Pi's themselves, which was recommended to me such as to keep them as clean as possible; it's not a big deal but it is a nice feature to have on your router!).
I set the master to 198.168.0.100 and the slave to 198.168.0.150.

### More Pi setup stuff

*	[ install the GPIO python library ] (http://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/install-python-module-rpi-dot-gpio) on boh Pi's (newer Raspbian releases should have it already though).
*	connect [ buttons ] (http://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi/bread-board-setup-for-input-buttons) and the [ LED ] (http://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/wire-leds) to GPIO pins on the Pi's (the master has a button and the LED ; the slave has only a button).
*	install rsync on both Pi's : 'apt-get install rsync'
*	[ setup ssh-key ] (https://blogs.oracle.com/jkini/entry/how_to_scp_scp_and) on your Pi's so rsync can operate without asking you for a password everytime. Do [ this ] (http://www.thegeekstuff.com/2010/04/how-to-fix-offending-key-in-sshknown_hosts-file/) too if problems arise.
*	on the Master, [ setup your USB audio adapter ] (http://asliceofraspberrypi.blogspot.ca/2013/02/adding-audio-input-device.html) to be the default recording device.

Finally, for running your python scripts on startup, do this: 
*	in Master Pi's shell: sudo bash
*	in Master Pi's shell: crontab -e
*	in crontab, comment-out everything (with '#') then add this line at the bottom: @reboot python /home/pi/tellatree_master.py
*	for the Slave, do the same but with the slave code file: @reboot python /home/pi/tellatree_slave.py

### Startup & running the Pi's

Power-up the Master first so the VPN gets running, then the Slave.
Use a laptop to connect to your wireless network over Wifi, then SSH into your Pi's in two seperate terminal windows, so you can see your Pi's print results while they're working.

Push your Master's record button; you have 10 seconds to record a message (though there are problems with that, see below). In the terminal, you should see a print result like '1- file saved: ' + the filename, and '2- rsync complete'.

Push your Slave's record button, and you should hear one of the recorded messages, and in the terminal see the audio file's name show up.

## Problems to solve

Do let me know if you have ideas for fixing the following issues:
*	the recording does works but somtimes throws this error, which probably has to do with memory management and buffer allocation:
	Recording WAVE '/home/pi/audio_recordings/test.wav' : Unsigned 8 bit, Rate 48000 Hz, Mono
	overrun!!! (at least 37.970 ms long)
*	rsync will have hiccups sometimes and not really work, although it usually does ; not too sure how to make it more stable.

## Parts list

Here are the parts I used for my two birdhouses.

For the Master:
*	[ Raspbery Pi model B ] (http://www.adafruit.com/products/998)
*	[ TP-Link TL-WR702N router ] (http://www.amazon.com/gp/product/B007PTCFFW/ref=oh_details_o01_s00_i00?ie=UTF8&psc=1)
*	[ USB audio adapter ] (http://www.amazon.com/gp/product/B007HISGRW/ref=oh_details_o02_s01_i01?ie=UTF8&psc=1)
*	[ 3.5mm microphone ] (http://www.amazon.com/Microphone-3-5MM-Ultra-Portable-plug-n-play/dp/B001D785BU/ref=pd_cp_pc_2) (didn't use this one myself though)
*	[ USB battery pack ] (https://www.sparkfun.com/products/11360)
*	[ 4GB SD card ] (http://www.amazon.com/gp/product/B0020ZDI5C/ref=oh_details_o02_s01_i00?ie=UTF8&psc=1)
*	an arcade-style push button
*	a large red LED
*	a perfboard, regular wire and jumper wires for connecting the GPIO pins to the button and LED

For the Slave:
*	[ Raspbery Pi model B ] (http://www.adafruit.com/products/1344)
*	[ USB audio speakers ] (http://www.adafruit.com/products/1363)
*	[ USB battery pack ] (https://www.sparkfun.com/products/11360)
*	[ 4GB SD card ] (http://www.amazon.com/gp/product/B0020ZDI5C/ref=oh_details_o02_s01_i00?ie=UTF8&psc=1)
*	an arcade-style push button
*	a perfboard, regular wire and jumper wires for connecting the GPIO pins to the button

## Credits
Thanks to the whole [ ITP Camp ] (itp.nyu.edu/camp2013/) crew for making it such a fostering environment and great learning experience.
Huge thanks to [ Matt Richardson ] (http://mattrichardson.com/) for helping me tackled the Raspberry Pi.
