/* Auto-generated by genmsg_cpp for file /home/patrick/catkin_ws/src/drcsim/ros/atlas_msgs/srv/SetJointDamping.srv */
#ifndef ATLAS_MSGS_SERVICE_SETJOINTDAMPING_H
#define ATLAS_MSGS_SERVICE_SETJOINTDAMPING_H
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

#include "ros/service_traits.h"




namespace atlas_msgs
{
template <class ContainerAllocator>
struct SetJointDampingRequest_ {
  typedef SetJointDampingRequest_<ContainerAllocator> Type;

  SetJointDampingRequest_()
  : damping_coefficients()
  {
    damping_coefficients.assign(0.0);
  }

  SetJointDampingRequest_(const ContainerAllocator& _alloc)
  : damping_coefficients()
  {
    damping_coefficients.assign(0.0);
  }

  typedef boost::array<double, 28>  _damping_coefficients_type;
  boost::array<double, 28>  damping_coefficients;


  typedef boost::shared_ptr< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator>  const> ConstPtr;
}; // struct SetJointDampingRequest
typedef  ::atlas_msgs::SetJointDampingRequest_<std::allocator<void> > SetJointDampingRequest;

typedef boost::shared_ptr< ::atlas_msgs::SetJointDampingRequest> SetJointDampingRequestPtr;
typedef boost::shared_ptr< ::atlas_msgs::SetJointDampingRequest const> SetJointDampingRequestConstPtr;



template <class ContainerAllocator>
struct SetJointDampingResponse_ {
  typedef SetJointDampingResponse_<ContainerAllocator> Type;

  SetJointDampingResponse_()
  : success(false)
  , status_message()
  {
  }

  SetJointDampingResponse_(const ContainerAllocator& _alloc)
  : success(false)
  , status_message(_alloc)
  {
  }

  typedef uint8_t _success_type;
  uint8_t success;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _status_message_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  status_message;


  typedef boost::shared_ptr< ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator>  const> ConstPtr;
}; // struct SetJointDampingResponse
typedef  ::atlas_msgs::SetJointDampingResponse_<std::allocator<void> > SetJointDampingResponse;

typedef boost::shared_ptr< ::atlas_msgs::SetJointDampingResponse> SetJointDampingResponsePtr;
typedef boost::shared_ptr< ::atlas_msgs::SetJointDampingResponse const> SetJointDampingResponseConstPtr;


struct SetJointDamping
{

typedef SetJointDampingRequest Request;
typedef SetJointDampingResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct SetJointDamping
} // namespace atlas_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "77f911c1c7f4135acec183d52f402a58";
  }

  static const char* value(const  ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x77f911c1c7f4135aULL;
  static const uint64_t static_value2 = 0xcec183d52f402a58ULL;
};

template<class ContainerAllocator>
struct DataType< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/SetJointDampingRequest";
  }

  static const char* value(const  ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
\n\
float64[28] damping_coefficients\n\
\n\
\n\
";
  }

  static const char* value(const  ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2ec6f3eff0161f4257b808b12bc830c2";
  }

  static const char* value(const  ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x2ec6f3eff0161f42ULL;
  static const uint64_t static_value2 = 0x57b808b12bc830c2ULL;
};

template<class ContainerAllocator>
struct DataType< ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/SetJointDampingResponse";
  }

  static const char* value(const  ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool success\n\
string status_message\n\
\n\
\n\
\n\
";
  }

  static const char* value(const  ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::atlas_msgs::SetJointDampingRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.damping_coefficients);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SetJointDampingRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::atlas_msgs::SetJointDampingResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.success);
    stream.next(m.status_message);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct SetJointDampingResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<atlas_msgs::SetJointDamping> {
  static const char* value() 
  {
    return "b3bf624354d6cc6f87700ca4a9eaeae1";
  }

  static const char* value(const atlas_msgs::SetJointDamping&) { return value(); } 
};

template<>
struct DataType<atlas_msgs::SetJointDamping> {
  static const char* value() 
  {
    return "atlas_msgs/SetJointDamping";
  }

  static const char* value(const atlas_msgs::SetJointDamping&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<atlas_msgs::SetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b3bf624354d6cc6f87700ca4a9eaeae1";
  }

  static const char* value(const atlas_msgs::SetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<atlas_msgs::SetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/SetJointDamping";
  }

  static const char* value(const atlas_msgs::SetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<atlas_msgs::SetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b3bf624354d6cc6f87700ca4a9eaeae1";
  }

  static const char* value(const atlas_msgs::SetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<atlas_msgs::SetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/SetJointDamping";
  }

  static const char* value(const atlas_msgs::SetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // ATLAS_MSGS_SERVICE_SETJOINTDAMPING_H
