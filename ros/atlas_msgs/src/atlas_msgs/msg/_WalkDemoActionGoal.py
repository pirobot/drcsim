# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from atlas_msgs/WalkDemoActionGoal.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import atlas_msgs.msg
import genpy
import actionlib_msgs.msg
import std_msgs.msg

class WalkDemoActionGoal(genpy.Message):
  _md5sum = "be276040800453fdc072cc2f7f7dbc6a"
  _type = "atlas_msgs/WalkDemoActionGoal"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
WalkDemoGoal goal

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: atlas_msgs/WalkDemoGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Goal
# For Setting MultiStep Walking Commands
Header header

# permissible values for behavior
int32 STAND             =  0 # stand
int32 USER              =  1 # disable AtlasSimInterface updates, rely on
                             # /atlas/atlas_command or /atlas/joint_commands
int32 FREEZE            =  2 # safety mode
int32 STAND_PREP        =  3 # stand-prep (AtlasSimInterface documentation)
int32 WALK              =  4 # multi-step walk
int32 STEP              =  5 # single step walk
int32 MANIPULATE        =  6 # stand and allows manipulation.

int32 behavior                # can be one of
                              # USER, FREEZE, STAND_PREP
                              # WALK, STEP, STAND, MANIPULATE
                              # DEMO1, DEMO2

# multi_step walking trajectory parameters
atlas_msgs/AtlasBehaviorStepData[] steps

# parameters for single_step behavior
atlas_msgs/AtlasBehaviorStepParams step_params

# parameters for standing behavior
atlas_msgs/AtlasBehaviorStandParams stand_params

# parameters for stand and manipulate
atlas_msgs/AtlasBehaviorManipulateParams manipulate_params

# same k_effort as AtlasCommand
uint8[] k_effort       # k_effort can be an unsigned int 8value from 0 to 255, 
                       # at run time, a double between 0 and 1 is obtained
                       # by dividing by 255.0d.


================================================================================
MSG: atlas_msgs/AtlasBehaviorStepData
# multi_step walking trajectory parameters
uint32 step_index              # Step index, matlab style, starting from 1,
                               # monotonically increasing during walking
                               #  resets to 1 if robot leaves walk behaviors
uint32 foot_index              # Foot_index can be LEFT_FOOT or RIGHT_FOOT
float64 duration               # Step duration, when in doubt, 0.63s is a
                               # good guess.
geometry_msgs/Pose pose        # Foot pose in Atlas world frame
float64 swing_height           # Step apex swing height measured form the
                               # midpoint between the feet.

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: atlas_msgs/AtlasBehaviorStepParams
# parameters for single_step behavior
atlas_msgs/AtlasBehaviorStepData desired_step
bool use_demo_walk

================================================================================
MSG: atlas_msgs/AtlasBehaviorStandParams
# stand parameters
int32 placeholder
# etc., more to come

================================================================================
MSG: atlas_msgs/AtlasBehaviorManipulateParams
# mirrored from AtlasControlTypes.h
bool use_desired
atlas_msgs/AtlasBehaviorPelvisServoParams desired
bool use_demo_mode

================================================================================
MSG: atlas_msgs/AtlasBehaviorPelvisServoParams
# mirrored from AtlasControlTypes.h

float64 pelvis_height
float64 pelvis_yaw
float64 pelvis_lat
"""
  __slots__ = ['header','goal_id','goal']
  _slot_types = ['std_msgs/Header','actionlib_msgs/GoalID','atlas_msgs/WalkDemoGoal']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,goal_id,goal

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WalkDemoActionGoal, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = atlas_msgs.msg.WalkDemoGoal()
    else:
      self.header = std_msgs.msg.Header()
      self.goal_id = actionlib_msgs.msg.GoalID()
      self.goal = atlas_msgs.msg.WalkDemoGoal()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs))
      _x = self.goal.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_i.pack(self.goal.behavior))
      length = len(self.goal.steps)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.steps:
        _x = val1
        buff.write(_struct_2Id.pack(_x.step_index, _x.foot_index, _x.duration))
        _v1 = val1.pose
        _v2 = _v1.position
        _x = _v2
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v3 = _v1.orientation
        _x = _v3
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_d.pack(val1.swing_height))
      _x = self
      buff.write(_struct_2I9dBiB3dB.pack(_x.goal.step_params.desired_step.step_index, _x.goal.step_params.desired_step.foot_index, _x.goal.step_params.desired_step.duration, _x.goal.step_params.desired_step.pose.position.x, _x.goal.step_params.desired_step.pose.position.y, _x.goal.step_params.desired_step.pose.position.z, _x.goal.step_params.desired_step.pose.orientation.x, _x.goal.step_params.desired_step.pose.orientation.y, _x.goal.step_params.desired_step.pose.orientation.z, _x.goal.step_params.desired_step.pose.orientation.w, _x.goal.step_params.desired_step.swing_height, _x.goal.step_params.use_demo_walk, _x.goal.stand_params.placeholder, _x.goal.manipulate_params.use_desired, _x.goal.manipulate_params.desired.pelvis_height, _x.goal.manipulate_params.desired.pelvis_yaw, _x.goal.manipulate_params.desired.pelvis_lat, _x.goal.manipulate_params.use_demo_mode))
      _x = self.goal.k_effort
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = atlas_msgs.msg.WalkDemoGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.goal.header.frame_id = str[start:end]
      start = end
      end += 4
      (self.goal.behavior,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.steps = []
      for i in range(0, length):
        val1 = atlas_msgs.msg.AtlasBehaviorStepData()
        _x = val1
        start = end
        end += 16
        (_x.step_index, _x.foot_index, _x.duration,) = _struct_2Id.unpack(str[start:end])
        _v4 = val1.pose
        _v5 = _v4.position
        _x = _v5
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v6 = _v4.orientation
        _x = _v6
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 8
        (val1.swing_height,) = _struct_d.unpack(str[start:end])
        self.goal.steps.append(val1)
      _x = self
      start = end
      end += 111
      (_x.goal.step_params.desired_step.step_index, _x.goal.step_params.desired_step.foot_index, _x.goal.step_params.desired_step.duration, _x.goal.step_params.desired_step.pose.position.x, _x.goal.step_params.desired_step.pose.position.y, _x.goal.step_params.desired_step.pose.position.z, _x.goal.step_params.desired_step.pose.orientation.x, _x.goal.step_params.desired_step.pose.orientation.y, _x.goal.step_params.desired_step.pose.orientation.z, _x.goal.step_params.desired_step.pose.orientation.w, _x.goal.step_params.desired_step.swing_height, _x.goal.step_params.use_demo_walk, _x.goal.stand_params.placeholder, _x.goal.manipulate_params.use_desired, _x.goal.manipulate_params.desired.pelvis_height, _x.goal.manipulate_params.desired.pelvis_yaw, _x.goal.manipulate_params.desired.pelvis_lat, _x.goal.manipulate_params.use_demo_mode,) = _struct_2I9dBiB3dB.unpack(str[start:end])
      self.goal.step_params.use_demo_walk = bool(self.goal.step_params.use_demo_walk)
      self.goal.manipulate_params.use_desired = bool(self.goal.manipulate_params.use_desired)
      self.goal.manipulate_params.use_demo_mode = bool(self.goal.manipulate_params.use_demo_mode)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal.k_effort = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs))
      _x = self.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs))
      _x = self.goal.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_i.pack(self.goal.behavior))
      length = len(self.goal.steps)
      buff.write(_struct_I.pack(length))
      for val1 in self.goal.steps:
        _x = val1
        buff.write(_struct_2Id.pack(_x.step_index, _x.foot_index, _x.duration))
        _v7 = val1.pose
        _v8 = _v7.position
        _x = _v8
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v9 = _v7.orientation
        _x = _v9
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_d.pack(val1.swing_height))
      _x = self
      buff.write(_struct_2I9dBiB3dB.pack(_x.goal.step_params.desired_step.step_index, _x.goal.step_params.desired_step.foot_index, _x.goal.step_params.desired_step.duration, _x.goal.step_params.desired_step.pose.position.x, _x.goal.step_params.desired_step.pose.position.y, _x.goal.step_params.desired_step.pose.position.z, _x.goal.step_params.desired_step.pose.orientation.x, _x.goal.step_params.desired_step.pose.orientation.y, _x.goal.step_params.desired_step.pose.orientation.z, _x.goal.step_params.desired_step.pose.orientation.w, _x.goal.step_params.desired_step.swing_height, _x.goal.step_params.use_demo_walk, _x.goal.stand_params.placeholder, _x.goal.manipulate_params.use_desired, _x.goal.manipulate_params.desired.pelvis_height, _x.goal.manipulate_params.desired.pelvis_yaw, _x.goal.manipulate_params.desired.pelvis_lat, _x.goal.manipulate_params.use_demo_mode))
      _x = self.goal.k_effort
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.goal_id is None:
        self.goal_id = actionlib_msgs.msg.GoalID()
      if self.goal is None:
        self.goal = atlas_msgs.msg.WalkDemoGoal()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.goal_id.stamp.secs, _x.goal_id.stamp.nsecs,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal_id.id = str[start:end].decode('utf-8')
      else:
        self.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.goal.header.seq, _x.goal.header.stamp.secs, _x.goal.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.goal.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.goal.header.frame_id = str[start:end]
      start = end
      end += 4
      (self.goal.behavior,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.goal.steps = []
      for i in range(0, length):
        val1 = atlas_msgs.msg.AtlasBehaviorStepData()
        _x = val1
        start = end
        end += 16
        (_x.step_index, _x.foot_index, _x.duration,) = _struct_2Id.unpack(str[start:end])
        _v10 = val1.pose
        _v11 = _v10.position
        _x = _v11
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v12 = _v10.orientation
        _x = _v12
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 8
        (val1.swing_height,) = _struct_d.unpack(str[start:end])
        self.goal.steps.append(val1)
      _x = self
      start = end
      end += 111
      (_x.goal.step_params.desired_step.step_index, _x.goal.step_params.desired_step.foot_index, _x.goal.step_params.desired_step.duration, _x.goal.step_params.desired_step.pose.position.x, _x.goal.step_params.desired_step.pose.position.y, _x.goal.step_params.desired_step.pose.position.z, _x.goal.step_params.desired_step.pose.orientation.x, _x.goal.step_params.desired_step.pose.orientation.y, _x.goal.step_params.desired_step.pose.orientation.z, _x.goal.step_params.desired_step.pose.orientation.w, _x.goal.step_params.desired_step.swing_height, _x.goal.step_params.use_demo_walk, _x.goal.stand_params.placeholder, _x.goal.manipulate_params.use_desired, _x.goal.manipulate_params.desired.pelvis_height, _x.goal.manipulate_params.desired.pelvis_yaw, _x.goal.manipulate_params.desired.pelvis_lat, _x.goal.manipulate_params.use_demo_mode,) = _struct_2I9dBiB3dB.unpack(str[start:end])
      self.goal.step_params.use_demo_walk = bool(self.goal.step_params.use_demo_walk)
      self.goal.manipulate_params.use_desired = bool(self.goal.manipulate_params.use_desired)
      self.goal.manipulate_params.use_demo_mode = bool(self.goal.manipulate_params.use_demo_mode)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.goal.k_effort = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2I9dBiB3dB = struct.Struct("<2I9dBiB3dB")
_struct_d = struct.Struct("<d")
_struct_i = struct.Struct("<i")
_struct_3I = struct.Struct("<3I")
_struct_2Id = struct.Struct("<2Id")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
