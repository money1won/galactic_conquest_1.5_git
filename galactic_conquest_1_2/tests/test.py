from random import *

def test_function(file):
    for _planet in file.planets:
        _button = _planet.ui.mapPlanetAssault_Button
        _button.setCheckable(True)
        # _button.clicked.connect(changeColor)

        # setting default color of button to light-grey
        _button.setStyleSheet("background-color : lightgrey")

    # method called by button
def changeColor(self):

    # if button is checked
    if self.button.isChecked():

        # setting background color to light-blue
        self.button.setStyleSheet("background-color : lightblue")
    else:
         # set background color back to light-grey
         self.button.setStyleSheet("background-color : lightgrey")