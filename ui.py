import sys
from gestion import GenerateurMdp

from PySide6 import QtWidgets, QtCore

from PySide6.QtWidgets import QApplication

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button1 = None
        self.liste_widget = None
        self.champ1 = None
        self.layout = None
        self.button_copier = None
        self.setWindowTitle("Gestionnaire de mots de passe")
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()
        self.connexion()

    def setup_ui(self):
        layout_ = QtWidgets.QVBoxLayout(self)
        self.layout = QtWidgets.QHBoxLayout()
        self.champ1 = QtWidgets.QLineEdit()
        self.champ1.setPlaceholderText('Le motif du mot de pass')


        layout_.addWidget(self.champ1, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        
        layout_.addLayout(self.layout)
        self.button_copier = QtWidgets.QPushButton("Copier")
        self.button_copier.setObjectName("Copier")

        self.button1 = QtWidgets.QPushButton("Générer un mot de passe")


        self.button_copier.setFixedSize(100, 40)


        self.layout.addWidget(self.champ1)
        self.layout.addWidget(self.button_copier)

        self.liste_widget = QtWidgets.QListWidget()
        layout_.addWidget(self.liste_widget)
        layout_.addWidget(self.button1)

    def connexion(self):
        self.button1.clicked.connect(lambda x : self.obtenir_le_result_du_champs())
        self.button_copier.clicked.connect(lambda x:self.copier())


    def obtenir_le_result_du_champs(self):
        champ1 = self.champ1.text()
        if champ1 == '' or champ1 is None:

            return False
        model = GenerateurMdp()
        genere = model.generer_un_mot_de_pass(champ1)
        model.sauvegarder_le_mdp()
        self.liste_widget.clear()
        self.liste_widget.addItem(genere)

        return genere

    def copier(self):
        if self.liste_widget.count() == 0:
            return False
        mdp = self.liste_widget.item(0)
        copier = QApplication.clipboard()
        copier.setText(mdp.text())
        QtWidgets.QMessageBox.information(self, "info", "Mot de pass copier")
        return None


app = QtWidgets.QApplication(sys.argv)
with open('assets/styles.qss', 'r') as f:
    styles = f.read()
    app.setStyleSheet(styles)
window = MainWindow()
window.show()
app.exec()