from gpiozero import Button, TonalBuzzer
from time import sleep
from gpiozero.tones import Tone

button = Button(11)
buzzer = TonalBuzzer(13)

tempo = 100
whole_note = (6000*4) / tempo

#Notes
C4 = Tone(261.63)
D4 = Tone(293.66)
E4 = Tone(329.63)
F4 = Tone(349.23)
G4 = Tone(392.00)
A4 = Tone(440.00)
B4 = Tone(493.88)

button.wait_for_press()
print('pressed')
buzzer.play(C4)