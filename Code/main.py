from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.direct import DirectPins
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())
import oled

keyboard = KMKKeyboard()

keyboard.matrix = DirectPins(
    pins=(1, 2, 3, 4),
    pull=True
)

keyboard.keymap = [
    [KC.PSCR, KC.MEDIA_NEXT_TRACK, KC.MEDIA_STOP, KC.BSPC]
]

encoder = EncoderHandler()
encoder.pins = ((8, 9),)
encoder.map = [(KC.VOLD, KC.VOLU)]
keyboard.modules.append(encoder)

def oled_update(keyboard):
    oled.show_text("RUNNING")

keyboard.after_matrix_scan.append(oled_update)

if __name__ == '__main__':
    oled.show_text("READY")
    keyboard.go()

#fingers crossed the code works on first flash