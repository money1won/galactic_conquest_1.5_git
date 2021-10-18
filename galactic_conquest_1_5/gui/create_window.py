from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QScrollArea, QLabel)
from PyQt5.QtCore import QEvent
import sys

from galactic_conquest_1_5.gui.pyqt_py3_gui_files import main_interface_file, planet_interface_file
from galactic_conquest_1_5.gui.pyqt_py3_gui_files.main_interface_file import Ui_MainWindow

# Sets up the interface window class
class CreateMyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Setup Qt Designer items DO NOT CHANGE here
        # Identifies the dialog.ui as "self.ui" within this class
        # Any additional widgets created within this class will not use the .ui extension
        super(CreateMyWindow, self).__init__()
        # Loads the custom UI file for the window's features
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Used for map scrolling
        self.last_time_move_y = 0
        self.last_time_move_x = 0

        self.ui.MapScrollArea.setWidget(self.ui.scrollAreaWidgetCHANGE_GEO_SIZE)
        self.ui.MapScrollArea.installEventFilter(self)

        self.ui.MapVerticalScrollBar = self.ui.MapScrollArea.verticalScrollBar()
        self.ui.MapHorizontalScrollBar = self.ui.MapScrollArea.horizontalScrollBar()
        # .

        # End DO NOT CHANGE setup

    # Do not edit, used in the click to drag map feature
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseMove:
            # print(event.pos().y())

            if self.last_time_move_y == 0:
                self.last_time_move_y = event.pos().y()

            distance = self.last_time_move_y - event.pos().y()
            self.ui.MapVerticalScrollBar.setValue(self.ui.MapVerticalScrollBar.value() + distance)
            self.last_time_move_y = event.pos().y()

            if self.last_time_move_x == 0:
                self.last_time_move_x = event.pos().x()

            distance = self.last_time_move_x - event.pos().x()
            self.ui.MapHorizontalScrollBar.setValue(self.ui.MapHorizontalScrollBar.value() + distance)
            self.last_time_move_x = event.pos().x()

        elif event.type() == QEvent.MouseButtonRelease:
            self.last_time_move_y = 0
            self.last_time_move_x = 0
        return QWidget.eventFilter(self, source, event)