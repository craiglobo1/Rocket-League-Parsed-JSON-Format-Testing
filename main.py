import carball
from carball.json_parser.game import Game
from carball.analysis.analysis_manager import AnalysisManager
import json
import time
import logging
class Frames:
    def __init__(self, obj) -> None:
        frames = obj["network_frames"]["frames"]
    
    def __iter__(self):
        for frame in self.frames:
            yield frame


class Replay_object:
    def __init__(self, obj) -> None:
        self.replay = obj
        self.frames = Frames(obj)


def pp(dict):
    print(json.dumps(dict,indent=3))

def replay_to_df(replay_path : str):
    replay = carball.decompile_replay(replay_path)
    game = Game()
    logging.getLogger('carball').setLevel(50)
    game.initialize(loaded_json=replay)
    analysis = AnalysisManager(game)
    df = analysis._initialize_data_frame(game)
    return df
t= time.time()
df = replay_to_df("F11221D849FADD3FA90470AE56571394.replay")
print(time.time()-t)
#TODO: replace NaN with 0 in throttle, steer (int/float)
#TODO: replace False with 0 in dodge_active, double_jump_active, jump_active (int/float)
#TODO: figure out what NaN is in handbrake (boolean), hit_team_no (int_boolean (1 or 0 or NaN))

# print(list(df["game"]["seconds_remaining"]))
