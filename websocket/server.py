# based on https://gist.github.com/jkp/3136208

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))+".."))
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))+'/../driver'))
sys.path.append("../driver")

import struct
import socketserver
import sys
from base64 import b64encode
from hashlib import sha1
from email.message import Message
from io import StringIO

import gpio

DEFAULT_PORT = 9999

class WebSocketsHandler(socketserver.StreamRequestHandler):
    magic = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'

    def setup(self):
        socketserver.StreamRequestHandler.setup(self)
        #print("connection established %s" % self.client_address)
        self.handshake_done = False

    def handle(self):
        while True:
            if not self.handshake_done:
                self.handshake()
            else:
                self.read_next_message()

    def read_next_message(self):
        length = ord(self.rfile.read(2)[1]) & 127
        if length == 126:
            length = struct.unpack(">H", self.rfile.read(2))[0]
        elif length == 127:
            length = struct.unpack(">Q", self.rfile.read(8))[0]
        masks = [ord(byte) for byte in self.rfile.read(4)]
        decoded = ""
        for char in self.rfile.read(length):
            decoded += chr(ord(char) ^ masks[len(decoded) % 4])
        self.on_message(decoded)
        #print "hallo"


    def send_message(self, message):
        self.request.send(chr(129))
        length = len(message)
        if length <= 125:
            self.request.send(chr(length))
        elif length >= 126 and length <= 65535:
            self.request.send(126)
            self.request.send(struct.pack(">H", length))
        else:
            self.request.send(127)
            self.request.send(struct.pack(">Q", length))
        self.request.send(message)

    def handshake(self):
        data = self.request.recv(1024).strip()
        headers = Message(StringIO(data.split('\r\n', 1)[1]))
        if headers.get("Upgrade", None) != "websocket":
            return
        print("Handshaking...")
        key = headers['Sec-WebSocket-Key']
        digest = b64encode(sha1(key + self.magic).hexdigest().decode('hex'))
        response = 'HTTP/1.1 101 Switching Protocols\r\n'
        response += 'Upgrade: websocket\r\n'
        response += 'Connection: Upgrade\r\n'
        response += 'Sec-WebSocket-Accept: %s\r\n\r\n' % digest
        self.handshake_done = self.request.send(response)

    def on_message(self, message):
        pass # overriden by WebSocketServer

class WebSocketServer(socketserver.TCPServer):

    def __init__(self, port, on_message):
        WebSocketsHandler.on_message = on_message
        socketserver.TCPServer.allow_reuse_address = True
        socketserver.TCPServer.__init__(self, ("192.168.2.241", port), WebSocketsHandler)


    def serve(self):
        try:
            self.serve_forever()

        except KeyboardInterrupt:
            print("Shutting down..")
            self.server_close();
            print("bye!")            
            self.shutdown()

if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except:
        port = DEFAULT_PORT
    print(sys.path)

    def simpleprint(self, message):
        print("message %s" % message) 
    WebSocketServer(port, simpleprint).serve()


