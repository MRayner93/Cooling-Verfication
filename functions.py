"""
Author: Leon van Stevendaal & Merlin Rayner
Version: 1.0
"""
from datetime import timedelta

# Function to check consistency = (Follows In after Out and Is the first entry an In)
def check_consistency(matrix):
    for i in range(len(matrix) - 1):
        if matrix[i][-2] == "'in'" and matrix[i+1][-2] != "'out'":
            return False, "In does not follow Out"
        
        if matrix[i][-2] == matrix[i+1][-2]:
            return False, f"Entry {i} and Entry {i+1} are both '{matrix[i][-2]}'"
        
    if matrix[0][-2] != "'in'":
        return False, "First entry is not an In"
    return True, ""

# Function to check the time stamps (Is the temporal sequence logical and were the 10 minutes adhered to)   
def check_time_difference(matrix): 
    for i in range(len(matrix) - 1):   
        if matrix[i][-2] == "'out'" and matrix[i+1][-2] == "'in'":
            time_out = matrix[i][-1]
            time_in = matrix[i+1][-1]
            time_difference = time_in - time_out
            transportstation_id = matrix[i][3]
            if time_difference > timedelta(minutes=10):
                return False, f"The time difference between ({time_out}) and ({time_in}) is more than 10 minutes", time_out, transportstation_id
    return True, "", time_out, transportstation_id

# Function to check if the transport duration of 48 hours has been adhered to
def check_transport_duration(matrix):
    first_time = matrix[0][-1]
    last_time = matrix[-1][-1]
    total_transport_duration = last_time - first_time
    if total_transport_duration > timedelta(hours=48):
        return False
    return True


def check_temp_data(temp_data, transportstation_id):
    for row in temp_data:
        if row[0] in transportstation_id:
            if not 2 <= row[-1] <= 4:
                temperature = row[-1]
                date = row[2]
                return False, f"The temperature ({temperature}) on date {date} for transport station ID {row[0]}, ({row[1]}) is not within the acceptable range of 2 to 4.",row[0]
    return True, "",""          

def weatherfunction_list(encrypted_transportstation, time_difference_id):
    weather_data_list = []
    for row in encrypted_transportstation:
        if row[-1] != "0":
            if row[0] == time_difference_id:
                cache_list = []
                cache_list.append(row[0])
                cache_list.append(row[-1])
                weather_data_list.append(cache_list)
    return weather_data_list



