from faker import Faker
import mysql.connector
import random
from datetime import datetime, timedelta

fake = Faker('id_ID')

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="basdat_toko_online"
)

cursor = conn.cursor()

# DATA REFERENSI
kota_list = [
    "Jakarta","Bandung","Surabaya","Medan","Makassar",
    "Yogyakarta","Semarang","Denpasar","Palembang","Balikpapan"
]

kategori_list = [
    "Elektronik","Pakaian","Buku","Makanan","Olahraga",
    "Kesehatan","Mainan","Otomotif"
]

# 1. INSERT PELANGGAN
print("Insert pelanggan...")
for i in range(100000):
    nama = fake.name()
    email = fake.unique.email()
    kota = random.choice(kota_list)
    tgl = fake.date_between(start_date='-2y', end_date='today')

    cursor.execute("""
        INSERT INTO pelanggan (nama, email, kota, tgl_daftar)
        VALUES (%s, %s, %s, %s)
    """, (nama, email, kota, tgl))

    if i % 1000 == 0:
        conn.commit()

conn.commit()

# 2. INSERT PRODUK
print("Insert produk...")
for i in range(100000):
    nama_produk = fake.word().capitalize() + " " + fake.word().capitalize()
    kategori = random.choice(kategori_list)
    harga = random.randint(10000, 5000000)
    stok = random.randint(1, 500)

    cursor.execute("""
        INSERT INTO produk (nama_produk, kategori, harga, stok)
        VALUES (%s, %s, %s, %s)
    """, (nama_produk, kategori, harga, stok))

    if i % 1000 == 0:
        conn.commit()

conn.commit()

# 3. INSERT TRANSAKSI
print("Insert transaksi...")
for i in range(100000):
    id_pelanggan = random.randint(1, 100000)
    id_produk = random.randint(1, 100000)
    qty = random.randint(1, 5)

    harga_satuan = random.randint(10000, 5000000)
    total = qty * harga_satuan

    tgl = fake.date_time_between(start_date='-1y', end_date='now')

    cursor.execute("""
        INSERT INTO transaksi (id_pelanggan, id_produk, qty, total_harga, tgl_transaksi)
        VALUES (%s, %s, %s, %s, %s)
    """, (id_pelanggan, id_produk, qty, total, tgl))

    if i % 1000 == 0:
        conn.commit()

conn.commit()

cursor.close()
conn.close()

print("SELESAI SEMUA 🚀")