import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLineEdit, 
    QPushButton, QLabel, QMessageBox, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt
from Database import Database as DB

class SearchProduct(QDialog):
    def __init__(self):
        super().__init__()

        self.DB = DB()
        self.setWindowTitle('Search Product')
        self.resize(900, 600)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.init_ui()

    def init_ui(self):
        self.init_title()
        self.init_form()
        self.init_results_list()
        self.init_buttons()

    def init_title(self):
        label = QLabel('Search Product')
        label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        self.main_layout.addWidget(label)

    def init_form(self):
        form_layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Ürün Adı Ara')
        self.search_input.setStyleSheet("padding: 6px; font-size: 16px; border: 1px solid #ccc; border-radius: 5px;")
        form_layout.addWidget(self.search_input)

        self.search_button = QPushButton('Ara')
        self.search_button.setStyleSheet("padding: 10px; font-size: 16px; background-color: #007BFF; color: white; border: none; border-radius: 5px;")
        self.search_button.clicked.connect(self.search_product)
        form_layout.addWidget(self.search_button)

        self.main_layout.addLayout(form_layout)

    def init_results_list(self):
        self.results_list = QListWidget()
        self.main_layout.addWidget(self.results_list)

    def init_buttons(self):
        button_layout = QHBoxLayout()

        self.close_button = self.create_button('Kapat', self.close)
        button_layout.addWidget(self.close_button)

        self.main_layout.addLayout(button_layout)

    def create_button(self, text, callback):
        button = QPushButton(text)
        button.setStyleSheet("padding: 10px; font-size: 16px; background-color: #007BFF; color: white; border: none; border-radius: 5px;")
        button.clicked.connect(callback)
        return button

    def search_product(self):
        search_query = self.search_input.text().strip()
        if not search_query:
            QMessageBox.critical(self, 'Hata', 'Lütfen aramak için bir ürün adı giriniz.')
            return

        products = self.DB.search_products(search_query)
        self.results_list.clear()
        print(products)
        
        if not products:
            QMessageBox.information(self, 'Sonuç Yok', 'Arama kriterlerine uygun ürün bulunamadı.')
            return

        for product in products:
            item = QListWidgetItem(f"Ürün Adı: {product[0]},Satış Fiyatı: {product[1]}, Alış Fiyatı: {[product[2]]}, Stok Miktarı: {product[3]}, Raf Numarası: {product[4]}, Ürün Açıklaması: {product[5]}, Marka: {product[6]}, Uyumlu Arabalar: {product[7]}, Ebat: {product[8]}, OEM: {product[9]}")
            self.results_list.addItem(item)

            similar_products = self.DB.get_similar_products([product[10]])
            if similar_products:
                for similar_product in similar_products:
                    similar_item = QListWidgetItem(f"Ürün Adı: {product[0]},Satış Fiyatı: {product[1]}, Alış Fiyatı: {[product[2]]}, Stok Miktarı: {product[3]}, Raf Numarası: {product[4]}, Ürün Açıklaması: {product[5]}, Marka: {product[6]}, Uyumlu Arabalar: {product[7]}, Ebat: {product[8]}, OEM: {product[9]}")
                    self.results_list.addItem(similar_item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SearchProduct()
    dialog.exec()
