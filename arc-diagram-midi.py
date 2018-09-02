
from mido import MidiFile

from arc_diagram import plot_arc_diagram


midi_file = 'midis/ravel_bolero_piano.mid'
plot_title = "Bolero (Ravel)"

# midi_file = 'midis/fuer_elise.mid'
# plot_title = "Für Elise (Beethoven)"

plot_arc_diagram(stringify_notes(midi_file, 1), plot_title)


def stringify_notes( midi_file, track_number ):

    mid = MidiFile(midi_file)
    track_notes = {}
    for i, track in enumerate(mid.tracks):
        track_notes[i] = ''
        for msg in track:
            if( msg.type == 'note_on'):
                track_notes[i] += str(msg.note) +'n'
            if( msg.type == 'note_off'):
                track_notes[i] += str(msg.note) +'f'
    return track_notes[track_number] 