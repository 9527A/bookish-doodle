import pymongo

def data_seve(mydict):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    
    mydb = myclient["cralwer"]
    mycol = mydb["data"]

    for m in mydict:
        if m in mycol.find():
            pass
        else:
            x = mycol.insert_one(m)

def data_get():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["cralwer"]
    mycol = mydb["data"]

    m = mycol.find()

    return m

def delete():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["cralwer"]
    mycol = mydb["data"]
    
    x = mycol.delete_many({})


