import sys

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from admin import Admin
from historique_page import MainWindow


class AdminPage(QWidget):
    def __init__(self):
        super().__init__()
        self.page_historique = None
        self.setWindowTitle('Admin checking')
        self.resize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(10)

        self.stack = QStackedWidget(self)
        layout.addWidget(self.stack)

        self.create_page = self._build_form_page(
            title='inscription',
            primary_label='Créer admin',
            switch_label='Connexion',
            input_name='create',
        )
        self.login_page = self._build_form_page(
            title='identifiant admin',
            primary_label='Vérifier',
            switch_label='Inscription',
            input_name='login',
        )

        self.stack.addWidget(self.create_page)
        self.stack.addWidget(self.login_page)
        self.stack.setCurrentIndex(0)

        self.create_action_button.clicked.connect(self.check_user)
        self.login_action_button.clicked.connect(self.check_info)

        self.create_switch_button.clicked.connect(self.show_login_page)
        self.login_switch_button.clicked.connect(self.show_create_page)

    def _build_form_page(self, title, primary_label, switch_label, input_name):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(10)

        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(5, 5, 5, 5)
        title_label = QLabel(
            f"<h1 style='text-align: center; color: rgba(10, 40, 80, 1)'>{title}</h1>"
        )
        title_layout.addWidget(title_label)

        switch_button = QPushButton(switch_label)
        title_layout.addWidget(switch_button)
        layout.addLayout(title_layout)

        name_input = QLineEdit()
        name_input.setPlaceholderText('Nom')

        password_input = QLineEdit()
        password_input.setPlaceholderText('Mot de passe')
        password_input.setEchoMode(QLineEdit.Password)

        layout.addWidget(name_input)
        layout.addWidget(password_input)

        action_button = QPushButton(primary_label)
        layout.addWidget(action_button)
        layout.addStretch()

        setattr(self, f'{input_name}_name_input', name_input)
        setattr(self, f'{input_name}_password_input', password_input)
        setattr(self, f'{input_name}_action_button', action_button)
        setattr(self, f'{input_name}_switch_button', switch_button)

        return page

    def show_login_page(self):
        self.clear_form(self.create_name_input, self.create_password_input)
        self.stack.setCurrentWidget(self.login_page)
        self.raise_()
        self.activateWindow()

    def show_create_page(self):
        self.clear_form(self.login_name_input, self.login_password_input)
        self.stack.setCurrentWidget(self.create_page)
        self.raise_()
        self.activateWindow()

    @staticmethod
    def clear_form(*champ):
        for field in champ:
            field.clear()

    def check_info(self):
        nom = self.login_name_input.text().strip()
        mot = self.login_password_input.text()

        if not nom or not mot:
            QMessageBox.information(self, 'message', 'champ vide ...')
            return

        admin = Admin(nom, mot)
        if admin.check(nom, mot):
            self.page_historique = MainWindow()
            self.page_historique.show()
            self.clear_form(self.login_name_input, self.login_password_input)
            return

        QMessageBox.warning(self, 'Error', 'Le mot de passe est incorrect')

    def check_user(self):
        nom = self.create_name_input.text().strip()
        mot = self.create_password_input.text()

        if not nom or not mot:
            QMessageBox.information(self, 'message', 'champ vide ...')
            return

        admin = Admin(nom, mot)
        if admin.check(nom, mot):
            QMessageBox.warning(self, 'warning', 'Admin present')
            return

        admin.creer_un_admin()
        self.clear_form(self.create_name_input, self.create_password_input)
        QMessageBox.information(self, 'message', 'nouvel admin ajouté')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    with open('assets/styles.qss', 'r') as f:
        app.setStyleSheet(f.read())
    window = AdminPage()
    window.show()
    app.exec()
