# Tkinter Pencere Ayarları
import tkinter
from password import sifre_coz ,sifreleme
form = tkinter.Tk()
form.title("Şifreli Notlar")
form.minsize(width=800, height=500)

# Başlık Etiketi
label_title = tkinter.Label(text="Başlık Girin", background="white", foreground="black")
label_title.pack(pady=20)

# Başlık Giriş Kutusu
entry1 = tkinter.Entry()
entry1.pack(pady=10)
entry1.focus()

# Metin Etiketi
label2 = tkinter.Label(text="Metninizi Girin", background="white", foreground="black")
label2.pack(pady=10)

# Metin Alanı
text1 = tkinter.Text(width=40, height=10)
text1.pack(pady=10)

# Şifre Etiketi
label_password = tkinter.Label(text="Şifrenizi Girin", background="white", foreground="black")
label_password.pack(pady=10)

# Şifre Giriş Kutusu
entry2 = tkinter.Entry(show="*")  # Şifreyi gizler
entry2.pack(pady=10)


# 📥 Kaydet ve Şifrele Fonksiyonu
def fonk():
    password = entry2.get()
    if not password:
        print("Lütfen bir şifre girin!")
        return

    metin = text1.get("1.0", tkinter.END).strip()  # Metni al
    if metin:
        sifrelenmis_metin = sifreleme(metin, password)  # Şifreleme
        with open("myfile.txt", mode="w") as emel:
            emel.write(sifrelenmis_metin)
        print("Metin şifrelendi ve dosyaya kaydedildi.")
    else:
        print("Metin alanı boş!")


# 📖 Şifreyi Çözme Fonksiyonu
def sifre_coz_fonk():
    password = entry2.get()
    if not password:
        print("Lütfen bir şifre girin!")
        return

    try:
        with open("myfile.txt", mode="r") as myfile:
            my_content = myfile.read()

        metin_son = sifre_coz_fonk(my_content, password)  # Çözme
        text1.delete("1.0", tkinter.END)
        text1.insert(tkinter.END, metin_son)
        print("Şifre başarıyla çözüldü.")
    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except Exception as e:
        print("Şifre çözme hatası:", str(e))


# ✅ Butonlar
button1 = tkinter.Button(text="Kaydet ve Şifrele", command=fonk, background="black", foreground="white", width=20)
button1.pack(pady=20)

button2 = tkinter.Button(text="Şifreyi Çöz", command=sifre_coz_fonk, background="black", foreground="white", width=20)
button2.pack(pady=10)

# Tkinter Ana Döngü
form.mainloop()
