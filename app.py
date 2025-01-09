from flask import Flask, request, render_template
from flask_restx import Resource, Api
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET','POST'])
def chat():
    if request.method == 'POST':
        email = request.form['email']
        print(">>email:", email)
    return render_template('chat.html',emailvalue=email)

@socketio.on('event')
def event_handler(json):
    print("json:{}".format(json))
    # socketio.emit('response', json)
    if "data" in json:
        if json["data"] == "Connect":
            print("Received data : {}".format(json["data"]))
            socketio.emit('response', {"message": ""})
    else:
        # json["message"] = json["message"].encode["latin1"].decode("utf-8")
        socketio.emit('response', {"message": json["message"], "time": json["time"]})

     
if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port="6700")
    # socketio.run(app, host='0.0.0.0', port="5000", debug=True)
    socketio.run(app)

