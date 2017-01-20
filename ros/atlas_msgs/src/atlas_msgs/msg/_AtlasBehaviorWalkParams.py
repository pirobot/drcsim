# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from atlas_msgs/AtlasBehaviorWalkParams.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import atlas_msgs.msg

class AtlasBehaviorWalkParams(genpy.Message):
  _md5sum = "0a5b4bccbb6f87ef4f591430c3499c4f"
  _type = "atlas_msgs/AtlasBehaviorWalkParams"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# multi_step walking trajectory parameters
atlas_msgs/AtlasBehaviorStepData[4] step_queue
bool use_demo_walk

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
"""
  __slots__ = ['step_queue','use_demo_walk']
  _slot_types = ['atlas_msgs/AtlasBehaviorStepData[4]','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       step_queue,use_demo_walk

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AtlasBehaviorWalkParams, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.step_queue is None:
        self.step_queue = [atlas_msgs.msg.AtlasBehaviorStepData(),atlas_msgs.msg.AtlasBehaviorStepData(),atlas_msgs.msg.AtlasBehaviorStepData(),atlas_msgs.msg.AtlasBehaviorStepData()]
      if self.use_demo_walk is None:
        self.use_demo_walk = False
    else:
      self.step_queue = [atlas_msgs.msg.AtlasBehaviorStepData(),atlas_msgs.msg.AtlasBehaviorStepData(),atlas_msgs.msg.AtlasBehaviorStepData(),atlas_msgs.msg.AtlasBehaviorStepData()]
      self.use_demo_walk = False

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
      for val1 in self.step_queue:
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
      buff.write(_struct_B.pack(self.use_demo_walk))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.step_queue is None:
        self.step_queue = None
      end = 0
      self.step_queue = []
      for i in range(0, 4):
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
        self.step_queue.append(val1)
      start = end
      end += 1
      (self.use_demo_walk,) = _struct_B.unpack(str[start:end])
      self.use_demo_walk = bool(self.use_demo_walk)
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
      for val1 in self.step_queue:
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
      buff.write(_struct_B.pack(self.use_demo_walk))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.step_queue is None:
        self.step_queue = None
      end = 0
      self.step_queue = []
      for i in range(0, 4):
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
        self.step_queue.append(val1)
      start = end
      end += 1
      (self.use_demo_walk,) = _struct_B.unpack(str[start:end])
      self.use_demo_walk = bool(self.use_demo_walk)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_d = struct.Struct("<d")
_struct_2Id = struct.Struct("<2Id")
_struct_B = struct.Struct("<B")
_struct_4d = struct.Struct("<4d")
_struct_3d = struct.Struct("<3d")
