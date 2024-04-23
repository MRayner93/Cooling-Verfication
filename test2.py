# Bibliotheken
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
# Initialisierung
key = b'mysecretpassword' # 16 Byte Passwort
iv = b'passwort-salzen!' # 16 Byte Initialization Vektor
cipher = AES.new(key, AES.MODE_CBC, iv) # Verschlüsselung initialisieren
# Entschlüsselung
ciphertext = b'\xb1Fj\x99\x83\x87\xcb1\xed\xd1\xa2\th`\xeaAbq\x11a\xc1\xbasEsZX\xa6\xf8z\x1ee'
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size) # Text entschlüsseln
# Ausgabe
print ('--------------------------------------------------------------------------')
print ("Entschlüsselter Text als Bytewert: ", plaintext)
print ("Entschlüsselter Text als String: ", plaintext.decode())
print ('--------------------------------------------------------------------------')