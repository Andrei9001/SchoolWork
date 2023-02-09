import psycopg2
from flask import Flask, render_template, request, url_for, redirect
import pandas as pd
import json
import requests

#       & tiek apzīmēti jaunumi &

#Flask
app = Flask(__name__)
HOST_NAME = 'localhost'
HOST_PORT = 80

#Postgres SQL
conn_books = psycopg2.connect(user="postgres",
                        password="klase12",
                        host="127.0.0.1",
                        port="5432",
                        database="books_db")
conn_doc = psycopg2.connect(user="postgres",
                        password="klase12",
                        host="127.0.0.1",
                        port="5432",
                        database="medical")
cur_doc = conn_doc.cursor()

# Open a cursor to perform database operations
cur = conn_books.cursor()
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
)

# Insert data into the table
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )
conn_books.commit()
#tables
def database(dB):
  select_query = pd.read_sql_query('''select * from {}'''.format(dB),conn_doc)
  df = pd.DataFrame(select_query) 
  return df

#globals
name = ''
Mscript = ''

#routes
        # & Izveidoju login lapu, kas iegūst informāciju no randomuser.me API un kas atspoguļo lieotāju home lapā &
@app.route('/')
def login():
        global user
        global photo
        global Fname
        global Lname
        url = "https://randomuser.me/api/?format=json"
        user_url = requests.get(url, timeout=10)
        user_DIC = json.loads(user_url.text)
        name = user_DIC['results'][0]['name']
        Fname = name['first']
        Lname = name['last']
        user = name['title'] +' '+ Fname +' '+ Lname
        photo = user_DIC['results'][0]['picture']['large']
        return render_template('login.html', user=user, photo=photo)

@app.route('/home/')
def home():
  return render_template('home.html', user=user, photo=photo, fname=Fname)

@app.route('/index/')
def index():
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    return render_template('index.html', books=books,)

@app.route('/create/', methods=('GET', 'POST'))
def create():
        if request.method == 'POST':
                title = request.form['title']
                author = request.form['author']
                pages_num = int(request.form['pages_num'])
                review = request.form['review']
                cur.execute('INSERT INTO books (title, author, pages_num, review)'
                                'VALUES (%s, %s, %s, %s)',
                                (title, author, pages_num, review))
                conn_books.commit()
                cur.close()
                conn_books.close()
                return redirect(url_for('index'))
        return render_template('create.html')

@app.route('/meme/')
def meme():
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url, timeout=10)
        joke_dict = json.loads(response.text)
        joke = joke_dict["value"]
        return render_template('joke.html', joke=joke)

        # & Izveidoju lapu, kas iegūst informāciju no mājaslapas html koda &
@app.route('/about/', methods=['GET', 'POST'])
def about():
        global name; global Mscript
        cinema = ['Bee Movie','Shrek', 'Kung Fu Panda', 'Madagascar','Monsters vs Aliens', 'Monsters inc', 'Tresure Planet','Tarzan', ]
        if request.method == "POST":
                action = request.form.get("film")
                if action == "Bee Movie": movie = requests.get("http://www.script-o-rama.com/movie_scripts/a1/bee-movie-script-transcript-seinfeld.html").text
                elif action == "Shrek": movie = requests.get("http://www.script-o-rama.com/movie_scripts/s/shrek-script-transcript-mike-myers.html").text
                elif action == "Kung Fu Panda": movie = requests.get("http://www.script-o-rama.com/movie_scripts/k/kung-fu-panda-script-transcript.html").text
                elif action == "Madagascar": movie = requests.get("http://www.script-o-rama.com/movie_scripts/m/madagascar-script-transcript.html").text
                elif action == "Monsters vs Aliens": movie = requests.get("http://www.script-o-rama.com/movie_scripts/m/monsters-vs-aliens-script-transcript.html").text
                elif action == "Monsters inc": movie = requests.get("http://www.script-o-rama.com/movie_scripts/m/monsters-inc-script-transcript-pixar.html").text
                elif action == "Tresure Planet": movie = requests.get("http://www.script-o-rama.com/movie_scripts/t/treasure-planet-script-transcript-disney.html").text
                elif action == "Tarzan": movie = requests.get("http://www.script-o-rama.com/movie_scripts/t/tarzan-script-transcript-disney.html").text
                movie_text_raw = movie.split('<h2>')[1]
                movie_text_pre = movie_text_raw.split('</pre>')[0]
                name = movie_text_pre.split('</h2>')[0]
                Mscript = movie_text_pre.split('<pre>')[1]
                return render_template('about.html', name=name, Mscript=Mscript, colours=cinema)
        return render_template('about.html', name=name, Mscript=Mscript, colours=cinema)

@app.route("/doctor/")
def doctor():
  return render_template("doctor.html", tables=[database('doctor').to_html(classes='data')], titles=database('doctor').columns.values)


        # & Papildus python kodam, tika izveidotas jaunas html lapas, kā arī atjaunināts izskats pašreizējām lapām lietojot css &













app.run(HOST_NAME)





cur.close()
conn_books.close()
conn_doc.close()

