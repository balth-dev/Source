import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "resa_salles")
DB_PORT = int(os.getenv("DB_PORT", "3307"))


def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT,
        )
        if connection.is_connected():
            print("Connexion à la base de données MySQL réussie !")
            return connection
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL : {e}")
        return None
    
    import sqlite3
import hashlib

DB_PATH = 'instance/rooms.db'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Users table (matches your description)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prenom TEXT NOT NULL,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telephone TEXT UNIQUE,
            genre TEXT,
            role TEXT,
            password TEXT NOT NULL
        )
    ''')
    
    # Rooms table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            capacity INTEGER NOT NULL,
            equipment TEXT,
            amenities TEXT
        )
    ''')
    
    # Reservations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            room_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            duration INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        )
    ''')
    
    # Insert sample rooms
    cursor.execute("SELECT COUNT(*) FROM rooms")
    if cursor.fetchone()[0] == 0:
        sample_rooms = [
            ("Salle Émeraude", 8, "video", "Vidéoprojecteur, Tableau blanc"),
            ("Amphithéâtre Central", 45, "visio", "Écran géant, Sonorisation, Visio"),
            ("Salle Azur", 14, "whiteboard", "Tableau blanc, Wifi haut débit"),
            ("Lab Créatif", 22, "video", "Smart TV, Câble HDMI, Paperboard"),
            ("Huddle Room", 4, "whiteboard", "Écran tactile, Adaptateur USB-C"),
            ("Salle Lumière", 12, "visio", "Visio 4K, Micro sans fil")
        ]
        for name, cap, equip, amenities in sample_rooms:
            cursor.execute("INSERT INTO rooms (name, capacity, equipment, amenities) VALUES (?,?,?,?)",
                           (name, cap, equip, amenities))
    
    conn.commit()
    conn.close()

def add_user(prenom, nom, email, telephone, genre, role, password):
    # Simple hash for demo (use bcrypt in production)
    hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (prenom, nom, email, telephone, genre, role, password)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (prenom, nom, email, telephone or None, genre, role, hashed))
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    return dict(user) if user else None

def get_all_rooms():
    conn = get_db()
    rooms = conn.execute("SELECT * FROM rooms").fetchall()
    conn.close()
    return [dict(r) for r in rooms]

def get_room_by_id(room_id):
    conn = get_db()
    room = conn.execute("SELECT * FROM rooms WHERE id = ?", (room_id,)).fetchone()
    conn.close()
    return dict(room) if room else None

def add_reservation(user_id, room_id, date, start_time, end_time, duration):
    conn = get_db()
    conn.execute('''
        INSERT INTO reservations (user_id, room_id, date, start_time, end_time, duration)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, room_id, date, start_time, end_time, duration))
    conn.commit()
    conn.close()

def get_user_reservations(user_id):
    conn = get_db()
    rows = conn.execute('''
        SELECT r.id, rooms.name as room_name, r.date, r.start_time, r.end_time, r.duration
        FROM reservations r
        JOIN rooms ON r.room_id = rooms.id
        WHERE r.user_id = ?
        ORDER BY r.date, r.start_time
    ''', (user_id,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]

def cancel_reservation(reservation_id, user_id):
    conn = get_db()
    conn.execute("DELETE FROM reservations WHERE id = ? AND user_id = ?", (reservation_id, user_id))
    conn.commit()
    conn.close()
