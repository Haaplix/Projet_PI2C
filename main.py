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
    
    self.list_message = ["Wallah, t'es trop guez", "C'est quoi ce move ???","Take the L","C'est un jeu de formes, mais je vais te plier en quatre","Une victoire de plus dans ma base de données","Ce coup est sponsorisé par l'intelligence artificielle","Je vais prétendre que j'ai perdu pour améliorer ton ego","Je suis plus carré que ces pièces","Je vois plus de connexions ici que dans ta box Wi-Fi"]
    
  
  
  @timeit
  def move(self, state):
    self.state = state #make a unit test to check if it loads correctly
    self.board = self.state["board"]
    
    if self.state["piece"] == None: #if we're first 
        piece_giv = "".join(random.choice(self.list_piece_possible))
    
        return {"response": "move",
                "move": {"piece":piece_giv},
                "message": random.choice(self.list_message)
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
                            "piece":self.piece_giv},
                    "message": random.choice(self.list_message)
                }
        else:  
            return {"response": "move",
                    "move": {"pos": self.heu_pos(),
                            "piece":self.piece_that_we_give()},
                    "message": random.choice(self.list_message)
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
      best_res = float('-inf')
      best_pos = None
      for i,t in enumerate(board_init): 
        board_new = copy.deepcopy(self.board)
        if t == None:
          board_new[i] = self.piece_got
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
            for value in D.values():
              if value == 4:
                return i
              if best_res < value:
                best_res = value
                best_pos = i
      return best_pos
  
  def piece_that_we_give(self):
    board_init = self.board
    worst_res = float("+inf")
    worst_piece = None
      
    if len(self.list_piece_possible) == 1: # Cas de fin de partie : une seule pièce restante
      self.piece_giv = "".join(self.list_piece_possible[0])
      return self.piece_giv
    if len(self.list_piece_possible) == 0:# Cas de fin de partie : aucune piece restante
      self.piece_giv = None
      return self.piece_giv
    
    for maybe_piece in self.list_piece_possible:
      result = 0
      is_winning = False
      for i, case in enumerate(board_init):
        if case is None:
          board_new = copy.deepcopy(board_init)
          board_new[i] = maybe_piece
          for line in self.lines:
            if i not in line:
              continue
            d = {"S":0,"B":0,"D":0,"L":0,"E":0,"F":0,"P":0,"C":0}
            for case in line:
              if board_new[case] != None:
                intersection = maybe_piece.intersection(board_new[case])
                for letter in intersection:
                  d[letter] += 1

            for i in d.values():
              if i == 4:
                is_winning = True
                break
            if is_winning: #si c'est une piece gagnante on la prend pas en compte et y'a besoin de se if pour vraiment sortir de la bloucle
              break

            result += sum(d.values())
        if is_winning:
          break
      if not is_winning and result < worst_res: #besoin de la 1er condi sinon ça prend potentiellement en compte les pieces gagnantes
        worst_res = result
        worst_piece = maybe_piece
    if worst_piece != None:
      self.piece_giv = "".join(worst_piece)
    else:
      self.piece_giv = "".join(random.choice(self.list_piece_possible)) #si dans le cas que toutes les pieces réstantes sont gagnantes 
    return self.piece_giv