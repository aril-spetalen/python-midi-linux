import time
from alsa_midi import SequencerClient, READ_PORT, NoteOnEvent, NoteOffEvent

client = SequencerClient("my client")
port = client.create_port("output", caps=READ_PORT)
dest_port = client.list_ports(output=True)[0]
port.connect_to(dest_port)

def play_one_note(note=64, velocity=34):
    event1 = NoteOnEvent(note=note, velocity=velocity, channel=0)
    client.event_output(event1)
    client.drain_output()
    time.sleep(0.25)

    event2 = NoteOffEvent(note, channel=0)
    client.event_output(event2)
    client.drain_output()

def play_scale():
    play_one_note(60, 34)
    play_one_note(62, 34)
    play_one_note(64, 38)
    play_one_note(65, 42)
    play_one_note(67, 46)
    play_one_note(69, 48)
    play_one_note(71, 43)
    play_one_note(72, 38)

play_scale()
