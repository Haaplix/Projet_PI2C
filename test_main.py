import pytest 
import main 
import test

def test_si_dernier_move():
    result = main.game().move({
  "players": ["23022", "23061"],
  "current": 0,
  "board": ["BDEC",None,"BDFC","BDFP","BLEC","BLFC","BLEP","BLFP",
            "SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP","SLFP"],
  "piece": "BDEP"
  
})
    assert result["response"] == "move"
    assert result["move"]["pos"] == 1
    assert result["move"]["piece"] == None

def test_si_nous_1er_move(): 

    list_piece_possible = [set("BDEC"),set("BDEP"),set("BDFC"),set("BDFP"),set("BLEC"),set("BLFC"),set("BLEP"),set("BLFP"),
                      set("SDEC"),set("SDEP"),set("SDFC"),set("SDFP"),set("SLEC"),set("SLFC"),set("SLEP"),set("SLFP")]
    result = main.game().move({"players": ["23022", "23061"],
            "current": 0,
            "board": [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
            "piece": None
        })

    assert set(result["move"]["piece"]) in list_piece_possible

    
def test_si_possi_win():
    result = main.game().move({
        "players": ["23022", "23061"],
        "current": 0,
        "board": ["BDEC", None, "BDFC", "BDFP",
                  "BLEC", None, "BLEP", None,
                  None, None, "SDFC", "SDFP",
                  None, None, None, "SLFP"],
        "piece": "BDEP"
    })
    
    assert result["response"] == "move"
    assert result["move"]["pos"] == 1


def test_donner_bonne_piece():
   piece_not_to_give = [set("BDEP"),set("BLFC"),set("BLFP")]

   result = main.game().move({
        "players": ["23022", "23061"],
        "current": 0,
        "board": ["BDEC", None, "BDFC", "BLEC",
                  "BDFP", None, "BLEP", None,
                  None, None, "SDFC", None,
                  None, None, None, None],
        "piece": "SDEP"
    })
   
   assert set(result["move"]["piece"]) not in piece_not_to_give

def test_si_dernier_move2():
    result = test.game().move({
  "players": ["23022", "23061"],
  "current": 0,
  "board": ["BDEC",None,"BDFC","BDFP","BLEC","BLFC","BLEP","BLFP",
            "SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP","SLFP"],
  "piece": "BDEP"
})
    assert result["response"] == "move"
    assert result["move"]["pos"] == 1
    assert result["move"]["piece"] == None
