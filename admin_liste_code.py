from PyQt5.QtWidgets  import *
from PyQt5.QtWidgets import QWidget
from admin_liste import Ui_Form

class adminlistePage(QWidget):
      def __init__(self):
            super().__init__()
            self.adminlisteform=Ui_Form()
            self.adminlisteform.setupUi(self)