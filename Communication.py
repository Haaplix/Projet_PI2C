import socket
import json



class Communication:

    def __init__(self,ip,port):
        sb = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #? socket subscribe
        sg = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #? socket for the "game" 
        self.__sb = sb
        self.__sg = sg
        self.ip_gest = ip     #! IP et port gestionnaire
        self.port_gest = port
        self.port = 8080
        self.subscribe()


    def subscribe(self):
        self.__sb.connect((self.ip_gest, self.port_gest))

        data = json.dumps({"request": "subscribe", 
                "port": self.port,
                "name": "test",
                "matricules" : ["23022"]})

        send = self.__sb.send(data.encode())
        
        chunk = []
        finished = False

        while not finished:

            data = self.__sb.recv(1024)
            chunk.append(data)
            finished = data == b''
        response = json.loads(b"".join(chunk).decode())

        if response.get("response") == "ok":
            print("Subscription successful")
            self.__sb.close()
            self.__sg.bind((socket.gethostname(), self.port))

            
        else:
            print("Subscription failed")
            self.subscribe()

    def ping_pong(self,gest):
            print("Ping received")
            data = json.dumps({"response": "pong"})
            gest.send(data.encode())
            print("Pong sent")

    def run(self):
        while True:
            self.__sg.listen()
            self.gest, addr =self.__sg.accept()
            respond = json.loads(self.gest.recv(1024).decode())

            if respond.get("request") == "ping":
                self.ping_pong(self.gest)



Communication("172.17.10.43",3000).run() #! IP Julie



