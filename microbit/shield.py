def on_received_number(receivedNumber):
    if receivedNumber == 4:
        music.set_volume(255)
        music.play(music.string_playable("F C F C F C F C ", 155),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        basic.show_leds("""
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            . . . . .
            """)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    music.stop_all_sounds()
    basic.show_leds("""
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

radio.set_group(1)
basic.show_leds("""
    . # . # .
    . . . . .
    # . . . #
    . # # # .
    . . . . .
    """)
