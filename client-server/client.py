"""
client

Usage:
    client [(-a | --addresses) <addresses>...]

Options:
    -a --addresses  A list of space separated addresses the client will connect to.
    -h --help   Prints this help message.
"""

import time
import uuid
import zmq

from docopt import docopt


def run_client(arguments):
    address_argument = arguments.get('<addresses>')
    if address_argument:
        addresses = ['tcp://' +  a for a in arguments.get('<addresses>')]
    else:
        addresses = ['tcp://127.0.0.1:8080', 'tcp://127.0.0.1:8081']

    client_id = uuid.uuid1()

    ctx = zmq.Context()

    socket = ctx.socket(zmq.XREQ)
    socket.SNDHWM = 1

    for address in addresses:
        socket.connect(address)

    poller = zmq.Poller()
    poller.register(socket, zmq.POLLIN)

    while True:
        try:
            socket.send(str(client_id), zmq.NOBLOCK)
            state = dict(poller.poll(50))
            if state.get(socket) == zmq.POLLIN:
                print socket.recv()
            else:
                print "Timed out, skipping."
        except zmq.ZMQError as e:
            print "Failed with {}, skipping.".format(e)
        time.sleep(.3)

if __name__ == '__main__':
    run_client(docopt(__doc__))
