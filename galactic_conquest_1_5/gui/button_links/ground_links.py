from galactic_conquest_1_5.gui.button_functions.ground_button_functions import move_to_outbound, move_to_garrison


def ground_links(file, _ui):
    _ui.outboundGround_Button.clicked.connect(lambda: move_to_outbound(file))
    _ui.garrisonGround_Button.clicked.connect(lambda: move_to_garrison(file))