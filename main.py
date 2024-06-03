import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLineEdit, 
                             QPushButton, QLabel, QMessageBox, QStackedLayout, QWidget, QGridLayout)
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtCore import Qt
from admin.admin import AdminPanel as admin
import Database as DB

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        self.setWindowTitle('Stok Takip Programı - V0.1 - Auth:Hamza ORTATEPE')
        self.resize(300, 400)
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.init_background()
        self.init_foreground()

    def init_background(self):
        self.background = QLabel(self)
        movie = QMovie('orig.gif')
        self.background.setMovie(movie)
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 300, 400)
        movie.start()

        self.layout.addWidget(self.background, 0, 0, 1, 1)

    def init_foreground(self):
        self.foreground_widget = QWidget()
        foreground_layout = QVBoxLayout()

        self.label = QLabel('Stok Takip Programına Hoşgeldiniz')
        self.label.setStyleSheet("font-size: 30px; font-weight: bold; text-align: center;color:white;")
        foreground_layout.addWidget(self.label)

        self.usernameLabel = QLabel('Kullanıcı Adı')
        self.usernameLabel.setStyleSheet("font-size: 16px; font-weight: bold;color:white;")
        foreground_layout.addWidget(self.usernameLabel)

        self.username = QLineEdit()
        self.username.setPlaceholderText('Kullanıcı Adı')
        self.username.setStyleSheet("""
            padding: 10px; 
            font-size: 16px; 
            border: 1px solid #ccc; 
            border-radius: 5px;
            color:white;
        """)
        foreground_layout.addWidget(self.username)

        self.passwordLabel = QLabel('Şifre')
        self.passwordLabel.setStyleSheet("font-size: 16px; font-weight: bold;color:white;")
        foreground_layout.addWidget(self.passwordLabel)

        self.password = QLineEdit()
        self.password.setPlaceholderText('Şifre')
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("""
            padding: 10px; 
            font-size: 16px; 
            border: 1px solid #ccc; 
            border-radius: 5px;
            color:white;
        """)
        foreground_layout.addWidget(self.password)

        self.login_button = QPushButton('Giriş Yap')
        self.login_button.setStyleSheet("""
            QPushButton {
                padding: 10px; 
                font-size: 16px; 
                background-color: red; 
                color: white; 
                border: none; 
                border-radius: 5px;
            }
            QPushButton:hover {
                font-weight: bold;
            }
            
        """)
        self.login_button.clicked.connect(self.check_credentials)
        foreground_layout.addWidget(self.login_button)

        self.foreground_widget.setLayout(foreground_layout)
        self.foreground_widget.setStyleSheet("background: transparent;")
        self.layout.addWidget(self.foreground_widget, 0, 0, 1, 1)

    def check_credentials(self):
        username = self.username.text()
        password = self.password.text()

        if not username or not password:
            QMessageBox.critical(self, 'Hata', 'Kullanıcı Adı ve Şifre Boş Olamaz')
            return

        user = DB.Database().authenticate_user(username, password)
        if user:
            QMessageBox.information(self, 'Başarılı', 'Başarıyla Giriş Yapıldı')
            self.accept()
        else:
            QMessageBox.critical(self, 'Hata', 'Geçersiz Kullanıcı Adı veya Şifre')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()

    if login_dialog.exec() == QDialog.Accepted:
        print('Login successful')
        admin_panel = admin()
        admin_panel.exec()
    else:
        print('Login failed')
