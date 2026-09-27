from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtWidgets import (
 QLineEdit, QPushButton, QVBoxLayout
)



from admin import Admin
from historique_page import MainWindow
import sys

class AdminPage(QWidget):
    def __init__(self):
        super().__init__()
        self.edit_nom_line = None
        self.edit_mdp_line = None
        self.page_historique = None
        self.btn_check = None
        self.setWindowTitle('Admin checking')
        self.setGeometry(300, 300, 300, 300)
        self.check_setup()
        self.connexion()

    def check_setup(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)

        self.edit_nom_line = QLineEdit()
        self.edit_nom_line.setPlaceholderText("Nom ")
        self.edit_mdp_line = QLineEdit()
        self.edit_mdp_line.setPlaceholderText("Mot de pass")
        layout.addWidget(self.edit_nom_line)
        layout.addWidget(self.edit_mdp_line)

        self.btn_check = QPushButton('Verifier')
        layout.addWidget(self.btn_check)

    def connexion(self):
        self.btn_check.clicked.connect(lambda x:self.check_info())

    def check_info(self):
        nom = str(self.edit_nom_line.text())
        mot = str(self.edit_mdp_line.text())
        admin = Admin(nom, mot)

        if admin.check(nom, mot):
            self.page_historique = MainWindow()
            self.page_historique.show()
            self.edit_mdp_line.clear()
            self.edit_nom_line.clear()

        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Le mot de pass est incorrect')







if __name__ == "__main__":

    app = QApplication(sys.argv)
    with open('assets/styles.qss', 'r') as f:
        app.setStyleSheet(f.read())
    window = AdminPage()
    window.show()
    app.exec()

