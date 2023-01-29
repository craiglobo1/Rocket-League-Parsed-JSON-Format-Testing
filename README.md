# Rocket League Parsed JSON Format Testing

This is more information on rocket league's parsed json format

## Main Headers

So the replay json is made of the following main keys

- class_indices
- content_crc
- content_size
- debug_info
- game_type
- header_crc
- header_size
- keyframes
- levels
- major_version
- minor_version
- names
- net_cache
- net_version
- **network_frames**
- **objects**
- packages
- properties
- tick_marks
---
From the above list the following are actually important:

## objects

So this is a list of all the objects (names as strings) where the indices correspond to the object_id used in each frame of **network_frames**

eg. 
```python
objects = ["Core.Object", "Engine.Actor:RelativeRotation" ... "arc_standard_p.TheWorld:PersistentLevel.GoalVolume_TA_0.Goal_TA_1"]
``` 
therefore the object_id in a frame is 
- "Core.Object" = 0
- "Engine.Actor:RelativeRotation" = 1

so on and so forth 

*The following object types are important:*

### TAGame.RBActor_TA:ReplicatedRBState

It holds the Players rigidbody information (ie. the postion, rotation etc)

the `attribute` keys are:
* RigidBody
  *  angular_velocity
  *  linear_velocity
  *  location
     * x
     * y
     * z  
  *  rotation
     * w 
     * x
     * y
     * z  
  *  sleeping : bool for sleeping


## network_frames
This is a dictionary containing one key "frames"

"frames" is a list of dictionaries where each dictionary is a `frame`

**frame**

Each frame contains the following keys:
- new_actors
- updated_actors
- deleted_actors
- delta
- time

The keys **deleted_actors**, **updated_actors**, **deleted_actors** all contain a list of *actors*

idk why but never seem to have a non-empty **deleted_actors**

**delta** is the time difference between frames

**time** contains the current time according to the replay file (not the same as game time)

What is a **actor**?

A actor is a dictionary with the following keys:
- `actor_id` : unique id for each actor
- `object_id` : correlates to the an [object](#objects)

Keys for only actors in **new_actors**
- `initial_trajectory`
- `name_id`

Keys for only actors in **updated_actors**
- `attribute` : the attributes of a particular type of [object](#objects)
- `stream_id`

  
