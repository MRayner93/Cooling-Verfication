"""
Author: Leon van Stevendaal & Merlin Rayner & Stefan Moormann & Leon Deupmann & Yannik Helms & Sebastian Klockgether
Version: 1.0
"""
import pyodbc
import databasefunctions, decryptfunction, weatherfunction

# Connection data
server = 'sc-db-server.database.windows.net'
database = 'supplychain' 
username = 'rse'
password = 'Pa$$w0rd'

# Define connection string
conn_str = (
f'DRIVER={{SQL Server}};'
f'SERVER={server};'
f'DATABASE={database};'
f'UID={username};'
f'PWD={password}'
)

while True:
    # Establish connection
    conn = pyodbc.connect(conn_str)
    # Create cursor
    cursor = conn.cursor()
    
    
    # Initialize matrix for data
    all_data = []   
    all_transport_id_list = []  
    transport_id_list=[] 
    company_id= []
    transportstation_id = []
    transportstation_data = []
    temp_data = []

    # Retrieve existing Transport IDs from the database
    cursor.execute('SELECT transportid FROM coolchain')
    for row in cursor:
        all_transport_id_list.append(row[0])
    for id in all_transport_id_list:
        if id not in transport_id_list:
            transport_id_list.append(id)
    

    # User input for selecting the Transport ID
    while True:
        for i, transport_id in enumerate(transport_id_list, start=1):
            print(f"{i}. {transport_id}")
        entry = int(input("Which entry do you want to check? (1-" + str(len(transport_id_list)) + ") "))
        if 1 <= entry <= len(transport_id_list):
            transport_id = transport_id_list[entry-1]
            break
        else:
            print("Invalid input. Please choose a number between 1 and", len(transport_id_list))
    
    # Execute SQL query, sorted by the previously selected Transport ID       
    cursor.execute('SELECT * FROM coolchain WHERE transportid = ? ORDER BY datetime', transport_id )
    # Save results
    for row in cursor:
        all_data.append(row)
 
    # How many transport station IDs do we have?
    for j in range(len(all_data)-1):
        if all_data[j][-3] not in transportstation_id:
            transportstation_id.append(all_data[j][-3]) 
    
    # Placeholder for further functionality (KEEP AS IS)
    #company_id = all_data[0][1]

    # Write all temperature data into temp_data
    cursor.execute('SELECT transportstationID, transportstation, datetime, temperature FROM v_tempdata')
    for row in cursor:
        temp_data.append(row)

   # Close connection and cursor
    cursor.close()
    conn.close()
    
    # Temperature check for the refrigeration units
    check_temp_data_result, check_temp_error,temp_error_id = databasefunctions.check_temp_data(temp_data, transportstation_id)
    # Decrypting transport stations
    encrypted_transportstation = decryptfunction.decryption_transportstation(transportstation_id)
    # Transfer encrypted company data to decryptfunction
    encrypted_company_data = decryptfunction.decryption_company(company_id)  
    # Check for cold chain consistency
    consistency_result, consistency_error = databasefunctions.check_consistency(all_data)
    # Check time difference
    time_difference_result, time_difference_error, time_out, time_difference_id = databasefunctions.check_time_difference(all_data)
    # Check transport duration
    transport_duration_result = databasefunctions.check_transport_duration(all_data)
    
    # If the time is not right, then check the weather
    if time_difference_result == False:
        weather_data_list = databasefunctions.weatherfunction_list(encrypted_transportstation, time_difference_id )
    # Check the weather in case of time differenz problems
        temperature_during_day = weatherfunction.check_weather(weather_data_list, time_out)
    if consistency_result and time_difference_result and transport_duration_result and check_temp_data_result:
        print("The ID", transport_id, "is \033[1;32;4mcorrect\033[0m.")
    else:
        # If an error occurred, print the corresponding error messages
        print("The ID", transport_id," has the following issues.")
        if not consistency_result:
            print(f"\033[1;31;4mWarning:\033[0m The cold chain has consistency errors: {consistency_error}")
        if not time_difference_result:
            print(f"\033[1;31;4mWarning:\033[0m {time_difference_error}")
            print("The temperatur during the transport was",temperature_during_day,"celcius")
        if not check_temp_data_result:
            print(f"The temperature check has failed : {check_temp_error} ")                
        if not transport_duration_result:
            print("\033[1;31;4mWarning:\033[0m The transport duration exceeded 48 hours.")
    break  