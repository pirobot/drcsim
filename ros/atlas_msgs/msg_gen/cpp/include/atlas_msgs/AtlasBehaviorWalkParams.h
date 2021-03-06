/* Auto-generated by genmsg_cpp for file /home/patrick/catkin_ws/src/drcsim/ros/atlas_msgs/msg/AtlasBehaviorWalkParams.msg */
#ifndef ATLAS_MSGS_MESSAGE_ATLASBEHAVIORWALKPARAMS_H
#define ATLAS_MSGS_MESSAGE_ATLASBEHAVIORWALKPARAMS_H
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

#include "atlas_msgs/AtlasBehaviorStepData.h"

namespace atlas_msgs
{
template <class ContainerAllocator>
struct AtlasBehaviorWalkParams_ {
  typedef AtlasBehaviorWalkParams_<ContainerAllocator> Type;

  AtlasBehaviorWalkParams_()
  : step_queue()
  , use_demo_walk(false)
  {
  }

  AtlasBehaviorWalkParams_(const ContainerAllocator& _alloc)
  : step_queue()
  , use_demo_walk(false)
  {
    step_queue.assign( ::atlas_msgs::AtlasBehaviorStepData_<ContainerAllocator> (_alloc));
  }

  typedef boost::array< ::atlas_msgs::AtlasBehaviorStepData_<ContainerAllocator> , 4>  _step_queue_type;
  boost::array< ::atlas_msgs::AtlasBehaviorStepData_<ContainerAllocator> , 4>  step_queue;

  typedef uint8_t _use_demo_walk_type;
  uint8_t use_demo_walk;


  typedef boost::shared_ptr< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator>  const> ConstPtr;
}; // struct AtlasBehaviorWalkParams
typedef  ::atlas_msgs::AtlasBehaviorWalkParams_<std::allocator<void> > AtlasBehaviorWalkParams;

typedef boost::shared_ptr< ::atlas_msgs::AtlasBehaviorWalkParams> AtlasBehaviorWalkParamsPtr;
typedef boost::shared_ptr< ::atlas_msgs::AtlasBehaviorWalkParams const> AtlasBehaviorWalkParamsConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace atlas_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> > {
  static const char* value() 
  {
    return "0a5b4bccbb6f87ef4f591430c3499c4f";
  }

  static const char* value(const  ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x0a5b4bccbb6f87efULL;
  static const uint64_t static_value2 = 0x4f591430c3499c4fULL;
};

template<class ContainerAllocator>
struct DataType< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/AtlasBehaviorWalkParams";
  }

  static const char* value(const  ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# multi_step walking trajectory parameters\n\
atlas_msgs/AtlasBehaviorStepData[4] step_queue\n\
bool use_demo_walk\n\
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
";
  }

  static const char* value(const  ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.step_queue);
    stream.next(m.use_demo_walk);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct AtlasBehaviorWalkParams_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::atlas_msgs::AtlasBehaviorWalkParams_<ContainerAllocator> & v) 
  {
    s << indent << "step_queue[]" << std::endl;
    for (size_t i = 0; i < v.step_queue.size(); ++i)
    {
      s << indent << "  step_queue[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::atlas_msgs::AtlasBehaviorStepData_<ContainerAllocator> >::stream(s, indent + "    ", v.step_queue[i]);
    }
    s << indent << "use_demo_walk: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.use_demo_walk);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ATLAS_MSGS_MESSAGE_ATLASBEHAVIORWALKPARAMS_H

