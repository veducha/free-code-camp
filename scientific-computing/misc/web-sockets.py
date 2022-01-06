# # EXAMPLE OF HOW TO CREATE A CONNECTION MANUALLY
# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # Opening a connection (i.e. socket)
# mysock.connect(('data.pr4e.org', 80))
# # Sending a request in the HTTP protocol
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# # Reading the returning information
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# # Closing the connection
# mysock.close()

# EXAMPLE OF HOW TO CREATE A CONNECTION WITH URLLIB
import urllib.request
import urllib.parse
import urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

print(counts)
