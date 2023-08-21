from PyQt5.QtWidgets import *
from anasayfa import Ui_MainWindow
from admin_ekle_code import admineklePage
from admin_liste_code import adminlistePage

class anasayfaPencere(QMainWindow):
     def __init__(self):
        super().__init__()
        self.anasayfaform=Ui_MainWindow()
        self.anasayfaform.setupUi(self)
        self.adminekle=admineklePage()
        self.adminliste=adminlistePage()

        self.anasayfaform.Admin_Ekle.triggered.connect(self.Admin_Ekle_Formu)
        self.anasayfaform.Admin_Listele.triggered.connect(self.Admin_Liste_Formu)
  
     def Admin_Ekle_Formu(self):
          self.adminekle.show()
          
     def Admin_Liste_Formu(self):
          self.adminliste.show()
          
          
    