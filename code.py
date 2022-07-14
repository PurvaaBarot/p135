from flask import Flask,jsonify,request
from data import data

app=Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data" : data,
        "msg" : "success"
    }),200

@app.route("/data")
def data():
    name=request.args.get("name")
    data=next(item for item in data if item["name"]==name)
    return jsonify({
        "data" : data,
        "msg" : "success"
    }),200
if __name__=="__main__":
    app.run()    