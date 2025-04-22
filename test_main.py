import pytest 
import main 

def test_si_dernier_move():
    assert main.game().move({
  "players": ["LUR", "FKY"],
  "current": 0,
  "board": ["BDEC",None,"BDFC","BDFP","BLEC","BLFC","BLEP","BLFP",
                      "SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP","SLFP"],
  "piece": "BDEP"
}) == {"response": "move",
        "move": {"pos":1,"piece": None}
    }