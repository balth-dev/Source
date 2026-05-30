from bcrypt import checkpw
from app.views.connexion import LoginView
from app.repositories.user_repository import UserRepository
from sqlalchemy.exc import OperationalError

class LoginController:
    def __init__(self, view: LoginView, repository: UserRepository):
        self.view = view
        self.repository = repository
        self._initialize()
        self.connect_signal()
        
    def _initialize(self):
        pass
    
    def connect_signal(self):
        self.view.login_clicked.connect(self.on_login_clicked)
    
    def on_login_clicked(self, email: str, password: str):
        
        try:
            user = self.repository.get_by_email(email)
        except OperationalError:
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.critical(
                self.view,
                "Erreur de base de données",
                "Impossible de se connecter à la base de données. Vérifie tes identifiants ou ta configuration .env.",
            )
            return
        
        if user and self._verify_password(password, user.password):
            # Connexion réussie
            from PySide6.QtWidgets import QMessageBox
            QMessageBox.information(self.view, "Succès", f"Bienvenue {user.name}!")
        else:
            # Identifiants incorrects
            self.view.invalid_credential()

    def _verify_password(self, provided_password: str, stored_password: str) -> bool:
        return checkpw(
            provided_password.encode("utf-8"),
            stored_password.encode("utf-8"),
        )
        
        
#    def on_login_clicked(self, login: str, password: str):
#        user = self.repository.get_by_email(login)
#        compare = self.repository.get_by_email(login)
#        if user and compare:
#            pass #afficher la page d'accueil