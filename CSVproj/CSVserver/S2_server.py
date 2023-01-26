# (A) INIT
# (A1) LOAD MODULES
from flask import Flask, render_template
import csv
import psycopg2
import pandas as pd
 
# (A2) FLASK SETTINGS + INIT
HOST_NAME = "localhost"
HOST_PORT = 80
app = Flask(__name__)
# app.debug = True

cv = int(input('Ievadīt 1 priekš CSV un 0 priekš SQL: '))

connection = psycopg2.connect(user="postgres",
                        password="klase12",
                        host="127.0.0.1",
                        port="5432",
                        database="medical")
cursor = connection.cursor()

def database(dB):
  select_query = pd.read_sql_query('''select * from {}'''.format(dB),connection)
  df = pd.DataFrame(select_query) 
  return df

# (B) DEMO - READ CSV & GENERATE HTML TABLE
@app.route("/")
def index():
  if cv == 1:
    with open("S1_dummy.csv") as file:
      reader = csv.reader(file)
      header = next(reader)
      return render_template("S3_csv.html", header=header, rows=reader)
  else:
    return render_template("S3_sql.html", tables=[database('doctor').to_html(classes='data')], titles=database('doctor').columns.values)

# (C) START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)


  
