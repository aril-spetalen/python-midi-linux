# A note on how to get started with python MIDI scripts on a linux platform

## Abstract

I wanted to script [MIDI](https://midi.org/) control instructions with python, allowing my linux machine control my old el-piano. It wasn't as easy as I expected to get things to play. Here's a tale of my long and winding road (that is: a days reading and hacking), to something which worked.

## Prerequisites

* a musical instrument with a MIDI interface (I have an old el-piano with old fashioned 5 pin MIDI plugs)
* MIDI cable (I ran out and bought a Roland UM ONE mk2, the cheapest USB - MIDI adapter I found)
* a linux laptop (ubuntu 20.04)
* python v3

## Python modules and linux add ons

*  To allow python interface with MIDI, a modification of the operating system is required. It is called [Advanced Linux Sound Architecture (ALSA)](https://www.alsa-project.org/wiki/Main_Page) and is fairly straight forward to get this in place. (`sudo apt install libasound2`).
* There is a huge load of python MIDI binding modules, however I struggled for hours finding something which worked on my machine. I had success with **[alsa-midi](https://pypi.org/project/alsa-midi/).** These are a bunch of libraries with which I failed (for some reason or the other - they obviously work for others):
  * [pygame.midi](https://www.pygame.org/docs/ref/midi.html)  (though it seems widely adopted)
  * [PyAlsaAudio](https://github.com/larsimmisch/pyalsaaudio)
  * [pyalsa](https://github.com/MaurizioB/Bigglesworth/blob/master/bigglesworth/alsa.py)
  * [py-midi](https://pypi.org/project/py-midi/)
  * [mido](https://github.com/mido/mido) (though this also seems widely adopted)

## The best blogs

[Ted's Linux MIDI Guide](http://tedfelix.com/linux/linux-midi.html) was my favourite. This most useful text helped me get things to play. I strongly recommend to start here, if you want to get a linux system up and running with [MIDI](https://midi.org/). It helps you get ALSA up and running, includes instructions on [jack](https://jackaudio.org/) (I skipped that), and has instructions on [vmpk](https://vmpk.sourceforge.io/), which is a nice virtual MIDI keyboard.

[Making a Synth with Python](https://python.plainenglish.io/build-your-own-python-synthesizer-part-3-162796b7d351)  is an other blog which has good descriptions on how to make a synth with python and MIDI. (I did not get the mentioned python libraries into play, but the text was still very instructive and well written).

With alsa and the command line tool "aplaymidi" in place, and a MIDI connection to my piano, I could play MIDI musical files ([find examples for classical piano here](http://www.piano-midi.de/)) like this: 

* call `aplaymidi -l` to list all MIDI connections known by ALSA. On my machine the output tells 20:0 is the port where my piano is connected. Then:
* call `aplaymidi -p 20:0 alb_se5_format0.mid`, and listen to "Concerto Aranjuez" MIDI file being played on / by my piano.

## Conclusion, result and next steps

The attached script is the very simple, yet most advanced script I managed get into play after a days struggle to make a python script control my piano over MIDI.

A goal for this, was to try making my reMarkable tablet act as a MIDI controller for my piano. I didn't get there, but a possible way to get it working might be to let instructions on reMarkable send events which in sequence could trigger MIDI events in a linux python script like in this.