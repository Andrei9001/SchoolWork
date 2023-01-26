import psycopg2
from psycopg2 import Error
import datetime
from dateutil.relativedelta import relativedelta

#   Savienojums
connection = psycopg2.connect(user="postgres",
                        password="klase12",
                        host="127.0.0.1",
                        port="5432",
                        database="medical")
cursor = connection.cursor()

#   Pārbaudes def
def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

#   Pārbauda vai eskistē "hospital" tabula un pievieno vajadzīgos failus
if checkTableExists(connection, "hospital") == False:
    table = """CREATE TABLE Hospital (
        Hospital_Id serial NOT NULL PRIMARY KEY, 
        Hospital_Name VARCHAR (100) NOT NULL, 
        Bed_Count serial);"""
    cursor.execute(table)
    doctors = """INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_Count) 
    VALUES 
    ('1', 'Mayo Clinic', 200), 
    ('2', 'Cleveland Clinic', 400), 
    ('3', 'Johns Hopkins', 1000), 
    ('4', 'UCLA Medical Center', 1500);"""
    cursor.execute(doctors)
    connection.commit()

#   Pārbauda vai eskistē "doctors" tabula un pievieno vajadzīgos failus
if checkTableExists(connection, "doctor") == False:
    doctor = """CREATE TABLE Doctor ( 
        Doctor_Id serial NOT NULL PRIMARY KEY, 
        Doctor_Name VARCHAR (100) NOT NULL, 
        Hospital_Id serial NOT NULL, 
        Joining_Date DATE NOT NULL, 
        Speciality VARCHAR (100) NOT NULL, 
        Salary INTEGER NOT NULL,
        Experience SMALLINT );"""
    doc = """INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary, Experience) 
    VALUES 
    ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', NULL), 
    ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', NULL), 
    ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', NULL), 
    ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', NULL), 
    ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', NULL), 
    ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', NULL), 
    ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', NULL), 
    ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', NULL);"""
    cursor.execute(doctor)
    cursor.execute(doc)
    connection.commit()

def printer(row):
    print("Doctor Id: ", row[0])
    print("Doctor Name:", row[1])
    print("Hospital Id:", row[2])
    print("Joining Date:", row[3])
    print("Specialty:", row[4])
    print("Salary:", row[5])
    print("Experience: {} ".format(row[6]))

def get_hospital_detail(hospital_id):
    select_query = """select * from Hospital where Hospital_Id = %s"""
    cursor.execute(select_query, (hospital_id,))
    records = cursor.fetchall()
    print("Printing Hospital record")
    for row in records:
        print("Hospital Id:", row[0])
        print("Hospital Name:", row[1])
        print("Bed Count:", row[2],"\n")

def get_doctor_detail(doctor_id):
    select_query = """select * from doctor where doctor_id = %s"""
    cursor.execute(select_query, (doctor_id,))
    records = cursor.fetchall()
    print("Printing Doctor record")
    for row in records:
        printer(row); print("\n")

def get_specialist_doctors_list(speciality, salary):
    select_query = """select * from doctor where speciality='{}' and salary > {}""".format(speciality,salary)
    cursor.execute(select_query)
    for row in cursor.fetchall():
        printer(row); print("\n")

def get_doc(x):
    y = """SELECT * FROM doctor WHERE hospital_id={}""".format(x)
    z = """SELECT * FROM hospital WHERE hospital_id = {}""".format(x)
    cursor.execute(y)
    d = cursor.fetchall()
    cursor.execute(z)
    s = cursor.fetchall()
    for row in d:
        printer(row)
        for row in s:
            print("Working at: {} \n".format(row[1]))

def update_doctor_exp(x):
    select_query = """select Joining_Date from Doctor where Doctor_Id = %s"""
    cursor.execute(select_query, (x,))
    joining_date = cursor.fetchone()
    joining_date_1 = datetime.datetime.strptime(''.join(map(str, joining_date)), '%Y-%m-%d')
    today_date = datetime.datetime.now()
    experience = relativedelta(today_date, joining_date_1).years
    sql_select_query = """update Doctor set Experience = %s where Doctor_Id =%s"""
    cursor.execute(sql_select_query, (experience, x))
    connection.commit()
    get_doctor_detail(x)



get_hospital_detail(3)
get_doctor_detail(101)
get_specialist_doctors_list("Garnacologist", 30000)
get_doc(2)
go = """select experience from doctor"""
cursor.execute(go)
ho = cursor.fetchall()
if "(None,)" == str(ho[1]):
    for i in range(101,109):
        update_doctor_exp(i)
    print("ayo Mr.White")
else:
    print("everything ok")
    non = """UPDATE doctor SET experience = null where doctor_id > 1 """
    cursor.execute(non)
    connection.commit()

cursor.execute("SELECT version();")
db_version = cursor.fetchone()
print("Datubāzes versija:",db_version)