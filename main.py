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

replay = carball.decompile_replay('F11221D849FADD3FA90470AE56571394.replay')
frames = replay["network_frames"]["frames"]

# names = dict(enumerate(names))
# pp(names)

print([header for header in replay])
objects = {obj:i for i, obj in enumerate(replay["objects"])}
idx_to_objects = dict(enumerate(replay["objects"]))
# json.dump(objects, open("objects.json", "w+"), indent=3)
# pp(objects)
# print([header for header in frames[0]])

# cur_time = 0
used = set()
for frame in frames:
    # if frame["updated_actors"]:
    #     print([key for key in frame["updated_actors"][0]], end=" ")
    
    # if frame["updated_actors"]:
    #     for actor in frame["updated_actors"]:
    #         print([key for key in actor], end=" ")

    # if frame["deleted_actors"]:
    #     print([key for key in frame["deleted_actors"][0]],end=" ")
    # print()

    c_actor : list = frame["updated_actors"]
    obj_name = "TAGame.RBActor_TA:ReplicatedRBState"
    if objects[obj_name] in [actors["object_id"] for actors in c_actor]:
        actor = list(filter(lambda x: x["object_id"] == objects[obj_name], c_actor))[0]
        print([key for key in actor["attribute"]["RigidBody"]["rotation"]])
    # break
        
        # print(list(filter(lambda x: x["actor_id"] == 40, c_actor))[0])
    # print([names[actor["actor_id"]] for actor in frame["new_actors"]])
    # print(frame["new_actors"][0])
    # break

# for obj in used:
#     print(idx_to_objects[obj])

# json.dump(replay, open("test.json", "w+"), indent=3)