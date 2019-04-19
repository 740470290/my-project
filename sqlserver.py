import pymssql
from flask import Flask,render_template
import config
app = Flask(__name__)

@app.route('/')
def home():
  conn = pymssql.connect(config.server, config.user, config.pwd, config.database)
  cursor = conn.cursor()
  cursor.execute('SELECT locate_st FROM dbo.VIEW_IWMS_LOCATE')
  row = cursor.fetchall()
  ls = [0, 0, 0]
  length = len(row)
  for i in range(length):
    if row[i][0] == '0':
      ls[0] = ls[0] + 1
    elif row[i][0] == '1':
      ls[1] = ls[1] + 1
    else:
      ls[2] = ls[2] + 1
  cursor.close()
  conn.close()
  info = ['未分配','已分配','已占用']
  return render_template('sqlser.html', list=ls,info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8081)
