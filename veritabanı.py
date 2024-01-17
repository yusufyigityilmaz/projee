import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_sayısı INT)")
    con.commit()
def veri_ekle():
    cursor.execute("INSERT INTO Kitaplık VALUES('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO Kitaplık VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def verileri_al():
    cursor.execute("SELECT * FROM Kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri...")
    for i in liste:
        print(i)
def verileri_al2():
    cursor.execute("SELECT İsim,Yazar FROM Kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri...")
    for i in liste:
        print(i)
def verileri_al3(yayinevi):
    cursor.execute("SELECT * FROM Kitaplık WHERE Yayınevi = ?",(yayinevi,))
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri...")
    for i in liste:
        print(i)
def verilerigüncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("UPDATE Kitaplık SET Yayınevi = ? WHERE Yayınevi = ? ",(yeni_yayinevi,eski_yayinevi))
    con.commit()
def verileri_sil(yazar):
    cursor.execute("DELETE FROM Kitaplık WHERE Yazar = ?",(yazar,))
    con.commit()

verilerigüncelle()



con.close()

