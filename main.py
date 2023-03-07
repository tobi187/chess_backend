import socketio
import eventlet
import secrets
import game

sio = socketio.Server(cors_allowed_origins="*")
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

groups = {}


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def create(sid):
    token = secrets.token_urlsafe(15)
    sio.enter_room(sid, token)
    return {"roomKey": token}


@sio.event
def join(sid, data):
    game_key = data["key"]
    sio.enter_room(sid, game_key)
    sio.emit("game_start", room=game_key, data={
             "message": "wowo its starting"})

    return 200


def move(sid, data):
    print("message", data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
