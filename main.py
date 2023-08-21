from PyQt5.QtWidgets import *
from login_code import LoginPage

app=QApplication([])
pencere=LoginPage()
pencere.show()

app.exec_()
