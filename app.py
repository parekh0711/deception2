from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['POST'])
def myendpoint():
    incoming_msg = request.values.get('Body', '').lower()
    print(incoming_msg,file=open("output.txt","a+"))

if __name__ == '__main__':
    app.run()
