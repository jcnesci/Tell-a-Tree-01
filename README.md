# Welcome to the Tell-a-Tree NYC project code, which was developed during ITP Camp 2013 at NYU.

It's a very simple prototype to demo the functionality of the project and it's proposed interaction.

## The concept

Trees surround us, even in the city ; the insight behind this project is that our parks have witnessed our collective history and carry memories through time of our comings-and-goings, our first dates, our secret encounters and random wanderings. 

Park-goers will come upon special birdhouses attached to trees that incite them to share a secret of theirs by speaking into them.
At another end of the park, other types of birdhouses will playback people's secrets in randomly assembled forms, unbeknownst to the one's who shared secrets. 

Like a physical version of [ PostSecret ](http://www.postsecret.com/), or maybe a pun on the magpies that might be living in the birdhouses, these objects attract and diffuse secrets throughout a park in various patterns and narrative threads depending on how they are placed among the trees, creating endless possibilities for new experiences.

This project is about bringing out these memories, and letting new ones take form by letting people connect in their most natural surroundings.

## The prototype

The idea was to create a network of Raspberry Pi's, with one master that allowed users to record audio snippets, and many slaves that could playback those recordings.

For the initial prototype that we have here, there is only 1 master (which records) and 1 slave (which does playback). The code is laughably simple, only a few lines, really. But it's a start, and it works!

### The Master

The code for the master is comprises the following:
* the 'tellatree_master.py' file
* the 'audio_recordings/' folder
* the startup script

The hardware parts:
* Raspberry Pi model B (ie. with ethernet port)
* TP-Link nano router (for a quick and easy router solution)
* Syma USB audio adapter (for recording audio input)
* 3.5mm Microphone (plugs into adapter)
* [ battery ]
* LED

### The Slave

The slave is made of the following:
* Raspberry Pi model A (ie. no ethernet port)
* [ Audio speakers ]
* [ battery ]





... IN PROGRESS


Thanks to Matt Richardson and all the other ITP Camp counselors and staff.