import sys
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLineEdit, 
                             QPushButton, QLabel, QMessageBox, QStackedLayout, QWidget, QGridLayout)
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

from admin.add_prod import AddProduct
from admin.search_product import SearchProduct

class AdminPanel(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)

        self.setWindowTitle('Admin Panel')
        self.resize(400, 300)

        # Set up the layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Set up the background GIF
        self.init_background()

        # Set up the UI components
        self.init_foreground()

    def init_background(self):
        self.background = QLabel(self)
        movie = QMovie('bg.gif')
        self.background.setMovie(movie)
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 500, 300)
        movie.start()

    def init_foreground(self):
        self.main_widget = QWidget()
        main_layout = QVBoxLayout(self.main_widget)

        self.label = QLabel('Yönetici Paneline Hoşgeldiniz')
        self.label.setStyleSheet("font-size: 30px; font-weight: bold; text-align: center;color:white;")
        main_layout.addWidget(self.label)

        self.add_product_button = QPushButton('Ürün Ekle')
        self.add_product_button.setStyleSheet("""
            QPushButton {
                padding: 10px; 
                font-size: 16px; 
                background-color: #007BFF; 
                color: white; 
                border: none; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.add_product_button.clicked.connect(self.add_product)
        main_layout.addWidget(self.add_product_button)

        self.search_product_button = QPushButton('Ürün Ara')
        self.search_product_button.setStyleSheet("""
            QPushButton {
                padding: 10px; 
                font-size: 16px; 
                background-color: #007BFF; 
                color: white; 
                border: none; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.search_product_button.clicked.connect(self.search_product)
        main_layout.addWidget(self.search_product_button)

        # Make the main_widget transparent
        self.main_widget.setStyleSheet("background:transparent;")
        self.layout.addWidget(self.main_widget, 0, 0, 1, 1)

    def add_product(self):
        add_product_dialog = AddProduct()
        add_product_dialog.exec_()

    def search_product(self):
        search_product_dialog = SearchProduct()
        search_product_dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = AdminPanel()
    dialog.exec_()
