from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.views.register import RegisterView as RegisterDialog

FIELD_LABELS = {
    "email": "Email",
    "password": "Mot de passe",


}

ERROR_MESSAGES = {
    "mail": "L'adresse email n'est pas valide.",
    "password": "Le mot de passe doit contenir au moins 8 caracteres, une majuscule, un chiffre et un caractere special.",
    "gender": "Le genre selectionne n'est pas valide.",
    "id_role": "Le role doit etre selectionne.",
}

GENDER_MAPPING = {
    "Selectionner un genre": None,
    "homme": "homme",
    "femme": "femme",
    "non-renseigner": "non renseigne",
}

ROLE_MAPPING = {
    "Selectionner un role": None,
    "Utilisateur": 1,
    "Admin": 2,
}

class LoginView(QWidget):
    login_clicked = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setObjectName("LoginWidget")
        self.setStyleSheet(
            "QWidget#LoginWidget { background-color: #0E1216; color: #E8EFF5; }"
            "QFrame { background-color: #11161A; }"
            "QLabel { color: #E8EFF5; }"
            "QPushButton { background-color: #2D6AB7; color: #FFFFFF; border-radius: 10px; }"
            "QPushButton:hover { background-color: #3F7FD2; }"
            "QPushButton:pressed { background-color: #245B95; }"
        )

        # Champs et bouton de connexion
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Mot de passe")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Se connecter", self)
        self.login_button.setObjectName("loginButton")
        self.login_button.setMinimumHeight(40)
        self.login_button.clicked.connect(self._on_login_clicked)

        self.signup_button = QPushButton("Créer un compte", self)
        self.signup_button.setObjectName("signupButton")
        self.signup_button.setFlat(True)
        self.signup_button.setStyleSheet(
            "QPushButton#signupButton { color: #A2D1FF; background: transparent; border: none; text-decoration: underline; }"
            "QPushButton#signupButton:hover { color: #FFFFFF; }"
        )
        self.signup_button.setCursor(Qt.PointingHandCursor)
        self.signup_button.clicked.connect(self.open_register)

        # Mise en page de la vue de connexion
        self.setWindowTitle("Connexion")
        self.resize(500, 320)
        self.setMinimumSize(420, 280)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        title = QLabel("Connexion")
        title.setObjectName("formTitle")
        layout.addWidget(title)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.signup_button)
        layout.addStretch()

    def _on_login_clicked(self):
        email = self.email_input.text() if hasattr(self, "email_input") else ""
        password = self.password_input.text() if hasattr(self, "password_input") else ""
        self.login_clicked.emit(email, password)

    def open_register(self):
        register_dialog = RegisterDialog(self)
        register_dialog.exec()

    def invalid_credential(self):
        QMessageBox.critical(self, "Erreur de connexion", "Email ou mot de passe incorrect.")

    # Le formulaire d'inscription est géré dans app/views/register.py
