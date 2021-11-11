def on_forever():
    basic.clear_screen()
    led.plot(pins.map(pins.analog_read_pin(AnalogPin.P1), 0, 1023, 0, 4),
        pins.map(pins.analog_read_pin(AnalogPin.P2), 0, 1023, 0, 4))
basic.forever(on_forever)
