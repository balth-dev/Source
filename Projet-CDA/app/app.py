import sys
from PySide6.QtWidgets import QApplication

from app.views.register import RegisterView
from app.views.connexion import LoginView
from app.controllers.login_controller import LoginController
from app.repositories.user_repository import UserRepository

def run():
    app = QApplication(sys.argv)

    # Initialiser le repository et les vues
    user_repository = UserRepository()
    login_view = LoginView()
    login_controller = LoginController(login_view, user_repository)
    
    # Afficher la vue de connexion
    login_view.setWindowTitle("Connexion")
    login_view.setMinimumSize(500, 300)
    login_view.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    run()
