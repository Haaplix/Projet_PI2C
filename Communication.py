import socket
import json
import main


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
                "name": "QT_3000",
                "matricules" : ["23022","23061"]})

        send = self.__sb.send(data.encode())
        
        response = self.recive(self.__sb)

        if response.get("response") == "ok":
            print("Subscription successful")
            self.__sb.close()
            self.__sg.bind((socket.gethostname(), self.port))

            
        else:
            print("Subscription failed")
            self.subscribe()

    
    def recive(self,s):
        chunk = []
        finished = False

        while not finished:
            data = s.recv(1024)
            chunk.append(data)
            
            try:
                response = json.loads(b"".join(chunk).decode())
                finished = True
            except IndentationError:
                pass
        return response


    def ping_pong(self,gest):
            print("Ping received")
            data = json.dumps({"response": "pong"})
            gest.send(data.encode())
            print("Pong sent")

    def run(self):
        while True:
            self.__sg.listen()
            self.gest, addr =self.__sg.accept()
            respond = self.recive(self.gest)

            if respond.get("request") == "ping":
                self.ping_pong(self.gest)
            
            if respond.get("request") == "play":
               move = json.dumps(main.game().move(respond.get("state"))) #put the move in a json to send to the sever
               self.gest.send(move.encode())



Communication("172.17.82.145",3000).run() #! IP Julie



