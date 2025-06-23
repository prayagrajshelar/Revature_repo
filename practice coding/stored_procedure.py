import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='practice_db'
)

cursor = conn.cursor()

# Call the stored procedure with a parameter
min_salary = 25000
cursor.callproc('GetHighPaidEmployees', [min_salary])

# Fetch results
for result in cursor.stored_results():
    for row in result.fetchall():
        print(row)

# Clean up
cursor.close()
conn.close()
