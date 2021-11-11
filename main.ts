basic.forever(function () {
    servos.P0.setAngle(pins.map(
    pins.analogReadPin(AnalogPin.P1),
    0,
    1023,
    0,
    180
    ))
})
