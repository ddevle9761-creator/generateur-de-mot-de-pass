import sys
from gestion import GenerateurMdp

from PySide6 import QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gestionnaire de mots de passe")
        self.setGeometry(100, 100, 400, 300)

        self.setup_ui()
        self.connexion()


    def setup_ui(self):
        layout_ = QtWidgets.QVBoxLayout(self)
        self.layout = QtWidgets.QHBoxLayout()
        self.champ1 = QtWidgets.QLineEdit()
        self.champ1.setPlaceholderText('Le motif du mot de pass')
        layout_.addWidget(self.champ1)

        layout_.addLayout(self.layout)
        self.liste_widget = QtWidgets.QListWidget()
        self.layout.addWidget(self.liste_widget)
        self.btn_rafrechie = QtWidgets.QPushButton('Rafrechie les données')
        layout_.addWidget(self.btn_rafrechie)


    def connexion(self):

        self.infos()
        self.champ1.textChanged.connect(self.text_de_recherche)
        self.btn_rafrechie.clicked.connect(self.infos)

    def text_de_recherche(self, texte: str):
        self.rafrechie_users(filter_text=texte)

    def infos(self):
        infos = GenerateurMdp().les_sauvegarde()
        if infos:

            self.liste_widget.clear()
            self.champ1.clear()
            for info in infos:
                for i, x in info.items():
                    texte = f"{i}: <-> {x}"
                    self.liste_widget.addItem(texte)


    def rafrechie_users(self, filter_text: str = ''):

        recherche = GenerateurMdp().obtenir_recherche(filter_text=filter_text)
        if recherche:
            for recherche in recherche:
                self.liste_widget.clear()
                for x, y in recherche.items():
                    texte = f"{x}: -> {y}"
                    self.liste_widget.addItem(texte)

        else:
            self.liste_widget.clear()
            self.liste_widget.addItem('Aucune information trouvé')
            return




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    with open('assets/styles.qss', 'r') as f:
        app.setStyleSheet(f.read())
    window = MainWindow()

    window.show()
    app.exec()