import pymssql
from flask import Flask,render_template
import config
app = Flask(__name__)

@app.route('/')
def home():
  conn = pymssql.connect(config.server, config.user, config.pwd, config.database1)
  cursor = conn.cursor()
  cursor.execute('SELECT locate_st FROM dbo.VIEW_IWMS_LOCATE')
  row = cursor.fetchall()
  list = [0, 0, 0]
  length = len(row)
  for i in range(length):
    if row[i][0] == '0':
      list[0] = list[0] + 1
    elif row[i][0] == '1':
      list[1] = list[1] + 1
    else:
      list[2] = list[2] + 1
  cursor.close()
  conn.close()
  info = ['未分配','已分配','已占用']

  conn2 = pymssql.connect(config.server, config.user, config.pwd, config.database2)
  cursor2 = conn2.cursor()
  cursor2.execute('SELECT TRK_TP,CREATE_DATE FROM dbo.HIS_WCS_TRK')
  row2 = cursor2.fetchall()
  ls = []
  length = len(row2)
  for i in range(length):
    ls.append(str(row2[i][1])[0:10])
  ls = sorted(set(ls), reverse=True)
  ls1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  ls2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  if len(ls)<12:
    for m in range(12-len(ls)):
      ls.append('-')
  for k in range(12):
    for j in range(length):
      if row2[j][0] == '1' and str(row2[j][1])[0:10] == ls[k]:
        ls1[k] = ls1[k] + 1
      elif row2[j][0] == '2' and str(row2[j][1])[0:10] == ls[k]:
        ls2[k] = ls2[k] + 1
  ls=ls[:12][::-1]
  ls1=ls1[::-1]
  ls2=ls2[::-1]
  cursor2.close()
  conn2.close()
  return render_template('sqlser.html', **locals())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8081)
