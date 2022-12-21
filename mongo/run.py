from flask import Flask,request ,json
from pymongo import MongoClient

app = Flask(__name__)

server = MongoClient("localhost", 27017)
db =server.vet
mycol = db.jhkj


@app.route("/data ",methods =['POST'])
def info_post():
        print(request.json)
        if request.method =='POST':
              name = request. json["name"]
              password = request.json['pwd']
              list = db.jhkj.insert({'name':name,'pwd':password})
              return "user added successfuly"

           




if __name__=="__main__":
    app.run(debug=True)
