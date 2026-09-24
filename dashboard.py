import sys

from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QVBoxLayout, QHBoxLayout, QLabel,
    QStackedWidget, QListWidget, QLineEdit, QSpinBox,
    QMessageBox, QComboBox, QRadioButton, QButtonGroup
)

from historique_page import MainWindow
from ui import MainWindow as mn

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dashboard')
        self.setup_ui()
        self.connexion()

    def setup_ui(self):
        # Barres de navigation boutons en colonne
        self.btn_tableau = QPushButton("Tableau")
        self.btn_histo = QPushButton("Historique")

        for b in (self.btn_tableau, self.btn_histo):
            b.setObjectName("Btn_affiche-primary")

        # layout des boutons

        sidebar = QVBoxLayout()
        sidebar.setContentsMargins(10, 10, 10, 10)
        sidebar.setSpacing(20)
        sidebar.addWidget(self.btn_tableau)
        sidebar.addStretch(1)
        sidebar.addWidget(self.btn_histo)




        # Contenu principal (pile de pages)
        self.stack = QStackedWidget()
        self.pile_pages = self.stack
        main_win = MainWindow()
        Generate_win = mn()
        self.pile_pages.addWidget(Generate_win)
        self.pile_pages.addWidget(main_win)

        # le layout des windows
        top_layout = QHBoxLayout(self)

        top_layout.setContentsMargins(10, 10, 10, 10)
        top_layout.setSpacing(20)

        top_layout.addLayout(sidebar)
        top_layout.addWidget(self.stack)


    # les connexion des boutons et actions

    def connexion(self):
        self.btn_tableau.clicked.connect(self.page_Generate)
        self.btn_histo.clicked.connect(self.page_Historique)

    # la premiere page
    def page_Generate(self):
        self.pile_pages.setCurrentIndex(0)

    #la secode page
    def page_Historique(self):
        self.pile_pages.setCurrentIndex(1)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open("assets/styles.qss") as f:
        app.setStyleSheet(f.read())
    window = Dashboard()
    window.show()
    sys.exit(app.exec())