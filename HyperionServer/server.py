from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'thisisnotawaryoushouldbefighting'
socketio = SocketIO(app)

@app.route('/')
def hyperion():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@socketio.on('connect')
def user_connect():
    emit('response', {'data': 'Connection Successful'})

if __name__ == '__main__':
    socketio.run(app)