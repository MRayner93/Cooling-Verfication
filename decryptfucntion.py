from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decryption(company_data):
    decrypted_list = []
    extracted_list = company_data[0]
    key = b'mysecretpassword'  # 16 Byte Passwort
    iv = b'passwort-salzen!'  # 16 Byte Initialisierungsvektor
    cipher = AES.new(key, AES.MODE_CBC, iv)

    def decrypt_value(encrypted_data):
        return unpad(cipher.decrypt(encrypted_data), AES.block_size).decode()

    
    for item in extracted_list:
        if isinstance(item, bytes):
            try:
                decrypted_value = decrypt_value(item)
                print("The decryption was successful")
                decrypted_list.append(decrypted_value)
            except Exception as e:
                print(e)  # Hier sollte eine geeignete Fehlerbehandlung implementiert werden
        else:
            decrypted_list.append(item)

    return decrypted_list


























