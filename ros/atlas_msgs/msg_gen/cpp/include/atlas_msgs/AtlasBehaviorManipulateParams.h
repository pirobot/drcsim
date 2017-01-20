/* Auto-generated by genmsg_cpp for file /home/patrick/catkin_ws/src/drcsim/ros/atlas_msgs/msg/AtlasBehaviorManipulateParams.msg */
#ifndef ATLAS_MSGS_MESSAGE_ATLASBEHAVIORMANIPULATEPARAMS_H
#define ATLAS_MSGS_MESSAGE_ATLASBEHAVIORMANIPULATEPARAMS_H
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

#include "atlas_msgs/AtlasBehaviorPelvisServoParams.h"

namespace atlas_msgs
{
template <class ContainerAllocator>
struct AtlasBehaviorManipulateParams_ {
  typedef AtlasBehaviorManipulateParams_<ContainerAllocator> Type;

  AtlasBehaviorManipulateParams_()
  : use_desired(false)
  , desired()
  , use_demo_mode(false)
  {
  }

  AtlasBehaviorManipulateParams_(const ContainerAllocator& _alloc)
  : use_desired(false)
  , desired(_alloc)
  , use_demo_mode(false)
  {
  }

  typedef uint8_t _use_desired_type;
  uint8_t use_desired;

  typedef  ::atlas_msgs::AtlasBehaviorPelvisServoParams_<ContainerAllocator>  _desired_type;
   ::atlas_msgs::AtlasBehaviorPelvisServoParams_<ContainerAllocator>  desired;

  typedef uint8_t _use_demo_mode_type;
  uint8_t use_demo_mode;


  typedef boost::shared_ptr< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator>  const> ConstPtr;
}; // struct AtlasBehaviorManipulateParams
typedef  ::atlas_msgs::AtlasBehaviorManipulateParams_<std::allocator<void> > AtlasBehaviorManipulateParams;

typedef boost::shared_ptr< ::atlas_msgs::AtlasBehaviorManipulateParams> AtlasBehaviorManipulateParamsPtr;
typedef boost::shared_ptr< ::atlas_msgs::AtlasBehaviorManipulateParams const> AtlasBehaviorManipulateParamsConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace atlas_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> > {
  static const char* value() 
  {
    return "c4e967ec87266f9e108243e7ac4b9614";
  }

  static const char* value(const  ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xc4e967ec87266f9eULL;
  static const uint64_t static_value2 = 0x108243e7ac4b9614ULL;
};

template<class ContainerAllocator>
struct DataType< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/AtlasBehaviorManipulateParams";
  }

  static const char* value(const  ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# mirrored from AtlasControlTypes.h\n\
bool use_desired\n\
atlas_msgs/AtlasBehaviorPelvisServoParams desired\n\
bool use_demo_mode\n\
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

  static const char* value(const  ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.use_desired);
    stream.next(m.desired);
    stream.next(m.use_demo_mode);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct AtlasBehaviorManipulateParams_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::atlas_msgs::AtlasBehaviorManipulateParams_<ContainerAllocator> & v) 
  {
    s << indent << "use_desired: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.use_desired);
    s << indent << "desired: ";
s << std::endl;
    Printer< ::atlas_msgs::AtlasBehaviorPelvisServoParams_<ContainerAllocator> >::stream(s, indent + "  ", v.desired);
    s << indent << "use_demo_mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.use_demo_mode);
  }
};


} // namespace message_operations
} // namespace ros

#endif // ATLAS_MSGS_MESSAGE_ATLASBEHAVIORMANIPULATEPARAMS_H
