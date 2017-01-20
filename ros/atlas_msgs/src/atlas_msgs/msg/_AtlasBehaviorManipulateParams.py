# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from atlas_msgs/AtlasBehaviorManipulateParams.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import atlas_msgs.msg

class AtlasBehaviorManipulateParams(genpy.Message):
  _md5sum = "c4e967ec87266f9e108243e7ac4b9614"
  _type = "atlas_msgs/AtlasBehaviorManipulateParams"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# mirrored from AtlasControlTypes.h
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
  __slots__ = ['use_desired','desired','use_demo_mode']
  _slot_types = ['bool','atlas_msgs/AtlasBehaviorPelvisServoParams','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       use_desired,desired,use_demo_mode

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AtlasBehaviorManipulateParams, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.use_desired is None:
        self.use_desired = False
      if self.desired is None:
        self.desired = atlas_msgs.msg.AtlasBehaviorPelvisServoParams()
      if self.use_demo_mode is None:
        self.use_demo_mode = False
    else:
      self.use_desired = False
      self.desired = atlas_msgs.msg.AtlasBehaviorPelvisServoParams()
      self.use_demo_mode = False

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
      buff.write(_struct_B3dB.pack(_x.use_desired, _x.desired.pelvis_height, _x.desired.pelvis_yaw, _x.desired.pelvis_lat, _x.use_demo_mode))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.desired is None:
        self.desired = atlas_msgs.msg.AtlasBehaviorPelvisServoParams()
      end = 0
      _x = self
      start = end
      end += 26
      (_x.use_desired, _x.desired.pelvis_height, _x.desired.pelvis_yaw, _x.desired.pelvis_lat, _x.use_demo_mode,) = _struct_B3dB.unpack(str[start:end])
      self.use_desired = bool(self.use_desired)
      self.use_demo_mode = bool(self.use_demo_mode)
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
      buff.write(_struct_B3dB.pack(_x.use_desired, _x.desired.pelvis_height, _x.desired.pelvis_yaw, _x.desired.pelvis_lat, _x.use_demo_mode))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.desired is None:
        self.desired = atlas_msgs.msg.AtlasBehaviorPelvisServoParams()
      end = 0
      _x = self
      start = end
      end += 26
      (_x.use_desired, _x.desired.pelvis_height, _x.desired.pelvis_yaw, _x.desired.pelvis_lat, _x.use_demo_mode,) = _struct_B3dB.unpack(str[start:end])
      self.use_desired = bool(self.use_desired)
      self.use_demo_mode = bool(self.use_demo_mode)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B3dB = struct.Struct("<B3dB")
