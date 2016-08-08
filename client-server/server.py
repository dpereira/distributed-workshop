"""
server

Usage:
    server [(-p | --port) <port>]
    server (-h | --help)

Options:
    -p --port   Sets the tcp port the server will bind to. Defaults to 8080.
    -h --help   Shows this help messsage.
"""

import sys
import zmq

from docopt import docopt

from helpers.throughput import Counter


def run_server(arguments):
    port = arguments.get('<port>') or '8080'
    ctx = zmq.Context()
    socket = ctx.socket(zmq.XREP)
    socket.bind("tcp://0.0.0.0:{}".format(port))

    counter = Counter()

    try: 
        while True:
            msg = socket.recv_multipart()
            socket.send_multipart(msg)
            counter.inc()
    except KeyboardInterrupt:
        counter.stop()

if __name__ == "__main__":
    run_server(docopt(__doc__))
