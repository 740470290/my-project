import json
# json文件格式需要unf-8无bom
with open("./t.json",'a',encoding='utf-8') as w:
    # json_dict = json.load(w)
    # print(json_dict)
    # json_dict['message'].insert(0,{"id":3,"name":"ffff"})
    # print(json_dict)
    json.dump(json_dict, w, ensure_ascii=False)
# with open("./t.json", 'w', encoding='utf-8') as w:
#     json.dump(json_dict, w,ensure_ascii = False)
#     print(json_dict)
