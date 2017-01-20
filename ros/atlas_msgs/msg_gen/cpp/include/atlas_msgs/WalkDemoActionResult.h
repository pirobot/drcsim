/* Auto-generated by genmsg_cpp for file /home/patrick/catkin_ws/src/drcsim/ros/atlas_msgs/msg/WalkDemoActionResult.msg */
#ifndef ATLAS_MSGS_MESSAGE_WALKDEMOACTIONRESULT_H
#define ATLAS_MSGS_MESSAGE_WALKDEMOACTIONRESULT_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"
#include "actionlib_msgs/GoalStatus.h"
#include "atlas_msgs/WalkDemoResult.h"

namespace atlas_msgs
{
template <class ContainerAllocator>
struct WalkDemoActionResult_ {
  typedef WalkDemoActionResult_<ContainerAllocator> Type;

  WalkDemoActionResult_()
  : header()
  , status()
  , result()
  {
  }

  WalkDemoActionResult_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , status(_alloc)
  , result(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::actionlib_msgs::GoalStatus_<ContainerAllocator>  _status_type;
   ::actionlib_msgs::GoalStatus_<ContainerAllocator>  status;

  typedef  ::atlas_msgs::WalkDemoResult_<ContainerAllocator>  _result_type;
   ::atlas_msgs::WalkDemoResult_<ContainerAllocator>  result;


  typedef boost::shared_ptr< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator>  const> ConstPtr;
}; // struct WalkDemoActionResult
typedef  ::atlas_msgs::WalkDemoActionResult_<std::allocator<void> > WalkDemoActionResult;

typedef boost::shared_ptr< ::atlas_msgs::WalkDemoActionResult> WalkDemoActionResultPtr;
typedef boost::shared_ptr< ::atlas_msgs::WalkDemoActionResult const> WalkDemoActionResultConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace atlas_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "e62dca2bf26ccbf63139e15689379528";
  }

  static const char* value(const  ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xe62dca2bf26ccbf6ULL;
  static const uint64_t static_value2 = 0x3139e15689379528ULL;
};

template<class ContainerAllocator>
struct DataType< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/WalkDemoActionResult";
  }

  static const char* value(const  ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
\n\
Header header\n\
actionlib_msgs/GoalStatus status\n\
WalkDemoResult result\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalStatus\n\
GoalID goal_id\n\
uint8 status\n\
uint8 PENDING         = 0   # The goal has yet to be processed by the action server\n\
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server\n\
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing\n\
                            #   and has since completed its execution (Terminal State)\n\
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)\n\
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due\n\
                            #    to some failure (Terminal State)\n\
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,\n\
                            #    because the goal was unattainable or invalid (Terminal State)\n\
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing\n\
                            #    and has not yet completed execution\n\
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,\n\
                            #    but the action server has not yet confirmed that the goal is canceled\n\
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing\n\
                            #    and was successfully cancelled (Terminal State)\n\
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be\n\
                            #    sent over the wire by an action server\n\
\n\
#Allow for the user to associate a string with GoalStatus for debugging\n\
string text\n\
\n\
\n\
================================================================================\n\
MSG: actionlib_msgs/GoalID\n\
# The stamp should store the time at which this goal was requested.\n\
# It is used by an action server when it tries to preempt all\n\
# goals that were requested before a certain time\n\
time stamp\n\
\n\
# The id provides a way to associate feedback and\n\
# result message with specific goal requests. The id\n\
# specified must be unique.\n\
string id\n\
\n\
\n\
================================================================================\n\
MSG: atlas_msgs/WalkDemoResult\n\
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n\
# Result\n\
atlas_msgs/AtlasSimInterfaceState end_state\n\
bool success\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasSimInterfaceState\n\
# For interfacing Boston Dynamics' AtlasSimInterface Dynamics Behavior Library\n\
# Feedback from AtlasSimInterface Controller after calling process_control_input\n\
# This ROS message should track AtlasControlOutput struct in\n\
# AtlasSimInterfaceTypes.h.\n\
# With the exception of addition of k_effort to provide user a way to switch\n\
# to/from PID servo control in AtlasPlugin.cpp on a per joint basis.\n\
\n\
int32 NO_ERRORS                        =  0    # no error detected\n\
int32 ERROR_UNSPECIFIED                = -1    # unspecified error\n\
int32 ERROR_VALUE_OUT_OF_RANGE         = -2    # passed value is out of range\n\
int32 ERROR_INVALID_INDEX              = -3    # passed index is invalid (too low or too high)\n\
int32 ERROR_FAILED_TO_START_BEHAVIOR   = -4    # robot failed to start desired behavior\n\
int32 ERROR_NO_ACTIVE_BEHAVIOR         = -5    # robot has no active behavior\n\
int32 ERROR_NO_SUCH_BEHAVIOR           = -6    # behavior doesn't exist\n\
int32 ERROR_BEHAVIOR_NOT_IMPLEMENTED   = -7    # behavior exists but not implemented\n\
int32 ERROR_TIME_RAN_BACKWARD          = -8    # a time earlier than previous times was given\n\
\n\
Header header\n\
\n\
int32 error_code                         # error code returned by\n\
                                         # process_control_input.\n\
                                         # See AtlasSimInterfaceTypes.h\n\
                                         # AtlasErrorCode for list of enums.\n\
                                         # The list is mimic'd here above.\n\
\n\
int32 current_behavior                   # current active behavior.\n\
int32 desired_behavior                   # desired behavior specified by usesr\n\
                                         # input. This may lag from\n\
                                         # current_behavior by a few simulation\n\
                                         # steps.\n\
\n\
# below are information from AtlasControlOutput in AtlasSimInterfaceTypes.h\n\
\n\
float64[28] f_out                        # torque command from BDI controller.\n\
\n\
atlas_msgs/AtlasPositionData pos_est     # Position and velocity estimate of robot pelvis\n\
\n\
geometry_msgs/Pose[2] foot_pos_est      # World position estimate for feet\n\
                                         # 0 - left, 1 - right\n\
\n\
atlas_msgs/AtlasBehaviorFeedback behavior_feedback\n\
atlas_msgs/AtlasBehaviorStepFeedback step_feedback\n\
atlas_msgs/AtlasBehaviorStandFeedback stand_feedback\n\
atlas_msgs/AtlasBehaviorWalkFeedback walk_feedback\n\
atlas_msgs/AtlasBehaviorManipulateFeedback manipulate_feedback\n\
\n\
# additional vector for transitioning from servo model in AtlasPlugin\n\
# to BDI servo.\n\
\n\
uint8[] k_effort       # k_effort can be an unsigned int 8value from 0 to 255, \n\
                       # at run time, a double between 0 and 1 is obtained\n\
                       # by dividing by 255.0d.\n\
\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasPositionData\n\
# mirrors AtlasPositionData in AtlasControlTypes.h\n\
geometry_msgs/Vector3 position\n\
geometry_msgs/Vector3 velocity\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasBehaviorFeedback\n\
# mirrors AtlasBehaviorFeedback\n\
#\n\
# Transition flags:\n\
#    - STATUS_TRANSITION_IN_PROGRESS\n\
#\n\
#        A transition is in progress.\n\
#\n\
#    - STATUS_TRANSITION_SUCCESS\n\
#\n\
#        Successful transition.\n\
#\n\
#    - STATUS_FAILED_TRANS_UNKNOWN_BEHAVIOR\n\
#\n\
#        Failed to transition; unknown behavior.\n\
#\n\
#    - STATUS_FAILED_TRANS_ILLEGAL_BEHAVIOR\n\
#\n\
#        Denied request for an illegal behavior transition.  This may\n\
#        happen if a transition to a new behavior is requested without\n\
#        going through a required intermediate behavior. (e.g., can't\n\
#        go from Walk straight to Manipulate.)\n\
#\n\
#    - STATUS_FAILED_TRANS_COM_POS\n\
#\n\
#        Failed to transition; the position of the COM is too far from\n\
#        the center of support.\n\
#\n\
#    - STATUS_FAILED_TRANS_COM_VEL\n\
#\n\
#        Failed to transition; the COM velocity too high.\n\
#\n\
#    - STATUS_FAILED_TRANS_VEL\n\
#\n\
#        Failed to transition; some joint velocities too high.\n\
#\n\
#  \\em Warnings:\n\
#\n\
#    - STATUS_WARNING_AUTO_TRANS\n\
#\n\
#        An automatic transition occurred; see behavior specific\n\
#        feedback for reason.\n\
#\n\
#  \\em Errors:\n\
#\n\
#    - STATUS_ERROR_FALLING\n\
#\n\
#        COM below acceptable threshold, cannot recover.\n\
\n\
# copied from AtlasBehaviorFlags\n\
uint32 STATUS_OK                            = 0\n\
uint32 STATUS_TRANSITION_IN_PROGRESS        = 1\n\
uint32 STATUS_TRANSITION_SUCCESS            = 2\n\
uint32 STATUS_FAILED_TRANS_UNKNOWN_BEHAVIOR = 4\n\
uint32 STATUS_FAILED_TRANS_ILLEGAL_BEHAVIOR = 8\n\
uint32 STATUS_FAILED_TRANS_COM_POS          = 16\n\
uint32 STATUS_FAILED_TRANS_COM_VEL          = 32\n\
uint32 STATUS_FAILED_TRANS_VEL              = 64\n\
uint32 STATUS_WARNING_AUTO_TRANS            = 128\n\
uint32 STATUS_ERROR_FALLING                 = 256\n\
\n\
uint32 status_flags  # can be one of above\n\
\n\
int32 trans_from_behavior_index  # use this as a parm to get_behavior_at_index() to get behavior string\n\
int32 trans_to_behavior_index  # use this as a parm to get_behavior_at_index() to get behavior string\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasBehaviorStepFeedback\n\
# mirrored from AtlasControlTypes.h\n\
uint32 STEP_SUBSTATE_SWAYING = 0  # Feet are in double support. This flag does not latch. Only one of STEP_SUBSTATE_SWAYING or STEP_SUBSTATE_STEPPING will be set at any given time.\n\
uint32 STEP_SUBSTATE_STEPPING = 1 # Actively stepping; one foot is in the air. This flag does not latch.\n\
\n\
uint32 status_flags    # use AtlasBeahviorFeedback/status_flags\n\
float64 t_step_rem\n\
uint32 current_step_index\n\
uint32 next_step_index_needed\n\
atlas_msgs/AtlasBehaviorStepData desired_step_saturated\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasBehaviorStepData\n\
# multi_step walking trajectory parameters\n\
uint32 step_index              # Step index, matlab style, starting from 1,\n\
                               # monotonically increasing during walking\n\
                               #  resets to 1 if robot leaves walk behaviors\n\
uint32 foot_index              # Foot_index can be LEFT_FOOT or RIGHT_FOOT\n\
float64 duration               # Step duration, when in doubt, 0.63s is a\n\
                               # good guess.\n\
geometry_msgs/Pose pose        # Foot pose in Atlas world frame\n\
float64 swing_height           # Step apex swing height measured form the\n\
                               # midpoint between the feet.\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasBehaviorStandFeedback\n\
# mirrored from AtlasControlTypes.h\n\
uint32 status_flags    # use AtlasBeahviorStandFlags\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasBehaviorWalkFeedback\n\
# mirrored from AtlasControlTypes.h\n\
float64 t_step_rem\n\
uint32 current_step_index\n\
uint32 next_step_index_needed\n\
uint32 status_flags    # use AtlasBeahviorFeedback/status_flags\n\
atlas_msgs/AtlasBehaviorStepData[4] step_queue_saturated # 4 is hardcoded in AtlasSimInterface library.\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasBehaviorManipulateFeedback\n\
# mirrored from AtlasControlTypes.h\n\
uint32 status_flags    # use AtlasBeahviorManipulateFlags\n\
atlas_msgs/AtlasBehaviorPelvisServoParams clamped\n\
\n\
================================================================================\n\
MSG: atlas_msgs/AtlasBehaviorPelvisServoParams\n\
# mirrored from AtlasControlTypes.h\n\
\n\
float64 pelvis_height\n\
float64 pelvis_yaw\n\
float64 pelvis_lat\n\
\n\
";
  }

  static const char* value(const  ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.status);
    stream.next(m.result);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct WalkDemoActionResult_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::atlas_msgs::WalkDemoActionResult_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "status: ";
s << std::endl;
    Printer< ::actionlib_msgs::GoalStatus_<ContainerAllocator> >::stream(s, indent + "  ", v.status);
    s << indent << "result: ";
s << std::endl;
    Printer< ::atlas_msgs::WalkDemoResult_<ContainerAllocator> >::stream(s, indent + "  ", v.result);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ATLAS_MSGS_MESSAGE_WALKDEMOACTIONRESULT_H

