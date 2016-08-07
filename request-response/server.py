import zmq


ctx = zmq.Context()
socket = ctx.socket(zmq.XREP)
socket.bind("tcp://0.0.0.0:8080")

msg = ""

while True:
    msg = socket.recv_multipart()
    print msg
    socket.send_multipart(msg)
