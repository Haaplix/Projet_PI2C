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

# def test_si_nous_1er_move(): 
#     assert main.game().move({"players": ["LUR", "FKY"],
#   "current": 0,
#   "board": [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
#   "piece": "BDEP"
#         }) == 


def test_si_possi_win():
    result = main.game().move({
        "players": ["LUR", "FKY"],
        "current": 0,
        "board": ["BDEC", None, "BDFC", "BDFP",
                  "BLEC", None, "BLEP", None,
                  None, None, "SDFC", "SDFP",
                  None, None, None, "SLFP"],
        "piece": "BDEP"
    })
    
    assert result["response"] == "move"
    assert result["move"]["pos"] == 1
    assert sorted(result["move"]["piece"]) == sorted("LBFC")
