import sys
import zmq

from helpers.throughput import Counter

ctx = zmq.Context()
socket = ctx.socket(zmq.XREP)
socket.bind("tcp://0.0.0.0:8080")

counter = Counter()

try: 
    while True:
        msg = socket.recv_multipart()
        socket.send_multipart(msg)
        counter.inc()
except KeyboardInterrupt:
    counter.stop()
