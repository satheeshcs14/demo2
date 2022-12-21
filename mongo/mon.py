import pymongo


myclient = pymongo.MongoClient("localhost:27017")


power = myclient["vet"]
mycol = power["jhkj"]


data =power.jhkj.insert_one({"name":"satheesh","pwd":"hello"})
print(data)


