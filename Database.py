import mysql.connector as mysql
import hashlib

class Database:
    """Database class for handling database operations"""
    def __init__(self):
        self.mydb = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database='celikler'
            )
        self.cursor = self.mydb.cursor()

    def add_product(self, product_name, product_price,alis_fiyati,stok_miktari,rafNumara,urun_resim_url,urun_aciklamasi,marka,uyumlu_arabalar,ebat,kategori_id):
        """Add product to database"""
        self.cursor.execute("INSERT INTO urunler (urun_adi, urun_fiyati,alis_fiyati,stok_miktari,rafNumara,urun_resim_url,urun_aciklamasi,marka,uyumlu_arabalar,ebat,kategori_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (product_name, product_price,alis_fiyati,stok_miktari,rafNumara,urun_resim_url,urun_aciklamasi,marka,uyumlu_arabalar,ebat,kategori_id))
        self.mydb.commit()

    def remove_product(self, product_id):
        """Remove product from database"""
        self.cursor.execute("DELETE FROM urunler WHERE product_id = %s", (product_id,))
        self.mydb.commit()

    def search_product(self, product_name):
        """Search for product in database"""
        self.cursor.execute("SELECT * FROM urunler WHERE product_name = %s", (product_name,))
        return self.cursor.fetchall()
    
    def get_products(self):
        """Get all products from database"""
        self.cursor.execute("SELECT * FROM urunler")
        return self.cursor.fetchall()
    
    def get_users(self):
        """Get all users from database"""
        self.cursor.execute("SELECT * FROM kullanicilar")
        return self.cursor.fetchall()
    
    def authenticate_user(self, username, password):
        """Authenticate user"""
        password = hashlib.sha3_256(password.encode()).hexdigest()
        self.cursor.execute("SELECT * FROM kullanicilar WHERE kullaniciAdi = %s AND sifre = %s", (username, password))
        return self.cursor.fetchone()
    
    def get_brands(self):
        """Get all brands from database"""
        self.cursor.execute("SELECT * FROM markalar")
        return self.cursor.fetchall()
    
    def category(self):
        """Get all categories from database"""
        self.cursor.execute("SELECT * FROM kategoriler")
        return self.cursor.fetchall()
    
    def search_products(self, search_query):
        # Veritabanında ürün arama işlemi yapılmalıdır.
        # Bu fonksiyon, arama kriterlerine uygun ürünleri döndürmelidir.
        query = """
                SELECT urun_adi, urun_fiyati, alis_fiyati, stok_miktari, rafNumara, urun_aciklamasi, marka, uyumlu_arabalar, ebat, oem,urun_id
                FROM urunler 
                WHERE 
                urun_adi LIKE %s OR
                rafNumara LIKE %s OR
                urun_aciklamasi LIKE %s OR
                marka LIKE %s OR
                uyumlu_arabalar LIKE %s OR
                ebat LIKE %s OR
                oem LIKE %s
                """
        search_terms = (f"%{search_query}%",) * 7
        self.cursor.execute(query, search_terms)
        return self.cursor.fetchall()
    
        # products = [
        #     {'product_id': 1, 'product_name': 'Ürün 1', 'product_price': 100, 'product_stock': 10},
        #     {'product_id': 2, 'product_name': 'Ürün 2', 'product_price': 200, 'product_stock': 5},
        #     {'product_id': 2, 'product_name': 'hamza', 'product_price': 200, 'product_stock': 5},
        # ]
        # return products

    def get_similar_products(self, product_id):
        # Veritabanında benzer ürünleri alma işlemi yapılmalıdır.
        # Bu fonksiyon, verilen ürün ID'sine benzer ürünleri döndürmelidir.
        query = """
        SELECT urun_adi, urun_fiyati, alis_fiyati, stok_miktari, rafNumara, urun_aciklamasi, marka, uyumlu_arabalar, ebat, oem FROM urunler 
        WHERE urun_id LIKE %s
        """
        self.cursor.execute(query, product_id)
        return self.cursor.fetchall()
        # similar_products = [
        #     {'product_name': 'Benzer Ürün 1', 'product_price': 90, 'product_stock': 8},
        #     {'product_name': 'Benzer Ürün 2', 'product_price': 110, 'product_stock': 6},
        #     {'product_name': 'hamza', 'product_price': 110, 'product_stock': 6},
        # ]
        # return similar_products
    
    def __del__(self):
        self.cursor.close()
        self.mydb.close()
# Path: admin/admin.py