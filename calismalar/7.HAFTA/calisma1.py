# pyqt5 commentler  https://realpython.com/python-menus-toolbars/
# 
## örnek 1
# from PyQt5.QtWidgets import *
# app = QApplication([])
# pencere = QWidget()
# pencere.show()
# app.exec()

# # örnek 2
# import sys
# from PyQt5.QtWidgets import *
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.show()
# # Start the event loop.
# app.exec()


# örenk 3
import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
window = QPushButton("Tıkla")
window.show()
app.exec()