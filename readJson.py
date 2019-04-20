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
conn = pymssql.connect(config.server, config.user, config.pwd, config.database2)
cursor = conn.cursor()
cursor.execute('SELECT TRK_TP,CREATE_DATE FROM dbo.HIS_WCS_TRK')
row = cursor.fetchall()
ls=[]
length=len(row)
for i in range(length):
  ls.append(str(row[i][1])[0:10])
print('..........',sorted(set(ls), reverse=True))
ls=sorted(list(set(ls)),reverse=True)

ls1=[0,0,0,0,0,0,0,0,0,0,0,0]
ls2=[0,0,0,0,0,0,0,0,0,0,0,0]
for k in range(12):
  for j in range(length):
    if row[j][0]=='1' and str(row[j][1])[0:10]==ls[k]:
      ls1[k] = ls1[k]+1
    elif row[j][0]=='2' and str(row[j][1])[0:10]==ls[k]:
      ls2[k] = ls2[k]+1
#   if row[i][0]=='0':
#     ls[0]=ls[0]+1
#   elif row[i][0]=='1':
#     ls[1] = ls[1] + 1
#   else:
#     ls[2] = ls[2] + 1

# list=json.dumps(row)
# for i in row:
#   print(i[0])
#   i=i[0]
  # c=float(i[2])
  # i[2]=c
print(row)
print(str(row[0][0])[0:10])
print(ls)
a=list(set(ls))
print(sorted(a,reverse=True))
print(ls)
print(ls1)
print(ls2)
# print(ls)
# print(json.dumps(ls))
# print(list)
cursor.close()
conn.close()
# amount="Decimal('4.000')"
# a=json.dumps( { 'sum': amount } )
# print(a)
