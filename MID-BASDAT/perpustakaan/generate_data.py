import random
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="basdat_perpustakaan"
)

cursor = conn.cursor()

def random_isbn(i):
    return f"978-{i:013d}"[:17]  

def generate_tahun():
    while True:
        tahun = int(random.gauss(2010, 15))
        if 1900 <= tahun <= 2025:
            return tahun

TOTAL_DATA = 10000000  

for i in range(TOTAL_DATA):
    isbn = random_isbn(i)
    judul = f"Buku {i}"
    pengarang = f"Pengarang {random.randint(1,1000)}"
    penerbit = f"Penerbit {random.randint(1,1000)}"
    tahun = generate_tahun()
    stok = random.randint(1,100)
    harga = random.randint(1000,50000)

    cursor.execute("""
        INSERT INTO buku (isbn, judul, pengarang, penerbit, tahun_terbit, stok, harga_sewa)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (isbn, judul, pengarang, penerbit, tahun, stok, harga))

    if i % 10000 == 0:
        conn.commit()
        print(f"{i} data inserted...")

conn.commit()