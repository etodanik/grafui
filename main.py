#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys

from PySide2.QtWidgets import (QApplication)
from ui.MainWindow import MainWindow

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    window = MainWindow()
    window.show()
    # Run the main Qt loop
    sys.exit(app.exec_())