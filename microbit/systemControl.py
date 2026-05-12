def on_button_pressed_a():
    radio.send_number(5)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(4)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
