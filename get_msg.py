from flask import Flask,render_template,Response,request
from flask import jsonify
from flask_cors import CORS
import json,time

app = Flask(__name__)
cors = CORS(app, resources={r"/getMsg": {"origins": "*"}})
CORS(app, supports_credentials=True)
@app.route('/api/<name>')
def get_json(name):
  with open("./api/"+name+".json", 'r', encoding='utf-8') as f:
    json_dict = json.load(f)
  return jsonify(json_dict)

@app.route('/images/<name>')
def get_img(name):
  with open("./images/"+name+".jpg", 'rb') as f:
    image = f.read()
  return Response(image, mimetype="image/jpeg")

@app.route('/api/getnew/<name>')
def get_news(name):
  with open("./api/getnew/"+name+".json", 'r', encoding='utf-8') as f:
    json_dict = json.load(f)
  return jsonify(json_dict)

@app.route('/api/getimageInfo/<name>')
def getimageInfo(name):
  with open("./api/getimageInfo/"+name+".json", 'r', encoding='utf-8') as f:
    json_dict = json.load(f)
  return jsonify(json_dict)

@app.route('/api/getimages/<name>')
def getimages(name):
  with open("./api/getimages/"+name+".json", 'r', encoding='utf-8') as f:
    json_dict = json.load(f)
  return jsonify(json_dict)

@app.route('/api/getthuimages/<name>')
def getthuimages(name):
  with open("./api/getthuimages/"+name+".json", 'r', encoding='utf-8') as f:
    json_dict = json.load(f)
  return jsonify(json_dict)

@app.route('/api/getcomments/<name>', methods=['GET', 'POST'])
def get_cmt(name):
  if request.method == 'POST':
    page = int(request.form.get('page'))
    ls = []
    with open("./api/getcomments/"+name+".json", 'r', encoding='utf-8') as f:
      json_dict = json.load(f)['message']
      if page>(len(json_dict)-1)/10+1:
        return False
      else:
        for i in range((page-1)*10,page*10):
          try:
            ls.append(json_dict[i])
          except:
            pass
      return jsonify(ls)

@app.route('/api/postcomment/<name>', methods=['GET', 'POST'])
def post_cmt(name):
  if request.method == 'POST':
    ls=[]
    con = request.form.get('content')
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    with open("./api/getcomments/"+name+".json", 'r', encoding='utf-8') as f:
      json_dict = json.load(f)
      json_dict['message'].insert(0, {"user_name": "匿名用户", "add_time": date,"content":con})
      for i in range(10):
        ls.append(json_dict['message'][i])
    with open("./api/getcomments/"+name+".json", 'w', encoding='utf-8') as w:
      json.dump(json_dict, w, ensure_ascii=False)
    return jsonify(ls)

@app.route('/getMsg', methods=['GET', 'POST'])
def home():
    response = {
        'msg': 'Hello, Python !'
    }
    return jsonify(response)

# 启动运行
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)   # 这样子会直接运行在本地服务器，也即是 localhost:5000
   # app.run(host='your_ip_address') # 这里可通过 host 指定在公网IP上运行
