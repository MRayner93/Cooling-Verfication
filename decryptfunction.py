import pyodbc
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Connection data
server = 'sc-db-server.database.windows.net'
database = 'supplychain'
username = 'rse'
password = 'Pa$$w0rd'

# Connection string
conn_str = (
f'DRIVER={{SQL Server}};'
f'SERVER={server};'
f'DATABASE={database};'
f'UID={username};'
f'PWD={password}'
)

# Password and padding password
key = b'mysecretpassword'  # 16 Byte password
iv = b'passwort-salzen!'  # 16 Byte initialization vector

# Cipher objects
cipher_company = AES.new(key, AES.MODE_CBC, iv)
cipher_transportstation = AES.new(key, AES.MODE_CBC, iv)

# Decryption function for the Company decryption
def decrypt_value_company(encrypted_data):
    return unpad(cipher_company.decrypt(encrypted_data), AES.block_size).decode()

# Decrypting Transportstation ID
def decrypt_value_transportstation(encrypted_data):
    return unpad(cipher_transportstation.decrypt(encrypted_data), AES.block_size).decode()

# Decryption for the Company database
def decryption_company(company_id):
    decrypted_list_company = []
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM company_crypt ')

# All data is fetched, decrypted, and then appended to the list
    for row in cursor.fetchall():
        company_id, encrypted_company, encrypted_street, encrypted_village, encrypted_plz  = row
        company_id = company_id
        decrypted_company = decrypt_value_company(encrypted_company)
        decrypted_list_company.append(decrypted_company)
        decrypted_street = decrypt_value_company(encrypted_street)
        decrypted_list_company.append(decrypted_street)      
    cursor.close()
    conn.close()
    return decrypted_list_company

# Decryption for the Transportstation database
def decryption_transportstation(transportstation_id):
    decryped_id_list = []
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transportstation_crypt')

# Perform decryption for each record and output
    for row in cursor.fetchall():
        id, encrypted_transportstation, encrypted_category, encrypted_plz = row
        test_id = row[0]
        decrypted_list = []
        decrypted_list.append(row[0])
        decrypted_transportstation = decrypt_value_transportstation(encrypted_transportstation)
        decrypted_list.append(decrypted_transportstation)
        decrypted_category = decrypt_value_transportstation(encrypted_category)
        decrypted_list.append(decrypted_category)
        decrypted_pls = decrypt_value_transportstation(encrypted_plz)
        decrypted_list.append(decrypted_pls)
        if test_id in transportstation_id :
            decryped_id_list.append(decrypted_list)

# Close connection
    cursor.close()
    conn.close()

    return decryped_id_list