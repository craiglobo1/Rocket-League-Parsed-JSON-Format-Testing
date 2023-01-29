import carball
import json
import time
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

replay = carball.analyze_replay_file('F11221D849FADD3FA90470AE56571394.replay', logging_level=50)
df = replay.get_data_frame()
print(df.get("game").get("goal_number"))
# headers = [ "-".join(header) for header in df.head()]
# for head in headers:
#     print(head)