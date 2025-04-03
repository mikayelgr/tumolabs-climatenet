from gpiozero import Button
from signal import pause

btn = Button(27)

def p():
    print(1)

def r():
    print(0)

btn.when_pressed = p
btn.when_released = r

pause()

