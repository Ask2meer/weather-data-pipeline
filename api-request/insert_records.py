import psycopg2
from api_request import fetch_data


def connect_to_db():
    print("Connecting to PostgreSQL Database ...")
    try:
        conn = psycopg2.connect(
            host="db",       # Docker exposes PostgreSQL to this host
            port="5432",            # The port you mapped in docker-compose.yml
            database="db", # Your POSTGRES_DB value
            user="db_user",         # Your POSTGRES_USER value
            password="db_password"  # Your POSTGRES_PASSWORD value
        )
        print("Connection successful!")
        return conn

    except psycopg2.Exception as e:
        print("Error connecting to the database:", e)
        raise


def create_table(conn):
    """Create a table if it does not exist."""
    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS dev;
        CREATE TABLE IF NOT EXISTS dev.raw_weather_data(
            id SERIAL PRIMARY KEY,
            city TEXT,
            temperature FLOAT,
            weather_description TEXT,
            wind_speed FLOAT,
            time TIMESTAMP,
            inserted_at TIMESTAMP DEFAULT NOW(),
            utc_offset TEXT
        );
        """)
        conn.commit()
        print("Table created successfully or already exists.")  

    except psycopg2.Error as e:
        print("Failed to create table:", e)
        raise
  


def insert_records(conn,data):
    print("Inserting weather data into the database.")
    try:
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                       city,
                       temperature,
                       weather_description,
                       wind_speed,
                       time,
                       inserted_at,
                       utc_offset
            ) VALUES (%s, %s, %s, %s,%s, NOW(), %s)
        """,(
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print("Data inserted successfully.")    
    except psycopg2.Error as e:
        print(f"Failed to insert weather data:", {e})
        raise

    


def main():
    try:
        #data = mock_data_fetch()
        data = fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)

    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")    


 