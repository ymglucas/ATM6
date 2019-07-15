from conf import settings
import os
import json


def save(user_dic):
    with open('%s/%s'%(settings.DB_DIR,user_dic['name']),'w',encoding='utf-8')as f:
        f.write(json.dumps(user_dic))
        f.flush()


def select(name):
    user_path = os.path.join(settings.DB_DIR,name)
    if not os.path.exists(user_path ):
        return False
    with open('%s/%s'%(settings.DB_DIR,name),'r',encoding='utf-8')as f:
        user_dic = json.load(f)
        return user_dic
