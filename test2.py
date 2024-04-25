# Bibliotheken
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
# Initialisierung
key = b'mysecretpassword' # 16 Byte Passwort
iv = b'passwort-salzen!' # 16 Byte Initialization Vektor
cipher = AES.new(key, AES.MODE_CBC, iv) # Verschlüsselung initialisieren
# Entschlüsselung
ciphertext = b'\x0b\x1c\x8e\x0e#\xae\xc8 \xc4\\\xf0\xdf\x15\x90\xe13'
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size) # Text entschlüsseln
# Ausgabe
print ('--------------------------------------------------------------------------')
print ("Entschlüsselter Text als Bytewert: ", plaintext)
print ("Entschlüsselter Text als String: ", plaintext.decode())
print ('--------------------------------------------------------------------------')