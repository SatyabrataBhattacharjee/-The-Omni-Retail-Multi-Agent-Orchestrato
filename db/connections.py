import pyodbc

def get_shopcore_conn():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=QTECH360\\SQLEXPRESS;"
        "DATABASE=DB_ShopCore;"
        "Trusted_Connection=yes;"
    )

def get_shipstream_conn():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=QTECH360\\SQLEXPRESS;"
        "DATABASE=DB_ShipStream;"
        "Trusted_Connection=yes;"
    )

def get_payguard_conn():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=DB_PayGuard;"
        "Trusted_Connection=yes;"
    )
def get_caredesk_conn():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=DB_CareDesk;"
        "Trusted_Connection=yes;"
    )


