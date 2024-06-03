import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, 
    QPushButton, QLabel, QMessageBox, QFileDialog, QComboBox, QWidget
)
from PyQt5.QtGui import QPixmap, QIntValidator
from PyQt5.QtCore import Qt, QByteArray, QBuffer
from Database import Database as DB
import base64

class AddProduct(QDialog):
    def __init__(self):
        super().__init__()

        self.DB = DB()
        self.setWindowTitle('Add Product')
        self.resize(900, 600)

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.init_ui()

    def init_ui(self):
        self.init_title()
        self.init_form()
        self.init_buttons()

    def init_title(self):
        label = QLabel('Add Product')
        label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        self.main_layout.addWidget(label)

    def init_form(self):
        form_layout = QGridLayout()

        self.product_name = self.create_line_edit('Ürün Adı')
        form_layout.addWidget(self.create_label('Ürün Adı'), 0, 0)
        form_layout.addWidget(self.product_name, 0, 1)

        self.product_price = self.create_line_edit('Satış Fiyatı', validator=QIntValidator())
        form_layout.addWidget(self.create_label('Satış Fiyatı'), 1, 0)
        form_layout.addWidget(self.product_price, 1, 1)

        self.product_buy_price = self.create_line_edit('Alış Fiyatı', validator=QIntValidator())
        form_layout.addWidget(self.create_label('Alış Fiyatı'), 2, 0)
        form_layout.addWidget(self.product_buy_price, 2, 1)

        self.product_stock = self.create_line_edit('Stok Adeti', validator=QIntValidator())
        form_layout.addWidget(self.create_label('Stok Adeti'), 3, 0)
        form_layout.addWidget(self.product_stock, 3, 1)

        self.product_shelf = self.create_line_edit('Raf Numarası')
        form_layout.addWidget(self.create_label('Raf Numarası'), 4, 0)
        form_layout.addWidget(self.product_shelf, 4, 1)

        self.product_description = self.create_line_edit('Ürün Açıklaması')
        form_layout.addWidget(self.create_label('Ürün Açıklaması'), 5, 0)
        form_layout.addWidget(self.product_description, 5, 1)

        self.product_brand = self.create_combo_box(self.DB.get_brands())
        form_layout.addWidget(self.create_label('Marka'), 6, 0)
        form_layout.addWidget(self.product_brand, 6, 1)

        self.product_car_models = self.create_line_edit('Uyumlu Araç Modelleri')
        form_layout.addWidget(self.create_label('Uyumlu Araç Modelleri'), 7, 0)
        form_layout.addWidget(self.product_car_models, 7, 1)

        self.product_size = self.create_line_edit('Boyut')
        form_layout.addWidget(self.create_label('Boyut'), 8, 0)
        form_layout.addWidget(self.product_size, 8, 1)

        self.product_category = self.create_combo_box(self.DB.category())
        form_layout.addWidget(self.create_label('Kategori'), 9, 0)
        form_layout.addWidget(self.product_category, 9, 1)

        self.image_label = QLabel()
        form_layout.addWidget(self.image_label, 0, 2, 10, 1)

        self.product_image_button = self.create_button('Ürün Resmi Seç', self.select_image)
        form_layout.addWidget(self.product_image_button, 10, 0, 1, 3)

        self.main_layout.addLayout(form_layout)

    def init_buttons(self):
        button_layout = QHBoxLayout()

        self.add_product_button = self.create_button('Add Product', self.add_product)
        button_layout.addWidget(self.add_product_button)

        self.main_layout.addLayout(button_layout)

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        return label

    def create_line_edit(self, placeholder, validator=None):
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        line_edit.setStyleSheet("padding: 6px; font-size: 16px; border: 1px solid #ccc; border-radius: 5px;")
        if validator:
            line_edit.setValidator(validator)
        return line_edit

    def create_combo_box(self, items):
        combo_box = QComboBox()
        for item in items:
            combo_box.addItem(item[1])
        combo_box.setStyleSheet("padding: 6px; font-size: 16px; border: 1px solid #ccc; border-radius: 5px;")
        return combo_box

    def create_button(self, text, callback):
        button = QPushButton(text)
        button.setStyleSheet("padding: 10px; font-size: 16px; background-color: #007BFF; color: white; border: none; border-radius: 5px;")
        button.clicked.connect(callback)
        return button

    def add_product(self):
        product_name = self.product_name.text()
        product_price = self.product_price.text()
        product_buy_price = self.product_buy_price.text()
        product_stock = self.product_stock.text()
        product_shelf = self.product_shelf.text()
        product_description = self.product_description.text()
        product_brand = self.product_brand.currentText()
        product_car_models = self.product_car_models.text()
        product_size = self.product_size.text()
        product_category = self.product_category.currentIndex() + 1
        product_image = self.imagebase64

        self.DB.add_product(
            product_name=product_name, 
            product_price=product_price, 
            alis_fiyati=product_buy_price, 
            stok_miktari=product_stock, 
            rafNumara=product_shelf, 
            urun_aciklamasi=product_description, 
            marka=product_brand, 
            uyumlu_arabalar=product_car_models, 
            ebat=product_size, 
            kategori_id=product_category, 
            urun_resim_url=product_image
        )

        QMessageBox.information(self, 'Başarılı', 'Ürün başarıyla eklendi.')
        self.accept()

    def select_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Resim Seç", "", "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp);;Tüm Dosyalar (*)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(pixmap)

            image_base64 = self.pixmap_to_base64(pixmap)
            QMessageBox.information(self, 'Başarılı', 'Resim başarıyla yüklendi ve kaydedildi.')
            self.imagebase64 = image_base64

    def pixmap_to_base64(self, pixmap):
        bytes_io = QByteArray()
        buffer = QBuffer(bytes_io)
        buffer.open(QBuffer.WriteOnly)
        pixmap.save(buffer, "PNG")
        return bytes_io.toBase64().data().decode()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = AddProduct()
    dialog.exec()
