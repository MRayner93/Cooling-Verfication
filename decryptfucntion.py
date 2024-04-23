from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'mysecretpassword'  # 16 Byte Passwort
iv = b'passwort-salzen!'  # 16 Byte Initialisierungsvektor
cipher = AES.new(key, AES.MODE_CBC, iv)

def decrypt_value(encrypted_data):
        return unpad(cipher.decrypt(encrypted_data), AES.block_size).decode()

def decryption_company(company_data):
    decrypted_list_company = []
    extracted_list = company_data[0] 

    for item in extracted_list:
        if isinstance(item, bytes):
            try:
                decrypted_value = decrypt_value(item)
                print("The decryption was successful")
                decrypted_list_company.append(decrypted_value)
            except Exception as e:
                print(e) 
        else:
            decrypted_list_company.append(item)

    return decrypted_list_company

def decryption_transportstation(transportstation_data):
    decrypted_list_transportstation = []

    extracted_list = transportstation_data[3] 

    for item in extracted_list:
        if isinstance(item, bytes):
            try:
                decrypted_value = decrypt_value(item)
                print("The decryption was successful")
                decrypted_list_transportstation.append(decrypted_value)
            except Exception as e:
                print(e) 
        else:
            decrypted_list_transportstation.append(item)

    return decrypted_list_transportstation
























