from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO


class LED:
    def __init__(self, pin_number, color):
        self.pin_number = pin_number
        GPIO.setup(self.pin_number, GPIO.OUT)
        self.color = color
        self.state = False

    def toggle(self):
        if self.state:
            self.state = False
            GPIO.output(self.pin_number, GPIO.LOW)
        else:
            self.state = True
            GPIO.output(self.pin_number, GPIO.HIGH)

        print(f'{self.color}: {self.state}')


app = Flask(__name__)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

green = LED(18, 'green')
red = LED(17, 'red')
blue = LED(19, 'blue')

leds = [green, red, blue]

@app.route('/toggle/<pin_number>')
def toggle(pin_number):
    target_led = None
    for led in leds:
        if led.pin_number == int(pin_number):
            target_led = led
    
    if target_led:
        target_led.toggle()

    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', 
                           leds=leds)


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0')
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(0)

