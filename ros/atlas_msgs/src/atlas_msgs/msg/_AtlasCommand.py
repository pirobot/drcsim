# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from atlas_msgs/AtlasCommand.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class AtlasCommand(genpy.Message):
  _md5sum = "3a56dd1f50633ad975636160b665384a"
  _type = "atlas_msgs/AtlasCommand"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Joint Command Message
# This structure contains the gains to be applied to a joint.
# The controller is a PID with feedforward desired torque:
#
# This message has been carefully constructed to be less
# than 1500 in size when serialized, to accommodate transfer
# UDP.
#
#   k_effort * (
#     kp_position     * ( position - measured_position )       +
#     ki_position     * 1/s * ( position - measured_position ) +
#     kd_position     * s * ( position - measured_position ) +
#     kp_velocity     * ( velocity - measured_velocity )     +
#     effort ) +
#   (1 - k_effort)  * effort_bdi
#
#  Where effort_bdi comes from AtlasSimInterface Dynamics Behavior Library.
#
Header header

float64[] position
float64[] velocity
float64[] effort

float32[] kp_position
float32[] ki_position
float32[] kd_position
float32[] kp_velocity
uint8[] k_effort       # k_effort can be an unsigned int 8value from 0 to 255, 
                       # at run time, a double between 0 and 1 is obtained
                       # by dividing by 255.0d.

float32[] i_effort_min
float32[] i_effort_max

uint8 desired_controller_period_ms # max allowed controller update period in milli-seconds simulation time for controller synchronization.  See SynchronizationStatistics.msg for tracking synchronization status.

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
"""
  __slots__ = ['header','position','velocity','effort','kp_position','ki_position','kd_position','kp_velocity','k_effort','i_effort_min','i_effort_max','desired_controller_period_ms']
  _slot_types = ['std_msgs/Header','float64[]','float64[]','float64[]','float32[]','float32[]','float32[]','float32[]','uint8[]','float32[]','float32[]','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,position,velocity,effort,kp_position,ki_position,kd_position,kp_velocity,k_effort,i_effort_min,i_effort_max,desired_controller_period_ms

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AtlasCommand, self).__init__(*args, **kwds)
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
      if self.k_effort is None:
        self.k_effort = ''
      if self.i_effort_min is None:
        self.i_effort_min = []
      if self.i_effort_max is None:
        self.i_effort_max = []
      if self.desired_controller_period_ms is None:
        self.desired_controller_period_ms = 0
    else:
      self.header = std_msgs.msg.Header()
      self.position = []
      self.velocity = []
      self.effort = []
      self.kp_position = []
      self.ki_position = []
      self.kd_position = []
      self.kp_velocity = []
      self.k_effort = ''
      self.i_effort_min = []
      self.i_effort_max = []
      self.desired_controller_period_ms = 0

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
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.position))
      length = len(self.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.velocity))
      length = len(self.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
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
      _x = self.k_effort
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.i_effort_min)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.i_effort_min))
      length = len(self.i_effort_max)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.i_effort_max))
      buff.write(_struct_B.pack(self.desired_controller_period_ms))
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
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.position = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocity = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
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
      start = end
      end += length
      self.k_effort = str[start:end]
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
      end += 1
      (self.desired_controller_period_ms,) = _struct_B.unpack(str[start:end])
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
      pattern = '<%sd'%length
      buff.write(self.position.tostring())
      length = len(self.velocity)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.velocity.tostring())
      length = len(self.effort)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
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
      _x = self.k_effort
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.i_effort_min)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.i_effort_min.tostring())
      length = len(self.i_effort_max)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.i_effort_max.tostring())
      buff.write(_struct_B.pack(self.desired_controller_period_ms))
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
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.position = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.effort = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
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
      start = end
      end += length
      self.k_effort = str[start:end]
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
      end += 1
      (self.desired_controller_period_ms,) = _struct_B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
