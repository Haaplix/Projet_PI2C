import json
import random
import time
import copy


def timeit(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fun(*args, **kwargs)
        print('Executed in {}s'.format(time.time() - start))
        return res
    return wrapper


class game:
    def __init__(self):
        self.list_piece_possible = [set("BDEC"),set("BDEP"),set("BDFC"),set("BDFP"),set("BLEC"),set("BLFC"),set("BLEP"),set("BLFP"),
                      set("SDEC"),set("SDEP"),set("SDFC"),set("SDFP"),set("SLEC"),set("SLFC"),set("SLEP"),set("SLFP")]
        
        self.lines =[[0,1,2,3],
                     [4,5,6,7],
                     [8,9,10,11],
                     [12,13,14,15],
                     [0,4,8,12],
                     [1,5,9,13],
                     [2,6,10,14],
                     [3,7,11,15],
                     [0,5,10,15],
                     [3,6,9,12]]
        
    
    
    @timeit
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

            if self.board == [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]:
                return {"response": "move",
                    "move": {"pos": self.pos(),
                             "piece":self.piece_giv}
                    }
            else:
    
                return {"response": "move",
                        "move": {"pos": self.heu_pos(),
                                "piece":self.piece_that_we_give()}
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


    def heu_pos(self):
        board_init = self.board
        board_new = copy.deepcopy(self.board)
        cara = set(self.piece_got)
        best_res = 0
        best_pos = None
        for i,t in enumerate(board_init): 
            board_new = copy.deepcopy(self.board)
            if t == None:
                board_new[i] = self.piece_got
                print(board_new)
                for line in self.lines:
                    D = {"S":0,"B":0,"D":0,"L":0,"E":0,"F":0,"P":0,"C":0}
                    result = 0
                    for case in line:
                        if board_new[case] != None:
                            cara_case = set(board_new[case])
                            for lettre in cara:
                                res = D.get(lettre)
                                if lettre in cara.intersection(cara_case):
                                    D[lettre] = res + 1
                    print(D)

                    if best_res < result:
                        best_res = result
                        best_pos = i
                        

            else: 
                pass
            print("bestres:",best_res)
        return best_pos
    

    def piece_that_we_give(self):
        board_init = self.board
        board_new = copy.deepcopy(self.board)
        worst_res = float("+inf")

        for i,t in enumerate(board_init):
            board_new = copy.deepcopy(self.board)
            for maybe_piece in  enumerate(self.list_piece_possible):
                #print(maybe_piece)
                cara = maybe_piece[1]
                if t == None:
                    board_new[i] = maybe_piece
                    for line in self.lines:
                        res = 0
                    
                        for case in line: 

                            if board_new[case] != None:
                                print(board_new[case])
                                cara_case = board_new[case][1]
                                res = len(cara.intersection(cara_case))

                        if res < worst_res:
                            self.piece_giv = "".join(maybe_piece[1])
                    

                            
        return self.piece_giv