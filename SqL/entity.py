import psycopg2

id = 1
pk = 0
uv = " "
nr = 0



try:
    connection = psycopg2.connect(user="postgres",
                                  password="klase12",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    # Executing a SQL query to insert data into  table
    #for j in range(1000000):
    #    insert_query = """ INSERT INTO Klienti (Klienta_ID, Personas_kods, Uzvards, Talrunis, Izbrauksanas_datums, Samaksats, Marsruta_ID) VALUES ({},{},{},{},10.11.2022)"""
    marsruta_id = """INSERT INTO marsruti (marsruta_id, valsts, transports, ilgums_dienas) values (010922, 'LATVIJA', 'Volkswagen Type 2', 7) """
    cursor.execute(marsruta_id)
    insert_query = """INSERT INTO klienti (klienta_id, personas_kods, uzvards, talrunis, izbrauksanas_datums, samaksats, marsruta_id) values (42069,'050783-12345','Jurelonis','+37129501661','2022-09-01','false',010922)"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 Record inserted successfully")
    # Fetch result
    cursor.execute("SELECT * from mobile")
    record = cursor.fetchall()
    print("Result ", record)

    # Executing a SQL query to update table
    update_query = """Update mobile set price = 1500 where id = 1"""
    cursor.execute(update_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record updated successfully ")
    # Fetch result
    cursor.execute("SELECT * from mobile")
    print("Result: ")
    for i in range(100):
        cursor.fetchone()

    '''# Executing a SQL query to delete table
    delete_query = """Delete from mobile where id = 1"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record deleted successfully ")
    # Fetch result
    cursor.execute("SELECT * from mobile")
    print("Result ", cursor.fetchall())'''


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")