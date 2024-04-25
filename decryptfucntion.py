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
f'DRIVER={{ODBC Driver 17 for SQL Server}};'
f'SERVER={server};'
f'DATABASE={database};'
f'UID={username};'
f'PWD={password}'
)

key = b'mysecretpassword'  # 16 Byte Passwort
iv = b'passwort-salzen!'  # 16 Byte Initialisierungsvektor

cipher_company = AES.new(key, AES.MODE_CBC, iv)
cipher_transportstation = AES.new(key, AES.MODE_CBC, iv)
cipher_temp = AES.new(key, AES.MODE_CBC, iv)

def decrypt_value_temp(encrypted_data):
    return unpad(cipher_temp.decrypt(encrypted_data),AES.block_size).decode()

def decrypt_value_company(encrypted_data):
    return unpad(cipher_company.decrypt(encrypted_data), AES.block_size).decode()

def decrypt_value_transportstation(encrypted_data):
    return unpad(cipher_transportstation.decrypt(encrypted_data), AES.block_size).decode()


def decryption_company(company_id):
    decrypted_list_company = []
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM company_crypt ')

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


#def decryption_temp_data(transportstation_id):
    #  decrypted_temp_data = []
     # conn = pyodbc.connect(conn_str)
   # cursor = conn.cursor()
    #cursor.execute('SELECT * FROM v_tempdata_crypt')

    #for row in cursor.fetchall():
     #   id, encrypted_transportstation, encrypted_category, datetime, temp = row
      #  decrypted_temp_data_cache = []
       # id = row[0]
        #decrypted_temp_data_cache.append(id)
        #decrypted_category = decrypt_value_temp(encrypted_category)
        #decrypted_temp_data_cache.append(decrypted_category)
        #if id in transportstation_id:
         #   decrypted_temp_data.append(decrypted_temp_data_cache)
            
    #return decrypted_temp_data    
            

def decryption_transportstationID_temp(temp_error_id):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('SELECT transportstation FROM v_tempdata_crypt WHERE transportstationID =?',(temp_error_id))
    encrypted_transportstation = cursor.fetchone()
    decrypted_transportstation_temp = decrypt_value_transportstation(encrypted_transportstation[0])
    cursor.close()
    conn.close()

    return decrypted_transportstation_temp

















