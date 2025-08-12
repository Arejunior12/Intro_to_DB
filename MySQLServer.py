import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (change credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',        # Change to your MySQL username
            password='your_password'  # Change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
