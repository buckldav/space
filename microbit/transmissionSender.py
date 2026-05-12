def on_button_pressed_a():
    global num
    num += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(num)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global num
    num += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

num = 0
radio.set_group(2)
num = 1

def on_forever():
    basic.show_string("" + str((num)))
basic.forever(on_forever)
