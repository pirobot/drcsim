# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from atlas_msgs/AtlasBehaviorPelvisServoParams.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class AtlasBehaviorPelvisServoParams(genpy.Message):
  _md5sum = "82f59d8aa26e61afaf2c8dbb7b4e7856"
  _type = "atlas_msgs/AtlasBehaviorPelvisServoParams"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# mirrored from AtlasControlTypes.h

float64 pelvis_height
float64 pelvis_yaw
float64 pelvis_lat
"""
  __slots__ = ['pelvis_height','pelvis_yaw','pelvis_lat']
  _slot_types = ['float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pelvis_height,pelvis_yaw,pelvis_lat

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AtlasBehaviorPelvisServoParams, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pelvis_height is None:
        self.pelvis_height = 0.
      if self.pelvis_yaw is None:
        self.pelvis_yaw = 0.
      if self.pelvis_lat is None:
        self.pelvis_lat = 0.
    else:
      self.pelvis_height = 0.
      self.pelvis_yaw = 0.
      self.pelvis_lat = 0.

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
      buff.write(_struct_3d.pack(_x.pelvis_height, _x.pelvis_yaw, _x.pelvis_lat))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.pelvis_height, _x.pelvis_yaw, _x.pelvis_lat,) = _struct_3d.unpack(str[start:end])
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
      buff.write(_struct_3d.pack(_x.pelvis_height, _x.pelvis_yaw, _x.pelvis_lat))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.pelvis_height, _x.pelvis_yaw, _x.pelvis_lat,) = _struct_3d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3d = struct.Struct("<3d")
