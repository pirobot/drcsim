# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from atlas_msgs/AtlasState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class AtlasState(genpy.Message):
  _md5sum = "f401ea8c0dd89918d4fa3a58c57816e6"
  _type = "atlas_msgs/AtlasState"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """#
# This message has been carefully constructed to be less
# than 1500 in size when serialized, to accommodate transfer
# UDP.
#
# testing everything a robot needs
Header header

# Default joint indices used when publishing the
# JointCommands joint_states topic below
# For exmaple, if you subscribe to this message, then
# msg.joint_states.position[atlas_msgs::AtlasStates::back_lbz] gives back
# the position of the back_lbz.
int32 back_lbz  = 0
int32 back_mby  = 1
int32 back_ubx  = 2
int32 neck_ay   = 3
int32 l_leg_uhz = 4
int32 l_leg_mhx = 5
int32 l_leg_lhy = 6
int32 l_leg_kny = 7
int32 l_leg_uay = 8
int32 l_leg_lax = 9
int32 r_leg_uhz = 10
int32 r_leg_mhx = 11
int32 r_leg_lhy = 12
int32 r_leg_kny = 13
int32 r_leg_uay = 14
int32 r_leg_lax = 15
int32 l_arm_usy = 16
int32 l_arm_shx = 17
int32 l_arm_ely = 18
int32 l_arm_elx = 19
int32 l_arm_uwy = 20
int32 l_arm_mwx = 21
int32 r_arm_usy = 22
int32 r_arm_shx = 23
int32 r_arm_ely = 24
int32 r_arm_elx = 25
int32 r_arm_uwy = 26
int32 r_arm_mwx = 27

# repeating data from osrf_msgs/JointCommands as joint_states
float32[] position
float32[] velocity
float32[] effort
float32[] kp_position
float32[] ki_position
float32[] kd_position
float32[] kp_velocity
float32[] i_effort_min
float32[] i_effort_max

uint8[] k_effort       # k_effort can be an unsigned int 8value from 0 to 255, 
                       # at run time, a double between 0 and 1 is obtained
                       # by dividing by 255.0d.


#sensor_msgs/Imu imu 
geometry_msgs/Quaternion orientation
geometry_msgs/Vector3 angular_velocity
geometry_msgs/Vector3 linear_acceleration

#atlas_msgs/ForceTorqueSensors force_torque_sensors
geometry_msgs/Wrench l_foot
geometry_msgs/Wrench r_foot
geometry_msgs/Wrench l_hand
geometry_msgs/Wrench r_hand

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
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Wrench
# This represents force in free space, separated into
# its linear and angular parts.
Vector3  force
Vector3  torque
"""
  # Pseudo-constants
  back_lbz = 0
  back_mby = 1
  back_ubx = 2
  neck_ay = 3
  l_leg_uhz = 4
  l_leg_mhx = 5
  l_leg_lhy = 6
  l_leg_kny = 7
  l_leg_uay = 8
  l_leg_lax = 9
  r_leg_uhz = 10
  r_leg_mhx = 11
  r_leg_lhy = 12
  r_leg_kny = 13
  r_leg_uay = 14
  r_leg_lax = 15
  l_arm_usy = 16
  l_arm_shx = 17
  l_arm_ely = 18
  l_arm_elx = 19
  l_arm_uwy = 20
  l_arm_mwx = 21
  r_arm_usy = 22
  r_arm_shx = 23
  r_arm_ely = 24
  r_arm_elx = 25
  r_arm_uwy = 26
  r_arm_mwx = 27

  __slots__ = ['header','position','velocity','effort','kp_position','ki_position','kd_position','kp_velocity','i_effort_min','i_effort_max','k_effort','orientation','angular_velocity','linear_acceleration','l_foot','r_foot','l_hand','r_hand']
  _slot_types = ['std_msgs/Header','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','float32[]','uint8[]','geometry_msgs/Quaternion','geometry_msgs/Vector3','geometry_msgs/Vector3','geometry_msgs/Wrench','geometry_msgs/Wrench','geometry_msgs/Wrench','geometry_msgs/Wrench']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,position,velocity,effort,kp_position,ki_position,kd_position,kp_velocity,i_effort_min,i_effort_max,k_effort,orientation,angular_velocity,linear_acceleration,l_foot,r_foot,l_hand,r_hand

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AtlasState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.position is None:
        self.position = []
      if self.velocity is None:
        self.velocity = []
      if self.effort is None:
        self.effort = []
      if self.kp_position is None:
        self.kp_position = []
      if self.ki_position is None:
        self.ki_position = []
      if self.kd_position is None:
        self.kd_position = []
      if self.kp_velocity is None:
        self.kp_velocity = []
      if self.i_effort_min is None:
        self.i_effort_min = []
      if self.i_effort_max is None:
        self.i_effort_max = []
      if self.k_effort is None:
        self.k_effort = ''
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.l_foot is None:
        self.l_foot = geometry_msgs.msg.Wrench()
      if self.r_foot is None:
        self.r_foot = geometry_msgs.msg.Wrench()
      if self.l_hand is None:
        self.l_hand = geometry_msgs.msg.Wrench()
      if self.r_hand is None:
        self.r_hand = geometry_msgs.msg.Wrench()
    else:
      self.header = std_msgs.msg.Header()
      self.position = []
      self.velocity = []
      self.effort = []
      self.kp_position = []
      self.ki_position = []
      self.kd_position = []
      self.kp_velocity = []
      self.i_effort_min = []
      self.i_effort_max = []
      self.k_effort = ''
      self.orientation = geometry_msgs.msg.Quaternion()
      self.angular_velocity = geometry_msgs.msg.Vector3()
      self.linear_acceleration = geometry_msgs.msg.Vector3()
      self.l_foot = geometry_msgs.msg.Wrench()
      self.r_foot = geometry_msgs.msg.Wrench()
      self.l_hand = geometry_msgs.msg.Wrench()
      self.r_hand = geometry_msgs.msg.Wrench()

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
      length = len(self.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.position))
      length = len(self.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.velocity))
      length = len(self.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.effort))
      length = len(self.kp_position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.kp_position))
      length = len(self.ki_position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.ki_position))
      length = len(self.kd_position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.kd_position))
      length = len(self.kp_velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.kp_velocity))
      length = len(self.i_effort_min)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.i_effort_min))
      length = len(self.i_effort_max)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.i_effort_max))
      _x = self.k_effort
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_34d.pack(_x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.l_foot.force.x, _x.l_foot.force.y, _x.l_foot.force.z, _x.l_foot.torque.x, _x.l_foot.torque.y, _x.l_foot.torque.z, _x.r_foot.force.x, _x.r_foot.force.y, _x.r_foot.force.z, _x.r_foot.torque.x, _x.r_foot.torque.y, _x.r_foot.torque.z, _x.l_hand.force.x, _x.l_hand.force.y, _x.l_hand.force.z, _x.l_hand.torque.x, _x.l_hand.torque.y, _x.l_hand.torque.z, _x.r_hand.force.x, _x.r_hand.force.y, _x.r_hand.force.z, _x.r_hand.torque.x, _x.r_hand.torque.y, _x.r_hand.torque.z))
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
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.l_foot is None:
        self.l_foot = geometry_msgs.msg.Wrench()
      if self.r_foot is None:
        self.r_foot = geometry_msgs.msg.Wrench()
      if self.l_hand is None:
        self.l_hand = geometry_msgs.msg.Wrench()
      if self.r_hand is None:
        self.r_hand = geometry_msgs.msg.Wrench()
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.position = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocity = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.kp_position = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.ki_position = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.kd_position = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.kp_velocity = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.i_effort_min = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.i_effort_max = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.k_effort = str[start:end]
      _x = self
      start = end
      end += 272
      (_x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.l_foot.force.x, _x.l_foot.force.y, _x.l_foot.force.z, _x.l_foot.torque.x, _x.l_foot.torque.y, _x.l_foot.torque.z, _x.r_foot.force.x, _x.r_foot.force.y, _x.r_foot.force.z, _x.r_foot.torque.x, _x.r_foot.torque.y, _x.r_foot.torque.z, _x.l_hand.force.x, _x.l_hand.force.y, _x.l_hand.force.z, _x.l_hand.torque.x, _x.l_hand.torque.y, _x.l_hand.torque.z, _x.r_hand.force.x, _x.r_hand.force.y, _x.r_hand.force.z, _x.r_hand.torque.x, _x.r_hand.torque.y, _x.r_hand.torque.z,) = _struct_34d.unpack(str[start:end])
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
      length = len(self.position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.position.tostring())
      length = len(self.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.velocity.tostring())
      length = len(self.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.effort.tostring())
      length = len(self.kp_position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.kp_position.tostring())
      length = len(self.ki_position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.ki_position.tostring())
      length = len(self.kd_position)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.kd_position.tostring())
      length = len(self.kp_velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.kp_velocity.tostring())
      length = len(self.i_effort_min)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.i_effort_min.tostring())
      length = len(self.i_effort_max)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.i_effort_max.tostring())
      _x = self.k_effort
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_34d.pack(_x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.l_foot.force.x, _x.l_foot.force.y, _x.l_foot.force.z, _x.l_foot.torque.x, _x.l_foot.torque.y, _x.l_foot.torque.z, _x.r_foot.force.x, _x.r_foot.force.y, _x.r_foot.force.z, _x.r_foot.torque.x, _x.r_foot.torque.y, _x.r_foot.torque.z, _x.l_hand.force.x, _x.l_hand.force.y, _x.l_hand.force.z, _x.l_hand.torque.x, _x.l_hand.torque.y, _x.l_hand.torque.z, _x.r_hand.force.x, _x.r_hand.force.y, _x.r_hand.force.z, _x.r_hand.torque.x, _x.r_hand.torque.y, _x.r_hand.torque.z))
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
      if self.orientation is None:
        self.orientation = geometry_msgs.msg.Quaternion()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.l_foot is None:
        self.l_foot = geometry_msgs.msg.Wrench()
      if self.r_foot is None:
        self.r_foot = geometry_msgs.msg.Wrench()
      if self.l_hand is None:
        self.l_hand = geometry_msgs.msg.Wrench()
      if self.r_hand is None:
        self.r_hand = geometry_msgs.msg.Wrench()
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.kp_position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.ki_position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.kd_position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.kp_velocity = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.i_effort_min = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.i_effort_max = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.k_effort = str[start:end]
      _x = self
      start = end
      end += 272
      (_x.orientation.x, _x.orientation.y, _x.orientation.z, _x.orientation.w, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.l_foot.force.x, _x.l_foot.force.y, _x.l_foot.force.z, _x.l_foot.torque.x, _x.l_foot.torque.y, _x.l_foot.torque.z, _x.r_foot.force.x, _x.r_foot.force.y, _x.r_foot.force.z, _x.r_foot.torque.x, _x.r_foot.torque.y, _x.r_foot.torque.z, _x.l_hand.force.x, _x.l_hand.force.y, _x.l_hand.force.z, _x.l_hand.torque.x, _x.l_hand.torque.y, _x.l_hand.torque.z, _x.r_hand.force.x, _x.r_hand.force.y, _x.r_hand.force.z, _x.r_hand.torque.x, _x.r_hand.torque.y, _x.r_hand.torque.z,) = _struct_34d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_34d = struct.Struct("<34d")
_struct_3I = struct.Struct("<3I")
