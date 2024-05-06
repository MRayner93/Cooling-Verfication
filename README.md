## Cooling Verifaction

This Python program is a comprehensive solution for monitoring and verifying cold chains by analyzing data from a SQL database. It utilizes a connection to the database to identify specific transport operations and verify if they meet the established requirements. This project was developed as part of a trainee program for certified technicians.

## Table of Contents

1. [Features](#features)
2. [Usage](#Usage)
3. [License](#license)


## Features

 1. Database Connection: Initializes a connection to a SQL database using the "pyodbc" library to access transport data.
 2. Retrieval and Selection of Transport IDs: Extracts a list of all transport IDs from the database and allows the user to select a specific ID for inspection.
 3. Data Extraction: For the selected transport ID, retrieves all associated records from the database and writes them into another list.
 4. Analysis by Subprograms: The program utilizes three specialized functions to check the integrity and efficiency of the transport. The explanation of these functions is provided on the next page.
 5. Result Evaluation: Informs the user about the outcome of the checks. In case of violations against the criteria, detailed warning messages are issued.
 6. Repeatable Checks: The program runs in a continuous loop, allowing to choose a new transport ID after each analysis and repeat the inspection.

## Usage

   1. Install ODBC Driver on your Windows Computer (https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)
    1.1 OR: Install ODBC Driver on your Linux Computer(https://learn.microsoft.com/de-de/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=debian18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline)
   2. Change the connection data and ODBC Driver in the main.py
   3. Install cryptodome with pip install
   4. Run the program   

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code.
