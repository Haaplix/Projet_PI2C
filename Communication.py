import socket
import json



class Communication:

    def __init__(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__s = s
        self.ip = ip
        self.port = port
        self.subscribe()


    def subscribe(self):
        self.__s.connect((self.ip, self.port))

        data = json.dumps({"request": "subscribe", 
                "port": 8080,
                "name": "tkt",
                "matricules" : ["23022", "23061"]})

        send = self.__s.send(data.encode())
        
        chunk = []
        finished = False

        while not finished:

            data = self.__s.recv(1024)
            chunk.append(data)
            finished = data == b''
        response = json.loads(b"".join(chunk).decode())

        if response.get("response") == "ok":
            print("Subscription successful")
        else:
            print("Subscription failed")
            self.subscribe()


        
Communication("172.17.10.43",3000) 



