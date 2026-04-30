def on_received_number(receivedNumber):
    music.play(music.string_playable("A - A - A - A - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("A - A - A - A - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    if receivedNumber == 1:
        basic.show_string("DO A BACKFLIP")
        basic.show_string("DO A BACKFLIP")
        basic.show_string("DO A BACKFLIP")
        basic.show_string("DO A BACKFLIP")
        basic.show_string("DO A BACKFLIP")
    if receivedNumber == 2:
        basic.show_string("HOWDY HEY GANG")
        basic.show_string("HOWDY HEY GANG")
        basic.show_string("HOWDY HEY GANG")
        basic.show_string("HOWDY HEY GANG")
        basic.show_string("HOWDY HEY GANG")
radio.on_received_number(on_received_number)

radio.set_group(2)

def on_forever():
    pass
basic.forever(on_forever)
