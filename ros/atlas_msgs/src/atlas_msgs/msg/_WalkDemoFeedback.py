# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from atlas_msgs/WalkDemoFeedback.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg
import atlas_msgs.msg

class WalkDemoFeedback(genpy.Message):
  _md5sum = "dbaa9607b44a2efe654c751e0bae6116"
  _type = "atlas_msgs/WalkDemoFeedback"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Feedback
atlas_msgs/AtlasSimInterfaceState state


================================================================================
MSG: atlas_msgs/AtlasSimInterfaceState
# For interfacing Boston Dynamics' AtlasSimInterface Dynamics Behavior Library
# Feedback from AtlasSimInterface Controller after calling process_control_input
# This ROS message should track AtlasControlOutput struct in
# AtlasSimInterfaceTypes.h.
# With the exception of addition of k_effort to provide user a way to switch
# to/from PID servo control in AtlasPlugin.cpp on a per joint basis.

int32 NO_ERRORS                        =  0    # no error detected
int32 ERROR_UNSPECIFIED                = -1    # unspecified error
int32 ERROR_VALUE_OUT_OF_RANGE         = -2    # passed value is out of range
int32 ERROR_INVALID_INDEX              = -3    # passed index is invalid (too low or too high)
int32 ERROR_FAILED_TO_START_BEHAVIOR   = -4    # robot failed to start desired behavior
int32 ERROR_NO_ACTIVE_BEHAVIOR         = -5    # robot has no active behavior
int32 ERROR_NO_SUCH_BEHAVIOR           = -6    # behavior doesn't exist
int32 ERROR_BEHAVIOR_NOT_IMPLEMENTED   = -7    # behavior exists but not implemented
int32 ERROR_TIME_RAN_BACKWARD          = -8    # a time earlier than previous times was given

Header header

int32 error_code                         # error code returned by
                                         # process_control_input.
                                         # See AtlasSimInterfaceTypes.h
                                         # AtlasErrorCode for list of enums.
                                         # The list is mimic'd here above.

int32 current_behavior                   # current active behavior.
int32 desired_behavior                   # desired behavior specified by usesr
                                         # input. This may lag from
                                         # current_behavior by a few simulation
                                         # steps.

# below are information from AtlasControlOutput in AtlasSimInterfaceTypes.h

float64[28] f_out                        # torque command from BDI controller.

atlas_msgs/AtlasPositionData pos_est     # Position and velocity estimate of robot pelvis

geometry_msgs/Pose[2] foot_pos_est      # World position estimate for feet
                                         # 0 - left, 1 - right

atlas_msgs/AtlasBehaviorFeedback behavior_feedback
atlas_msgs/AtlasBehaviorStepFeedback step_feedback
atlas_msgs/AtlasBehaviorStandFeedback stand_feedback
atlas_msgs/AtlasBehaviorWalkFeedback walk_feedback
atlas_msgs/AtlasBehaviorManipulateFeedback manipulate_feedback

# additional vector for transitioning from servo model in AtlasPlugin
# to BDI servo.

uint8[] k_effort       # k_effort can be an unsigned int 8value from 0 to 255, 
                       # at run time, a double between 0 and 1 is obtained
                       # by dividing by 255.0d.


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
MSG: atlas_msgs/AtlasPositionData
# mirrors AtlasPositionData in AtlasControlTypes.h
geometry_msgs/Vector3 position
geometry_msgs/Vector3 velocity

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
MSG: atlas_msgs/AtlasBehaviorFeedback
# mirrors AtlasBehaviorFeedback
#
# Transition flags:
#    - STATUS_TRANSITION_IN_PROGRESS
#
#        A transition is in progress.
#
#    - STATUS_TRANSITION_SUCCESS
#
#        Successful transition.
#
#    - STATUS_FAILED_TRANS_UNKNOWN_BEHAVIOR
#
#        Failed to transition; unknown behavior.
#
#    - STATUS_FAILED_TRANS_ILLEGAL_BEHAVIOR
#
#        Denied request for an illegal behavior transition.  This may
#        happen if a transition to a new behavior is requested without
#        going through a required intermediate behavior. (e.g., can't
#        go from Walk straight to Manipulate.)
#
#    - STATUS_FAILED_TRANS_COM_POS
#
#        Failed to transition; the position of the COM is too far from
#        the center of support.
#
#    - STATUS_FAILED_TRANS_COM_VEL
#
#        Failed to transition; the COM velocity too high.
#
#    - STATUS_FAILED_TRANS_VEL
#
#        Failed to transition; some joint velocities too high.
#
#  \em Warnings:
#
#    - STATUS_WARNING_AUTO_TRANS
#
#        An automatic transition occurred; see behavior specific
#        feedback for reason.
#
#  \em Errors:
#
#    - STATUS_ERROR_FALLING
#
#        COM below acceptable threshold, cannot recover.

# copied from AtlasBehaviorFlags
uint32 STATUS_OK                            = 0
uint32 STATUS_TRANSITION_IN_PROGRESS        = 1
uint32 STATUS_TRANSITION_SUCCESS            = 2
uint32 STATUS_FAILED_TRANS_UNKNOWN_BEHAVIOR = 4
uint32 STATUS_FAILED_TRANS_ILLEGAL_BEHAVIOR = 8
uint32 STATUS_FAILED_TRANS_COM_POS          = 16
uint32 STATUS_FAILED_TRANS_COM_VEL          = 32
uint32 STATUS_FAILED_TRANS_VEL              = 64
uint32 STATUS_WARNING_AUTO_TRANS            = 128
uint32 STATUS_ERROR_FALLING                 = 256

uint32 status_flags  # can be one of above

int32 trans_from_behavior_index  # use this as a parm to get_behavior_at_index() to get behavior string
int32 trans_to_behavior_index  # use this as a parm to get_behavior_at_index() to get behavior string

================================================================================
MSG: atlas_msgs/AtlasBehaviorStepFeedback
# mirrored from AtlasControlTypes.h
uint32 STEP_SUBSTATE_SWAYING = 0  # Feet are in double support. This flag does not latch. Only one of STEP_SUBSTATE_SWAYING or STEP_SUBSTATE_STEPPING will be set at any given time.
uint32 STEP_SUBSTATE_STEPPING = 1 # Actively stepping; one foot is in the air. This flag does not latch.

uint32 status_flags    # use AtlasBeahviorFeedback/status_flags
float64 t_step_rem
uint32 current_step_index
uint32 next_step_index_needed
atlas_msgs/AtlasBehaviorStepData desired_step_saturated

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
MSG: atlas_msgs/AtlasBehaviorStandFeedback
# mirrored from AtlasControlTypes.h
uint32 status_flags    # use AtlasBeahviorStandFlags

================================================================================
MSG: atlas_msgs/AtlasBehaviorWalkFeedback
# mirrored from AtlasControlTypes.h
float64 t_step_rem
uint32 current_step_index
uint32 next_step_index_needed
uint32 status_flags    # use AtlasBeahviorFeedback/status_flags
atlas_msgs/AtlasBehaviorStepData[4] step_queue_saturated # 4 is hardcoded in AtlasSimInterface library.

================================================================================
MSG: atlas_msgs/AtlasBehaviorManipulateFeedback
# mirrored from AtlasControlTypes.h
uint32 status_flags    # use AtlasBeahviorManipulateFlags
atlas_msgs/AtlasBehaviorPelvisServoParams clamped

================================================================================
MSG: atlas_msgs/AtlasBehaviorPelvisServoParams
# mirrored from AtlasControlTypes.h

float64 pelvis_height
float64 pelvis_yaw
float64 pelvis_lat
"""
  __slots__ = ['state']
  _slot_types = ['atlas_msgs/AtlasSimInterfaceState']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       state

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WalkDemoFeedback, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.state is None:
        self.state = atlas_msgs.msg.AtlasSimInterfaceState()
    else:
      self.state = atlas_msgs.msg.AtlasSimInterfaceState()

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
      buff.write(_struct_3I.pack(_x.state.header.seq, _x.state.header.stamp.secs, _x.state.header.stamp.nsecs))
      _x = self.state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3i.pack(_x.state.error_code, _x.state.current_behavior, _x.state.desired_behavior))
      buff.write(_struct_28d.pack(*self.state.f_out))
      _x = self
      buff.write(_struct_6d.pack(_x.state.pos_est.position.x, _x.state.pos_est.position.y, _x.state.pos_est.position.z, _x.state.pos_est.velocity.x, _x.state.pos_est.velocity.y, _x.state.pos_est.velocity.z))
      for val1 in self.state.foot_pos_est:
        _v1 = val1.position
        _x = _v1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v2 = val1.orientation
        _x = _v2
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_struct_I2iId4I9dId3I.pack(_x.state.behavior_feedback.status_flags, _x.state.behavior_feedback.trans_from_behavior_index, _x.state.behavior_feedback.trans_to_behavior_index, _x.state.step_feedback.status_flags, _x.state.step_feedback.t_step_rem, _x.state.step_feedback.current_step_index, _x.state.step_feedback.next_step_index_needed, _x.state.step_feedback.desired_step_saturated.step_index, _x.state.step_feedback.desired_step_saturated.foot_index, _x.state.step_feedback.desired_step_saturated.duration, _x.state.step_feedback.desired_step_saturated.pose.position.x, _x.state.step_feedback.desired_step_saturated.pose.position.y, _x.state.step_feedback.desired_step_saturated.pose.position.z, _x.state.step_feedback.desired_step_saturated.pose.orientation.x, _x.state.step_feedback.desired_step_saturated.pose.orientation.y, _x.state.step_feedback.desired_step_saturated.pose.orientation.z, _x.state.step_feedback.desired_step_saturated.pose.orientation.w, _x.state.step_feedback.desired_step_saturated.swing_height, _x.state.stand_feedback.status_flags, _x.state.walk_feedback.t_step_rem, _x.state.walk_feedback.current_step_index, _x.state.walk_feedback.next_step_index_needed, _x.state.walk_feedback.status_flags))
      for val1 in self.state.walk_feedback.step_queue_saturated:
        _x = val1
        buff.write(_struct_2Id.pack(_x.step_index, _x.foot_index, _x.duration))
        _v3 = val1.pose
        _v4 = _v3.position
        _x = _v4
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v5 = _v3.orientation
        _x = _v5
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_d.pack(val1.swing_height))
      _x = self
      buff.write(_struct_I3d.pack(_x.state.manipulate_feedback.status_flags, _x.state.manipulate_feedback.clamped.pelvis_height, _x.state.manipulate_feedback.clamped.pelvis_yaw, _x.state.manipulate_feedback.clamped.pelvis_lat))
      _x = self.state.k_effort
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
      if self.state is None:
        self.state = atlas_msgs.msg.AtlasSimInterfaceState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.state.header.seq, _x.state.header.stamp.secs, _x.state.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.state.error_code, _x.state.current_behavior, _x.state.desired_behavior,) = _struct_3i.unpack(str[start:end])
      start = end
      end += 224
      self.state.f_out = _struct_28d.unpack(str[start:end])
      _x = self
      start = end
      end += 48
      (_x.state.pos_est.position.x, _x.state.pos_est.position.y, _x.state.pos_est.position.z, _x.state.pos_est.velocity.x, _x.state.pos_est.velocity.y, _x.state.pos_est.velocity.z,) = _struct_6d.unpack(str[start:end])
      self.state.foot_pos_est = []
      for i in range(0, 2):
        val1 = geometry_msgs.msg.Pose()
        _v6 = val1.position
        _x = _v6
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v7 = val1.orientation
        _x = _v7
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        self.state.foot_pos_est.append(val1)
      _x = self
      start = end
      end += 136
      (_x.state.behavior_feedback.status_flags, _x.state.behavior_feedback.trans_from_behavior_index, _x.state.behavior_feedback.trans_to_behavior_index, _x.state.step_feedback.status_flags, _x.state.step_feedback.t_step_rem, _x.state.step_feedback.current_step_index, _x.state.step_feedback.next_step_index_needed, _x.state.step_feedback.desired_step_saturated.step_index, _x.state.step_feedback.desired_step_saturated.foot_index, _x.state.step_feedback.desired_step_saturated.duration, _x.state.step_feedback.desired_step_saturated.pose.position.x, _x.state.step_feedback.desired_step_saturated.pose.position.y, _x.state.step_feedback.desired_step_saturated.pose.position.z, _x.state.step_feedback.desired_step_saturated.pose.orientation.x, _x.state.step_feedback.desired_step_saturated.pose.orientation.y, _x.state.step_feedback.desired_step_saturated.pose.orientation.z, _x.state.step_feedback.desired_step_saturated.pose.orientation.w, _x.state.step_feedback.desired_step_saturated.swing_height, _x.state.stand_feedback.status_flags, _x.state.walk_feedback.t_step_rem, _x.state.walk_feedback.current_step_index, _x.state.walk_feedback.next_step_index_needed, _x.state.walk_feedback.status_flags,) = _struct_I2iId4I9dId3I.unpack(str[start:end])
      self.state.walk_feedback.step_queue_saturated = []
      for i in range(0, 4):
        val1 = atlas_msgs.msg.AtlasBehaviorStepData()
        _x = val1
        start = end
        end += 16
        (_x.step_index, _x.foot_index, _x.duration,) = _struct_2Id.unpack(str[start:end])
        _v8 = val1.pose
        _v9 = _v8.position
        _x = _v9
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v10 = _v8.orientation
        _x = _v10
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 8
        (val1.swing_height,) = _struct_d.unpack(str[start:end])
        self.state.walk_feedback.step_queue_saturated.append(val1)
      _x = self
      start = end
      end += 28
      (_x.state.manipulate_feedback.status_flags, _x.state.manipulate_feedback.clamped.pelvis_height, _x.state.manipulate_feedback.clamped.pelvis_yaw, _x.state.manipulate_feedback.clamped.pelvis_lat,) = _struct_I3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.state.k_effort = str[start:end]
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
      buff.write(_struct_3I.pack(_x.state.header.seq, _x.state.header.stamp.secs, _x.state.header.stamp.nsecs))
      _x = self.state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3i.pack(_x.state.error_code, _x.state.current_behavior, _x.state.desired_behavior))
      buff.write(self.state.f_out.tostring())
      _x = self
      buff.write(_struct_6d.pack(_x.state.pos_est.position.x, _x.state.pos_est.position.y, _x.state.pos_est.position.z, _x.state.pos_est.velocity.x, _x.state.pos_est.velocity.y, _x.state.pos_est.velocity.z))
      for val1 in self.state.foot_pos_est:
        _v11 = val1.position
        _x = _v11
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v12 = val1.orientation
        _x = _v12
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_struct_I2iId4I9dId3I.pack(_x.state.behavior_feedback.status_flags, _x.state.behavior_feedback.trans_from_behavior_index, _x.state.behavior_feedback.trans_to_behavior_index, _x.state.step_feedback.status_flags, _x.state.step_feedback.t_step_rem, _x.state.step_feedback.current_step_index, _x.state.step_feedback.next_step_index_needed, _x.state.step_feedback.desired_step_saturated.step_index, _x.state.step_feedback.desired_step_saturated.foot_index, _x.state.step_feedback.desired_step_saturated.duration, _x.state.step_feedback.desired_step_saturated.pose.position.x, _x.state.step_feedback.desired_step_saturated.pose.position.y, _x.state.step_feedback.desired_step_saturated.pose.position.z, _x.state.step_feedback.desired_step_saturated.pose.orientation.x, _x.state.step_feedback.desired_step_saturated.pose.orientation.y, _x.state.step_feedback.desired_step_saturated.pose.orientation.z, _x.state.step_feedback.desired_step_saturated.pose.orientation.w, _x.state.step_feedback.desired_step_saturated.swing_height, _x.state.stand_feedback.status_flags, _x.state.walk_feedback.t_step_rem, _x.state.walk_feedback.current_step_index, _x.state.walk_feedback.next_step_index_needed, _x.state.walk_feedback.status_flags))
      for val1 in self.state.walk_feedback.step_queue_saturated:
        _x = val1
        buff.write(_struct_2Id.pack(_x.step_index, _x.foot_index, _x.duration))
        _v13 = val1.pose
        _v14 = _v13.position
        _x = _v14
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v15 = _v13.orientation
        _x = _v15
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_d.pack(val1.swing_height))
      _x = self
      buff.write(_struct_I3d.pack(_x.state.manipulate_feedback.status_flags, _x.state.manipulate_feedback.clamped.pelvis_height, _x.state.manipulate_feedback.clamped.pelvis_yaw, _x.state.manipulate_feedback.clamped.pelvis_lat))
      _x = self.state.k_effort
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
      if self.state is None:
        self.state = atlas_msgs.msg.AtlasSimInterfaceState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.state.header.seq, _x.state.header.stamp.secs, _x.state.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.state.error_code, _x.state.current_behavior, _x.state.desired_behavior,) = _struct_3i.unpack(str[start:end])
      start = end
      end += 224
      self.state.f_out = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=28)
      _x = self
      start = end
      end += 48
      (_x.state.pos_est.position.x, _x.state.pos_est.position.y, _x.state.pos_est.position.z, _x.state.pos_est.velocity.x, _x.state.pos_est.velocity.y, _x.state.pos_est.velocity.z,) = _struct_6d.unpack(str[start:end])
      self.state.foot_pos_est = []
      for i in range(0, 2):
        val1 = geometry_msgs.msg.Pose()
        _v16 = val1.position
        _x = _v16
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v17 = val1.orientation
        _x = _v17
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        self.state.foot_pos_est.append(val1)
      _x = self
      start = end
      end += 136
      (_x.state.behavior_feedback.status_flags, _x.state.behavior_feedback.trans_from_behavior_index, _x.state.behavior_feedback.trans_to_behavior_index, _x.state.step_feedback.status_flags, _x.state.step_feedback.t_step_rem, _x.state.step_feedback.current_step_index, _x.state.step_feedback.next_step_index_needed, _x.state.step_feedback.desired_step_saturated.step_index, _x.state.step_feedback.desired_step_saturated.foot_index, _x.state.step_feedback.desired_step_saturated.duration, _x.state.step_feedback.desired_step_saturated.pose.position.x, _x.state.step_feedback.desired_step_saturated.pose.position.y, _x.state.step_feedback.desired_step_saturated.pose.position.z, _x.state.step_feedback.desired_step_saturated.pose.orientation.x, _x.state.step_feedback.desired_step_saturated.pose.orientation.y, _x.state.step_feedback.desired_step_saturated.pose.orientation.z, _x.state.step_feedback.desired_step_saturated.pose.orientation.w, _x.state.step_feedback.desired_step_saturated.swing_height, _x.state.stand_feedback.status_flags, _x.state.walk_feedback.t_step_rem, _x.state.walk_feedback.current_step_index, _x.state.walk_feedback.next_step_index_needed, _x.state.walk_feedback.status_flags,) = _struct_I2iId4I9dId3I.unpack(str[start:end])
      self.state.walk_feedback.step_queue_saturated = []
      for i in range(0, 4):
        val1 = atlas_msgs.msg.AtlasBehaviorStepData()
        _x = val1
        start = end
        end += 16
        (_x.step_index, _x.foot_index, _x.duration,) = _struct_2Id.unpack(str[start:end])
        _v18 = val1.pose
        _v19 = _v18.position
        _x = _v19
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v20 = _v18.orientation
        _x = _v20
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 8
        (val1.swing_height,) = _struct_d.unpack(str[start:end])
        self.state.walk_feedback.step_queue_saturated.append(val1)
      _x = self
      start = end
      end += 28
      (_x.state.manipulate_feedback.status_flags, _x.state.manipulate_feedback.clamped.pelvis_height, _x.state.manipulate_feedback.clamped.pelvis_yaw, _x.state.manipulate_feedback.clamped.pelvis_lat,) = _struct_I3d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.state.k_effort = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6d = struct.Struct("<6d")
_struct_d = struct.Struct("<d")
_struct_3i = struct.Struct("<3i")
_struct_28d = struct.Struct("<28d")
_struct_I2iId4I9dId3I = struct.Struct("<I2iId4I9dId3I")
_struct_3I = struct.Struct("<3I")
_struct_4d = struct.Struct("<4d")
_struct_I3d = struct.Struct("<I3d")
_struct_2Id = struct.Struct("<2Id")
_struct_3d = struct.Struct("<3d")
