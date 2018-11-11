import pymongo

def data_seve(mydict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    
    mydb = myclient["cralwer"]
    mycol = mydb["data"]
  
    # x = mycol.delete_many({})

    for m in mydict:
        if m in mycol.find():
            pass
        else:
            x = mycol.insert_one(m)

    # dblist = myclient.list_database_names()
    # if "runoobdb" in dblist:
    #   print("数据库已存在！")
    

def data_get():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["cralwer"]
    mycol = mydb["data"]

    # m = []

    # for x in mycol.find():
    #     m.append(x)
    m = mycol.find()

    return m