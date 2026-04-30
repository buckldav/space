num = 0

def on_pin_pressed_p0():
    global num
    num = randint(1, 2)
    music.play(music.string_playable("C D E F G A B - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    if num == 2:
        music.play(music.string_playable("C5 F C5 F C5 F C5 F ", 120),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_string("SICK")
    else:
        music.play(music.string_playable("C5 - C5 - C5 - C5 - ", 120),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_string("CLEAR")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_forever():
    pass
basic.forever(on_forever)
