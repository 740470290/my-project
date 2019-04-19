import json
import pymssql
import config
# json文件格式需要unf-8无bom
# with open("./t.json",'a',encoding='utf-8') as w:
    # json_dict = json.load(w)
    # print(json_dict)
    # json_dict['message'].insert(0,{"id":3,"name":"ffff"})
    # print(json_dict)
    # json.dump(json_dict, w, ensure_ascii=False)
# with open("./t.json", 'w', encoding='utf-8') as w:
#     json.dump(json_dict, w,ensure_ascii = False)
#     print(json_dict)
conn = pymssql.connect(config.server, config.user, config.pwd, config.database)
cursor = conn.cursor()
cursor.execute('SELECT locate_st FROM dbo.VIEW_IWMS_LOCATE')
row = cursor.fetchall()
ls=[0,0,0]
length=len(row)
for i in range(length):
  if row[i][0]=='0':
    ls[0]=ls[0]+1
  elif row[i][0]=='1':
    ls[1] = ls[1] + 1
  else:
    ls[2] = ls[2] + 1
# list=json.dumps(row)
# for i in row:
#   print(i[0])
#   i=i[0]
  # c=float(i[2])
  # i[2]=c
print(len(row))
print(ls)
print(json.dumps(ls))
# print(list)
cursor.close()
conn.close()
# amount="Decimal('4.000')"
# a=json.dumps( { 'sum': amount } )
# print(a)
