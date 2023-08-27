# Youtube video with details of how https://www.youtube.com/watch?v=3Jf4FnSWytU&t=298s 

# effectively the pyodbc library allows you to execute SQL commands in SSMS
# The SQL goes in quotes in the cusor.execute method eg cursor.execute("Select * from TableName")
# Then need to call different methods to create, read, update, delete eg read(conn)

from sqlite3 import Cursor
from venv import create #creates a virtual environment
import pyodbc # connects to servers

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("SELECT * From dbo.Customer")
    for row in cursor:
        print(f'row= {row}')
    print()

def create(conn):
    print("Create")
    cursor = conn.cursor()
    CustomerNum = input('Enter Customer Number: ')
    CustomerName = input('Enter Customer Name: ')
    RepNum = input('Enter Rep Number: ')
    
    cursor.execute("INSERT INTO dbo.Customer(CustomerName, CustomerNum, RepNum) values(?, ?, ?)", (CustomerName), (CustomerNum), (RepNum))

    conn.commit()
    read(conn)

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LAPTOP-R7U57JKB;"
    "Database=premiere;"
    "Trusted_Connection=yes;"
 )

create(conn)
read(conn)

conn.close()
       

