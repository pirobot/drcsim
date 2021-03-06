/* Auto-generated by genmsg_cpp for file /home/patrick/catkin_ws/src/drcsim/ros/atlas_msgs/msg/Test.msg */
#ifndef ATLAS_MSGS_MESSAGE_TEST_H
#define ATLAS_MSGS_MESSAGE_TEST_H
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

namespace atlas_msgs
{
template <class ContainerAllocator>
struct Test_ {
  typedef Test_<ContainerAllocator> Type;

  Test_()
  : header()
  , damping()
  , kp_position()
  , ki_position()
  , kd_position()
  , kp_velocity()
  , i_effort_min()
  , i_effort_max()
  , k_effort()
  {
  }

  Test_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , damping(_alloc)
  , kp_position(_alloc)
  , ki_position(_alloc)
  , kd_position(_alloc)
  , kp_velocity(_alloc)
  , i_effort_min(_alloc)
  , i_effort_max(_alloc)
  , k_effort(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _damping_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  damping;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _kp_position_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  kp_position;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _ki_position_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  ki_position;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _kd_position_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  kd_position;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _kp_velocity_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  kp_velocity;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _i_effort_min_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  i_effort_min;

  typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _i_effort_max_type;
  std::vector<float, typename ContainerAllocator::template rebind<float>::other >  i_effort_max;

  typedef std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  _k_effort_type;
  std::vector<uint8_t, typename ContainerAllocator::template rebind<uint8_t>::other >  k_effort;


  typedef boost::shared_ptr< ::atlas_msgs::Test_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::atlas_msgs::Test_<ContainerAllocator>  const> ConstPtr;
}; // struct Test
typedef  ::atlas_msgs::Test_<std::allocator<void> > Test;

typedef boost::shared_ptr< ::atlas_msgs::Test> TestPtr;
typedef boost::shared_ptr< ::atlas_msgs::Test const> TestConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::atlas_msgs::Test_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::atlas_msgs::Test_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace atlas_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::Test_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::Test_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::atlas_msgs::Test_<ContainerAllocator> > {
  static const char* value() 
  {
    return "62f63cd4b6db15007d8d3d4a23411c4c";
  }

  static const char* value(const  ::atlas_msgs::Test_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x62f63cd4b6db1500ULL;
  static const uint64_t static_value2 = 0x7d8d3d4a23411c4cULL;
};

template<class ContainerAllocator>
struct DataType< ::atlas_msgs::Test_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/Test";
  }

  static const char* value(const  ::atlas_msgs::Test_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::atlas_msgs::Test_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# test Message\n\
# Do not use, testing only\n\
Header header\n\
\n\
float32[] damping\n\
float32[] kp_position\n\
float32[] ki_position\n\
float32[] kd_position\n\
float32[] kp_velocity\n\
float32[] i_effort_min\n\
float32[] i_effort_max\n\
uint8[] k_effort\n\
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
";
  }

  static const char* value(const  ::atlas_msgs::Test_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::atlas_msgs::Test_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::atlas_msgs::Test_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::atlas_msgs::Test_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.damping);
    stream.next(m.kp_position);
    stream.next(m.ki_position);
    stream.next(m.kd_position);
    stream.next(m.kp_velocity);
    stream.next(m.i_effort_min);
    stream.next(m.i_effort_max);
    stream.next(m.k_effort);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct Test_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::atlas_msgs::Test_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::atlas_msgs::Test_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "damping[]" << std::endl;
    for (size_t i = 0; i < v.damping.size(); ++i)
    {
      s << indent << "  damping[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.damping[i]);
    }
    s << indent << "kp_position[]" << std::endl;
    for (size_t i = 0; i < v.kp_position.size(); ++i)
    {
      s << indent << "  kp_position[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.kp_position[i]);
    }
    s << indent << "ki_position[]" << std::endl;
    for (size_t i = 0; i < v.ki_position.size(); ++i)
    {
      s << indent << "  ki_position[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.ki_position[i]);
    }
    s << indent << "kd_position[]" << std::endl;
    for (size_t i = 0; i < v.kd_position.size(); ++i)
    {
      s << indent << "  kd_position[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.kd_position[i]);
    }
    s << indent << "kp_velocity[]" << std::endl;
    for (size_t i = 0; i < v.kp_velocity.size(); ++i)
    {
      s << indent << "  kp_velocity[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.kp_velocity[i]);
    }
    s << indent << "i_effort_min[]" << std::endl;
    for (size_t i = 0; i < v.i_effort_min.size(); ++i)
    {
      s << indent << "  i_effort_min[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.i_effort_min[i]);
    }
    s << indent << "i_effort_max[]" << std::endl;
    for (size_t i = 0; i < v.i_effort_max.size(); ++i)
    {
      s << indent << "  i_effort_max[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.i_effort_max[i]);
    }
    s << indent << "k_effort[]" << std::endl;
    for (size_t i = 0; i < v.k_effort.size(); ++i)
    {
      s << indent << "  k_effort[" << i << "]: ";
      Printer<uint8_t>::stream(s, indent + "  ", v.k_effort[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // ATLAS_MSGS_MESSAGE_TEST_H

