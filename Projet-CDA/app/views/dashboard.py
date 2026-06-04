from PySide6.QtCore import Qt, QTimer, QTime, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QScrollArea, QPushButton, QFrame
)
from datetime import datetime, date

class DashboardView(QWidget):
    reserve_clicked = Signal(int)  # Signal pour la réservation avec id de la salle

    def __init__(self):
        super().__init__()
        self.setObjectName("DashboardWidget")
        self.setStyleSheet(
            "QWidget#DashboardWidget { background-color: #0E1216; color: #E8EFF5; }"
            "QLabel { color: #E8EFF5; }"
            "QPushButton { background-color: #2D6AB7; color: #FFFFFF; border-radius: 5px; padding: 5px; }"
            "QPushButton:hover { background-color: #3F7FD2; }"
            "QPushButton:pressed { background-color: #245B95; }"
            "QFrame { background-color: #11161A; border-radius: 5px; padding: 10px; }"
        )

        self.setWindowTitle("Tableau de bord")
        self.resize(1000, 700)
        self.setMinimumSize(800, 600)

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Titre et horloge
        top_layout = QHBoxLayout()
        
        title = QLabel("Bienvenue sur le tableau de bord")
        title.setObjectName("dashboardTitle")
        title.setStyleSheet("QLabel#dashboardTitle { font-size: 24px; font-weight: bold; }")
        top_layout.addWidget(title)
        
        top_layout.addStretch()
        
        # Horloge
        self.clock_label = QLabel()
        self.clock_label.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; padding: 10px; }")
        top_layout.addWidget(self.clock_label)
        
        # Démarrer le timer pour l'horloge
        self.timer = QTimer()
        self.timer.timeout.connect(self._update_clock)
        self.timer.start(1000)  # Mise à jour chaque seconde
        self._update_clock()  # Affichage initial
        
        main_layout.addLayout(top_layout)

        # Section des salles disponibles
        salles_title = QLabel("Salles disponibles")
        salles_title.setStyleSheet("QLabel { font-size: 18px; font-weight: bold; margin-top: 20px; }")
        main_layout.addWidget(salles_title)

        # Scroll area pour les salles
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")
        
        self.rooms_container = QWidget()
        self.rooms_layout = QVBoxLayout(self.rooms_container)
        self.rooms_layout.setSpacing(10)
        self.rooms_layout.addStretch()
        
        scroll_area.setWidget(self.rooms_container)
        main_layout.addWidget(scroll_area)

        # Bouton de déconnexion
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        logout_button = QPushButton("Se déconnecter")
        logout_button.setMaximumWidth(150)
        logout_button.clicked.connect(self.on_logout_clicked)
        button_layout.addWidget(logout_button)
        
        main_layout.addLayout(button_layout)

    def _update_clock(self):
        """Mettre à jour l'horloge avec l'heure actuelle"""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.clock_label.setText(f"🕐 {current_time}")

    def add_room(self, room_id: int, room_name: str, capacity: int, category: str, stage: str):
        """Ajouter une salle à la liste des disponibles"""
        # Créer un frame pour la salle
        room_frame = QFrame()
        room_frame.setFixedHeight(80)
        room_layout = QHBoxLayout(room_frame)
        room_layout.setContentsMargins(15, 10, 15, 10)
        room_layout.setSpacing(10)

        # Infos de la salle
        info_layout = QVBoxLayout()
        
        name_label = QLabel(f"<b>{room_name}</b>")
        name_label.setStyleSheet("QLabel { font-size: 14px; font-weight: bold; }")
        info_layout.addWidget(name_label)

        details = f"Capacité: {capacity} | Catégorie: {category} | Étage: {stage}"
        details_label = QLabel(details)
        details_label.setStyleSheet("QLabel { font-size: 11px; color: #A2D1FF; }")
        info_layout.addWidget(details_label)

        room_layout.addLayout(info_layout)
        room_layout.addStretch()

        # Bouton de réservation
        reserve_btn = QPushButton("Réserver")
        reserve_btn.setMaximumWidth(100)
        reserve_btn.setMaximumHeight(35)
        reserve_btn.clicked.connect(lambda: self.reserve_clicked.emit(room_id))
        room_layout.addWidget(reserve_btn)

        # Insérer avant le stretch du container
        self.rooms_layout.insertWidget(self.rooms_layout.count() - 1, room_frame)

    def clear_rooms(self):
        """Effacer toutes les salles affichées"""
        while self.rooms_layout.count() > 1:  # Garder le stretch
            item = self.rooms_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

    def show_no_rooms_message(self):
        """Afficher un message si aucune salle disponible"""
        self.clear_rooms()
        no_rooms_label = QLabel("Aucune salle disponible pour le moment")
        no_rooms_label.setStyleSheet("QLabel { color: #FF6B6B; font-size: 14px; text-align: center; }")
        no_rooms_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rooms_layout.insertWidget(0, no_rooms_label)

    def on_logout_clicked(self):
        """Gestion de la déconnexion"""
        # Réafficher la vue de connexion et effacer les champs
        if hasattr(self, 'login_view'):
            self.login_view.email_input.clear()
            self.login_view.password_input.clear()
            self.login_view.show()
        
        self.close()

    def closeEvent(self, event):
        """Arrêter le timer quand la fenêtre se ferme"""
        self.timer.stop()
        super().closeEvent(event)
