from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError, OperationalError

from app.repositories.user_repository import UserRepository
from app.validators.user_validator import UserCreate
from pages.interface.Register_ui import Ui_Register

FIELD_LABELS = {
    "lastname": "Nom",
    "firstname": "Prenom",
    "email": "Email",
    "password": "Mot de passe",
    "gender": "Genre",
    "role": "Role",
}

ERROR_MESSAGES = {
    "name": "Le nom doit contenir au moins 3 caracteres.",
    "surname": "Le prenom doit contenir au moins 3 caracteres.",
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
    "admin": 2,
    "gestionnaire": 3,
    "enseignant": 4,
    "etudiant": 5,
    "technicien": 6,
}


class RegisterView(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("RegisterWidget")
        self.setWindowTitle("Inscription")
        self.resize(760, 740)
        self.setMinimumSize(720, 620)
        self.ui = Ui_Register()
        self.ui.setupUi(self)
 #       self._build_ui()
 #       self._apply_styles()

        self.repository = UserRepository()
        self.firstname_input = self.ui.firstnameLineEdit
        self.lastname_input = self.ui.lastnameLineEdit
        self.email_input = self.ui.registerEmailLineEdit
        self.gender_combo = self.ui.genderComboBox
        self.role_combo = self.ui.roleComboBox
        self.password_input = self.ui.registerPasswordLineEdit
        self.confirm_password_input = self.ui.confirmPasswordLineEdit
        self.error_label = self.ui.error_label
        self.register_button = self.ui.registerButton

        self.error_label.hide()
        self.register_button.clicked.connect(self.click_register_submit)

    def _build_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(24, 24, 24, 24)
        self.main_layout.setSpacing(16)

        header_label = QLabel("Creer un compte")
        header_label.setObjectName("formTitle")
        self.main_layout.addWidget(header_label)

        subtitle = QLabel("Remplissez le formulaire pour creer votre compte.")
        subtitle.setObjectName("formSubtitle")
        subtitle.setWordWrap(True)
        self.main_layout.addWidget(subtitle)

        self.error_label = QLabel()
        self.error_label.setObjectName("errorLabel")
        self.error_label.setWordWrap(True)
        self.main_layout.addWidget(self.error_label)

        form_frame = QFrame()
        form_frame.setObjectName("formFrame")
        form_layout = QGridLayout(form_frame)
        form_layout.setSpacing(18)
        form_layout.setContentsMargins(16, 16, 16, 16)

        self.firstname_input = QLineEdit()
        self.firstname_input.setPlaceholderText("Prenom")
        self.lastname_input = QLineEdit()
        self.lastname_input.setPlaceholderText("Nom")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.gender_combo = QComboBox()
        self.gender_combo.addItems([
            "Selectionner un genre",
            "homme",
            "femme",
            "non-renseigner",
        ])
        self.role_combo = QComboBox()
        self.role_combo.addItems([
            "Selectionner un role",
            "Utilisateur",
            "Admin",
        ])
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mot de passe")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirmer le mot de passe")
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)

        form_layout.addWidget(self._make_field_group("Prenom", self.firstname_input), 0, 0)
        form_layout.addWidget(self._make_field_group("Nom", self.lastname_input), 0, 1)
        form_layout.addWidget(self._make_field_group("Email", self.email_input), 1, 0)
        form_layout.addWidget(self._make_field_group("Role", self.role_combo), 1, 1)
        form_layout.addWidget(self._make_field_group("Genre", self.gender_combo), 2, 0)
        form_layout.addWidget(self._make_field_group("Mot de passe", self.password_input), 2, 1)
        form_layout.addWidget(self._make_field_group("Confirmer le mot de passe", self.confirm_password_input), 3, 0, 1, 2)

        self.main_layout.addWidget(form_frame)

        self.register_button = QPushButton("S'inscrire")
        self.register_button.setObjectName("registerButton")
        self.register_button.setMinimumHeight(50)
        self.main_layout.addWidget(self.register_button)

        self.main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    def _make_field_group(self, label_text: str, widget: QWidget) -> QFrame:
        container = QFrame()
        container.setObjectName("fieldGroup")
        layout = QVBoxLayout(container)
        layout.setSpacing(8)
        layout.setContentsMargins(12, 12, 12, 12)

        label = QLabel(label_text)
        label.setObjectName("fieldLabel")
        layout.addWidget(label)
        layout.addWidget(widget)

        return container

    def _apply_styles(self):
        self.setStyleSheet(
            "QWidget#RegisterWidget { background-color: #0E1216; color: #E8EFF5; }"
            "QFrame#formFrame { background-color: #131A20; border-radius: 20px; border: 1px solid #223147; }"
            "QLabel#formTitle { font-size: 28px; font-weight: 700; color: #ffffff; }"
            "QLabel#formSubtitle { color: #9EA8B4; font-size: 14px; }"
            "QLabel#fieldLabel { color: #DCE6F1; font-size: 12px; font-weight: 600; }"
            "QFrame#fieldGroup { background-color: #10161D; border: 1px solid #223147; border-radius: 16px; }"
            "QLineEdit, QComboBox { background-color: #10161D; border: 1px solid #223147; border-radius: 12px; color: #ffffff; padding: 10px; }"
            "QLineEdit:focus, QComboBox:focus { border: 1px solid #2CCED2; }"
            "QPushButton#registerButton { background-color: #2D6AB7; color: #ffffff; border: none; border-radius: 14px; font-size: 15px; font-weight: 700; }"
            "QPushButton#registerButton:hover { background-color: #3F7FD2; }"
            "QPushButton#registerButton:pressed { background-color: #245B95; }"
            "QLabel#errorLabel { color: #ffc9c9; background-color: #3f1f1f; border: 1px solid #a33a3a; border-radius: 10px; padding: 10px; }"
        )
        self.error_label.setObjectName("errorLabel")

    def click_register_submit(self):
        role_id = ROLE_MAPPING.get(self.role_combo.currentText())
        if role_id is None:
            self._show_error("Le role doit etre selectionne.")
            return

        if self.password_input.text() != self.confirm_password_input.text():
            self._show_error("Les mots de passe ne correspondent pas.")
            return

        try:
            user_create = UserCreate(
                name=self.lastname_input.text().strip(),
                surname=self.firstname_input.text().strip(),
                mail=self.email_input.text().strip(),
                password=self.password_input.text(),
                gender=GENDER_MAPPING.get(self.gender_combo.currentText()),
                id_role=role_id,
            )
        except ValidationError as exc:
            messages = "\n".join(
                f"- {ERROR_MESSAGES.get(err['loc'][0], self._default_error_message(err))}"
                for err in exc.errors()
            )
            self._show_error(messages)
            return

        try:
            self.repository.add(user_create)
        except IntegrityError:
            self._show_error("Cet email est déjà utilisé.")
            return
        except OperationalError:
            QMessageBox.critical(
                self,
                "Erreur de base de données",
                "Impossible de se connecter à la base de données. Vérifie ta configuration .env.",
            )
            return

        self._clear_error()
        QMessageBox.information(self, "Succès", "Inscription validée.")
        self.accept()

    def _default_error_message(self, error):
        field_name = error["loc"][0]
        return f"{FIELD_LABELS.get(field_name, field_name)} : valeur invalide."

    def _show_error(self, message):
        self.error_label.setText(message)
        self.error_label.show()

    def _clear_error(self):
        self.error_label.clear()
        self.error_label.hide()
