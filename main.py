import json
import random


class game:
    def __init__(self):
        self.list_piece_possible = ["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP",
                      "SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP","SLFP"]

    def move(self, state):

        self.state = state #make a unit test to check if it loads correctly
        self.board = self.state["board"]


        if self.state["piece"] == None: #if we're first 
            piece_giv = random.choice(self.list_piece_possible)
            print(self.list_piece_possible)

            return {"response": "move",
                    "move": {"piece":piece_giv}
                    }
        
        else: 
            self.piece_got = self.state["piece"]
            self.remove()
    

    def remove(self):
        self.list_piece_possible.remove(self.piece_got)
        for i in self.board:
            if i != None:
                self.list_piece_possible.remove(i)
