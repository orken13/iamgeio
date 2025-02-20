import tkinter as tk
from hashlib import sha256

# Basit Şifreleme ve Çözme (Şifreye Bağlı)
def sifreleme(metin, password):
    """Kullanıcının şifresine bağlı olarak metni şifreler."""
    sifre_hash = sha256(password.encode()).hexdigest()  # Şifreyi hashle
    sifrelenmis_metin = ''.join(chr(ord(c) + int(sifre_hash[i % len(sifre_hash)], 16) % 26)
                                if c.isalpha() else c for i, c in enumerate(metin))
    return sifrelenmis_metin


def sifre_coz(metin, password):
    """Kullanıcının şifresine bağlı olarak metni çözer."""
    sifre_hash = sha256(password.encode()).hexdigest()  # Şifreyi hashle
    cozulmus_metin = ''.join(chr(ord(c) - int(sifre_hash[i % len(sifre_hash)], 16) % 26)
                             if c.isalpha() else c for i, c in enumerate(metin))
    return cozulmus_metin
