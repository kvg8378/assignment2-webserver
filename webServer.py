```python
# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  # Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen(1)

  while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]
      
      # Open the requested file in binary mode
      f = open(filename[1:], "rb")
      
      # Status line (200 OK)
      outputdata = b"HTTP/1.1 200 OK\r\n"

      # REQUIRED headers (Gradescope)
      outputdata += b"Server: MyWebServer\r\n"
      outputdata += b"Connection: close\r\n"
              
      # Content-Type header
      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"

      # End of headers
      outputdata += b"\r\n"
               
      # Append file contents
      for line in f:
        outputdata += line
        
      f.close()
        
      # Send everything in ONE send command
      connectionSocket.send(outputdata)
      connectionSocket.close()
      
    except Exception as e:
      # 404 Not Found response
      outputdata = b"HTTP/1.1 404 Not Found\r\n"

      # REQUIRED headers (Gradescope)
      outputdata += b"Server: MyWebServer\r\n"
      outputdata += b"Connection: close\r\n"

      outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"
      outputdata += b"\r\n"
      outputdata += b"<html><body><h1>404 Not Found</h1></body></html>"

      connectionSocket.send(outputdata)
      connectionSocket.close()

  # DO NOT uncomment these for submission
  #serverSocket.close()
  #sys.exit()

if __name__ == "__main__":
  webServer(13331)
```
