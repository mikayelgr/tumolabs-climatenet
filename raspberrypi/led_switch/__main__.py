from gpiozero import LED, Button
from signal import pause
from dataclasses import dataclass

led = LED(17)
button = Button(27)

@dataclass
class LightSwitch:
    state: int = 0

    @classmethod
    def toggle(self):
        if self.state == 0:
            led.on()
        else:
            led.off()

        self.state = not self.state


button.when_pressed = LightSwitch.toggle

pause()
