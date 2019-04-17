import pymssql
from flask import Flask,render_template,request
from flask import jsonify
from flask_cors import CORS
import json,time
import config
app = Flask(__name__)

@app.route('/')
def home():
  conn = pymssql.connect(config.server, config.user, config.pwd, config.database)
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM dbo.test')
  row = cursor.fetchall()
  list=json.dumps(row)
  cursor.close()
  conn.close()
  return render_template('sqlser.html', list=list)

if __name__ == '__main__':
    app.run(debug=True)
