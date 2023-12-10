from flask import *
import test
app=Flask(__name__)

@app.route("/data",methods=['POST'])
def index():
    data=request.json['data']
    res=test.datac(data)
    return ({"result":res})



if __name__=="__main__":
    app.run(debug=True,port=8000)