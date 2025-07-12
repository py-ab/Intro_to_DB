import mysql.connector
    


   # Replace with your actual MySQL credentials
mydb = mysql.connector.connect(
       host="localhost",          # Or your MySQL server address
       user="yourusername",       # Your MySQL username (e.g., "root")
       password="yourpassword",   # Your MySQL password
       database="alx_book_store"  # The database you created
   )

if mydb.is_connected():
       print("Successfully connected to MySQL database")

       # Example: Creating a cursor to execute SQL queries
       mycursor = mydb.cursor()

       # Example: Execute a simple query
       mycursor.execute("SELECT * FROM Authors")

       # Fetch the results
       myresult = mycursor.fetchall()

       # Print the results
       for row in myresult:
           print(row)

else:
       print("Failed to connect to MySQL database")

   # Close the connection when done
if mydb.is_connected():
       mycursor.close()
       mydb.close()
       print("Connection closed.")
