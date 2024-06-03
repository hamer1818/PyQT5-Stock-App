from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

# ...

class SearchProduct(QDialog):
    # ...

    def search_product(self):
        # ...

        # Create a QTableWidget with 10 columns
        self.results_table = QTableWidget(0, 10)
        self.results_table.setHorizontalHeaderLabels(['Ürün Adı', 'Satış Fiyatı', 'Alış Fiyatı', 'Stok Miktarı', 'Raf Numarası', 'Ürün Açıklaması', 'Marka', 'Uyumlu Arabalar', 'Ebat', 'OEM'])

        # Add the product to the table
        self.add_product_to_table(product)

        # Add similar products to the table
        similar_products = self.DB.get_similar_products([product[10]])
        if similar_products:
            for similar_product in similar_products:
                self.add_product_to_table(similar_product)

        # Add the table to the layout
        self.layout.addWidget(self.results_table)

    def add_product_to_table(self, product):
        # Create a new row at the end of the table
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)

        # Add the product data to the row
        for i in range(10):
            self.results_table.setItem(row, i, QTableWidgetItem(str(product[i])))

# ...