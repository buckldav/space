def on_received_number(receivedNumber):
    music.play(music.string_playable("A - A - A - A - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("A - A - A - A - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    if receivedNumber == 1:
        basic.show_string("QUUX A D OANWM? FN A OANWM")
        basic.show_string("QUUX A D OANWM? FN A OANWM")
        basic.show_string("QUUX A D OANWM? FN A OANWM")
    if receivedNumber == 2:
        basic.show_string("OT MGIL?")
        basic.show_string("OT MGIL?")
        basic.show_string("OT MGIL?")
    if receivedNumber == 3:
        basic.show_string("ZH PHHW! IULHQGV!")
        basic.show_string("ZH PHHW! IULHQGV!")
        basic.show_string("ZH PHHW! IULHQGV!")
    if receivedNumber == 4:
        basic.show_string("KIV HMS? AP SIX QWCIYIM?")
        basic.show_string("KIV HMS? AP SIX QWCIYIM?")
        basic.show_string("KIV HMS? AP SIX QWCIYIM?")
    if receivedNumber == 5:
        basic.show_string("NK STY KWNJSI, JSJRD?")
        basic.show_string("NK STY KWNJSI, JSJRD?")
        basic.show_string("NK STY KWNJSI, JSJRD?")
    if receivedNumber == 6:
        basic.show_string("SKMPC GZIUC. KB THEJB VRA. RL VRX TLTOSK MTHEGB.")
        basic.show_string("SKMPC GZIUC. KB THEJB VRA. RL VRX TLTOSK MTHEGB.")
        basic.show_string("SKMPC GZIUC. KB THEJB VRA. RL VRX TLTOSK MTHEGB.")
    if receivedNumber == 7:
        basic.show_string("ZV DL MYPLUKZ! NVVK. DL TLLA UVD!")
        basic.show_string("ZV DL MYPLUKZ! NVVK. DL TLLA UVD!")
        basic.show_string("ZV DL MYPLUKZ! NVVK. DL TLLA UVD!")
    if receivedNumber == 8:
        basic.show_string("WZ YNQYY VS SOZQ DZN WZ YCQO HOCRSIR WZ IMNCVRF DZN AG HWA ITFF EGKK ADFES [NUBWFSXBRQMU DVPR] IXSH RCUZ CFZZ DZN YAVO CSMAVM BEUD HYA JUNPGB LNOTUH FTQKHONWR")
        radio.set_group(1)
        radio.send_number(4)
        radio.send_number(5)
        radio.set_group(2)
radio.on_received_number(on_received_number)

radio.set_group(2)

def on_forever():
    pass
basic.forever(on_forever)
