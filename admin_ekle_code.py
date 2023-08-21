from PyQt5.QtWidgets  import *
from PyQt5.QtWidgets import QWidget
from admin_ekle import Ui_Form

class admineklePage(QWidget):
      def __init__(self) -> None:
            super().__init__()
            self.adminekleform=Ui_Form()
            self.adminekleform.setupUi(self)
            
      
    