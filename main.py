# This is a sample Python script.
import socket

sock = socket.socket()
sock.bind(("", 8080))
sock.listen(5)
while True:
    connection, address = sock.accept()
    print('Got connection from', address)
    break


request = connection.recv(2048).decode("ASCII")

response = "<h1>Your browser sent the following request:</h1>\n<pre>" + request + "</pre>"

connection.sendall(bytearray("HTTP/1.1 200 ok\n", "ASCII"))
connection.sendall(bytearray("\n", "ASCII") )
connection.sendall(bytearray("<html>\n", "ASCII"))
connection.sendall(bytearray(response, "ASCII"))
connection.sendall(bytearray("</html>", "ASCII"))
