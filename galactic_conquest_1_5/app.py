# C:\Users\mdcar\PycharmProjects\Portfolio\GUI\PyQt\Qt Designer\project_file_1.9.1.py   use for reference of last run
# C:\Users\mdcar\PycharmProjects\Freelance\Galactic Supremacy 1.1 # where all related files must go
# C:\Users\mdcar\anaconda3\Library\bin # where to find and compile the ui file from qt designer
# Place the interface file physically here and then copy and paste:
# pyuic5 -x interface.ui -o interface.py
# Copy that file somewhere local to this project so it can be referenced

from galactic_conquest_1_5.data.file import File
from galactic_conquest_1_5.gui.interface_loader import load_interface
import os
from time import sleep

def main():
    file = File()
    load_interface(file)


def updateUI(base_file = True, planet_file = False):
    path1 = "C:\\Users\mdcar\PycharmProjects\Freelance\galactic_conquest_1.5_git\galactic_conquest_1_5\gui\pyqt_py3_gui_files"
    path2 = "C:\\users\mdcar\Anaconda3\Library\Bin"
    if base_file:
        cmd = "pyuic5 -x interface.ui -o main_interface_file.py"
        os.system("cd " + path2 + " && dir && " + cmd + " && " + "copy main_interface_file.py " + path1)
    if planet_file:
        cmd = "pyuic5 -x planet.ui -o planet_interface_file.py"
        os.system("cd " + path2 + " && dir && " + cmd + " && " + "copy planet_interface_file.py " + path1)

        # subprocess.run(['ls', '-al'])

updateUI()
main()
