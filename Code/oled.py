import board
import busio
import displayio
import adafruit_ssd1306
from adafruit_display_text import label
import terminalio

displayio.release_displays()

I2C_SDA = board.GP5
I2C_SCL = board.GP6

i2c = busio.I2C(scl=I2C_SCL, sda=I2C_SDA)

while not i2c.try_lock():
    pass
i2c.unlock()

display_bus = displayio.I2CDisplay(i2c,device_address=0x3C)
display = adafruit_ssd1306.SSD1306(display_bus,width=128,height=32)
text = label.Label(terminalio.FONT,text="BOOTING...",color=0xFFFFFF,x=0,y=16)

group = displayio.Group()
group.append(text)
display.show(group)

_last = None

def show_text(msg):
    global _last
    if msg != _last:
        text.text = msg
        _last = msg

def show_layer(layer):
    show_text(f"Layer: {layer}")


# still have to add animation and more functionalties after i get the display