import pyodbc

def get_connection():
    server = 'DESKTOP-E15UN3T'  # Replace with your server name
    database = 'AuctionDB'  # Replace with your database name
    connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
        return None
