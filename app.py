from flask import Flask
app = Flask(__name__)
import os
import psycopg2


@app.route('/',methods=['POST'])
def myendpoint():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    incoming_msg = request.values.get('Body', '').lower()
    cur.execute("""INSERT INTO votes VALUES('%s')""",incoming_msg)
    cur.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app.run()
