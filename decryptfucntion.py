import pyodbc
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Verbindungsdaten
server = 'sc-db-server.database.windows.net'
database = 'supplychain'
username = 'rse'
password = 'Pa$$w0rd'
# Verbindungsstring
conn_str = (
f'DRIVER={{ODBC Driver 18 for SQL Server}};'
f'SERVER={server};'
f'DATABASE={database};'
f'UID={username};'
f'PWD={password}'
)

key = b'mysecretpassword'  # 16 Byte Passwort
iv = b'passwort-salzen!'  # 16 Byte Initialisierungsvektor
cipher = AES.new(key, AES.MODE_CBC, iv)

def decrypt_value(encrypted_data):
    
    return unpad(cipher.decrypt(encrypted636_data), AES.block_size).decode()


def decryption_company(company_id):
    decrypted_list_company = []
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM company_crypt ')

    for row in cursor.fetchall():
        company_id, encrypted_company, encrypted_street, encrypted_village, encrypted_plz  = row
        company_id = company_id
        decrypted_company = decrypt_value(encrypted_company)
        decrypted_street = decrypt_value(encrypted_street)
        
    cursor.close()
    conn.close()
    return decrypted_list_company



def decryption_transportstation(transportstation_id):
    decryped_id_list = []
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transportstation_crypt')
# Für jeden Datensatz die Entschlüsselung durchführen und ausgeben
    for row in cursor.fetchall():
        id, encrypted_transportstation, encrypted_category, encrypted_plz = row
# Da die Daten als binär gespeichert wurden, sollte hier keine Umwandlung mit str() erfolgen
        test_id = row[0]
        decrypted_list = []
        decrypted_list.append(row[0])
        decrypted_transportstation = decrypt_value(encrypted_transportstation)
        decrypted_list.append(decrypted_transportstation)
        decrypted_category = decrypt_value(encrypted_category)
        decrypted_list.append(decrypted_category)
        decrypted_pls = decrypt_value(encrypted_plz)
        decrypted_list.append(decrypted_pls)
        if test_id in transportstation_id :
            decryped_id_list.append(decrypted_list)

# Close connection
    cursor.close()
    conn.close()

    return decryped_id_list
























