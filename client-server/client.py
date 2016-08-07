import zmq
import time
import uuid

client_id = uuid.uuid1()
ctx = zmq.Context()
socket = ctx.socket(zmq.XREQ)
socket.SNDHWM = 1

def connect(socket):
    socket.connect("tcp://127.0.0.1:8080")
    socket.connect("tcp://127.0.0.1:8081")

connect(socket)

poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)

while True:
    try:
        print "Sending"
        socket.send(str(client_id), zmq.NOBLOCK)
        print "Done sending" 
        state = dict(poller.poll(500))
        if state.get(socket) == zmq.POLLIN:
            print socket.recv()
        else:
            print "Timed out, skipping."
    except zmq.ZMQError as e:
        print "Failed with {}, skipping.".format(e)
    time.sleep(.3)
