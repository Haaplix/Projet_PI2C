import json
import random


class game:
    def __init__(self):
        self.list_piece_possible = [set("BDEC"),set("BDEP"),set("BDFC"),set("BDFP"),set("BLEC"),set("BLFC"),set("BLEP"),set("BLFP"),
                      set("SDEC"),set("SDEP"),set("SDFC"),set("SDFP"),set("SLEC"),set("SLFC"),set("SLEP"),set("SLFP")]

    def move(self, state):

        self.state = state #make a unit test to check if it loads correctly
        self.board = self.state["board"]


        if self.state["piece"] == None: #if we're first 
            piece_giv = "".join(random.choice(self.list_piece_possible))
        

            return {"response": "move",
                    "move": {"piece":piece_giv}
                    }
        
        else: 
            self.piece_got = self.state["piece"]
            self.remove()
            if len(self.list_piece_possible) != 0:
                self.piece_giv = "".join(random.choice(self.list_piece_possible))
            else:
                self.piece_giv = None
            return {"response": "move",
                    "move": {"pos":self.pos(),
                             "piece":self.piece_giv},
                    "message":"Imagine être plus nul qu'un random"
                    }
    

    def remove(self):
        self.list_piece_possible.remove(set(self.piece_got))
        for i in self.board:
            if i != None:
                self.list_piece_possible.remove(set(i))

    def pos(self):
        L = []
        for i,t in enumerate(self.board):

            if t == None:
                L.append(i)
        return random.choice(L)

