import psycopg2
import random

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
    for j in range(1000000):
        id = random.randint(10000,99999)
        pk = str(random.randint(0,12))+str()
        yn = bool(random.getrandbits(1))
        insert_query = """ INSERT INTO klienti (klienta_id, personas_kods, uzvards, talrunis, izbrauksanas_datums, samaksats, marsruta_id) values ({},{},{},{},2022-09-01,{},{})""".format(id,B,C,D,yn,G)
    
    
    marsruta_id = """INSERT INTO marsruti (marsruta_id, valsts, transports, ilgums_dienas) values ({}, 'LATVIJA', 'Volkswagen Type 2', 7) """.format(G)
    cursor.execute(marsruta_id)
    #insert_query = """INSERT INTO klienti (klienta_id, personas_kods, uzvards, talrunis, izbrauksanas_datums, samaksats, marsruta_id) values (42069,'050783-12345','Jurelonis','+37129501661','2022-09-01','false',010922)"""
    cursor.execute(insert_query)
    connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")