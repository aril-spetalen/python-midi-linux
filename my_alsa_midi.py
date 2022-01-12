""" This script sends key events to a connected MIDI instrument with the use of alsa_midi.
    ALSA is a set of linux MIDI bindings, and alsa_midi is a python module using it. """
import time
from alsa_midi import SequencerClient, READ_PORT, NoteOnEvent, NoteOffEvent

CLIENT = SequencerClient("my client")
PORT = CLIENT.create_port("output", caps=READ_PORT)
DEST_PORT = CLIENT.list_ports(output=True)[0]
PORT.connect_to(DEST_PORT)



def play_one_note(note=64, velocity=34):
    """ Play a single key on your instrument """
    event1 = NoteOnEvent(note=note, velocity=velocity, channel=0)
    CLIENT.event_output(event1)
    CLIENT.drain_output()
    time.sleep(0.25)

    event2 = NoteOffEvent(note, channel=0)
    CLIENT.event_output(event2)
    CLIENT.drain_output()

def play_scale():
    """ Play a major scale on your instrument """
    play_one_note(60, 34)
    play_one_note(62, 34)
    play_one_note(64, 38)
    play_one_note(65, 42)
    play_one_note(67, 46)
    play_one_note(69, 48)
    play_one_note(71, 43)
    play_one_note(72, 38)

play_scale()
