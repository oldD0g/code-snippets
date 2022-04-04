from flask import Flask,request,json

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Webhooks with Python'

@app.route('/webhook',methods=['POST'])
def webhook():
    data = request.json
    print(json.dumps(data, indent=4))
    return data

if __name__ == '__main__':
    app.run(debug=True)
