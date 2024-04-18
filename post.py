from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL 데이터베이스 설정
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_PORT'] = 3306  # 포트는 별도로 지정
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'user id'
app.config['MYSQL_DB'] = 'test_11'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    cur.close()
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
