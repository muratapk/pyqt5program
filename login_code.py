from PyQt5.QtWidgets  import *
from login import Ui_Form
from anasayfa_code import anasayfaPencere

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.loginform=Ui_Form()
        self.loginform.setupUi(self)
        self.anasayfaac=anasayfaPencere()
        self.loginform.pushButton.clicked.connect(self.login_in)
    
    def login_in(self):
        kadi=self.loginform.line_EditKullanici.text()
        sifre=self.loginform.line_EditSifre.text()
        if kadi=="Murat" and sifre=="123":
            self.anasayfaac.show()
            self.hide()


