/* Auto-generated by genmsg_cpp for file /home/patrick/catkin_ws/src/drcsim/ros/atlas_msgs/srv/GetJointDamping.srv */
#ifndef ATLAS_MSGS_SERVICE_GETJOINTDAMPING_H
#define ATLAS_MSGS_SERVICE_GETJOINTDAMPING_H
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
struct GetJointDampingRequest_ {
  typedef GetJointDampingRequest_<ContainerAllocator> Type;

  GetJointDampingRequest_()
  {
  }

  GetJointDampingRequest_(const ContainerAllocator& _alloc)
  {
  }


  typedef boost::shared_ptr< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator>  const> ConstPtr;
}; // struct GetJointDampingRequest
typedef  ::atlas_msgs::GetJointDampingRequest_<std::allocator<void> > GetJointDampingRequest;

typedef boost::shared_ptr< ::atlas_msgs::GetJointDampingRequest> GetJointDampingRequestPtr;
typedef boost::shared_ptr< ::atlas_msgs::GetJointDampingRequest const> GetJointDampingRequestConstPtr;



template <class ContainerAllocator>
struct GetJointDampingResponse_ {
  typedef GetJointDampingResponse_<ContainerAllocator> Type;

  GetJointDampingResponse_()
  : damping_coefficients()
  , damping_coefficients_min()
  , damping_coefficients_max()
  , success(false)
  , status_message()
  {
    damping_coefficients.assign(0.0);
    damping_coefficients_min.assign(0.0);
    damping_coefficients_max.assign(0.0);
  }

  GetJointDampingResponse_(const ContainerAllocator& _alloc)
  : damping_coefficients()
  , damping_coefficients_min()
  , damping_coefficients_max()
  , success(false)
  , status_message(_alloc)
  {
    damping_coefficients.assign(0.0);
    damping_coefficients_min.assign(0.0);
    damping_coefficients_max.assign(0.0);
  }

  typedef boost::array<double, 28>  _damping_coefficients_type;
  boost::array<double, 28>  damping_coefficients;

  typedef boost::array<double, 28>  _damping_coefficients_min_type;
  boost::array<double, 28>  damping_coefficients_min;

  typedef boost::array<double, 28>  _damping_coefficients_max_type;
  boost::array<double, 28>  damping_coefficients_max;

  typedef uint8_t _success_type;
  uint8_t success;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _status_message_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  status_message;


  typedef boost::shared_ptr< ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator>  const> ConstPtr;
}; // struct GetJointDampingResponse
typedef  ::atlas_msgs::GetJointDampingResponse_<std::allocator<void> > GetJointDampingResponse;

typedef boost::shared_ptr< ::atlas_msgs::GetJointDampingResponse> GetJointDampingResponsePtr;
typedef boost::shared_ptr< ::atlas_msgs::GetJointDampingResponse const> GetJointDampingResponseConstPtr;


struct GetJointDamping
{

typedef GetJointDampingRequest Request;
typedef GetJointDampingResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct GetJointDamping
} // namespace atlas_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const  ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/GetJointDampingRequest";
  }

  static const char* value(const  ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
\n\
";
  }

  static const char* value(const  ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b90f38abe0cbace7d3c92e071b5dd30b";
  }

  static const char* value(const  ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb90f38abe0cbace7ULL;
  static const uint64_t static_value2 = 0xd3c92e071b5dd30bULL;
};

template<class ContainerAllocator>
struct DataType< ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/GetJointDampingResponse";
  }

  static const char* value(const  ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "\n\
float64[28] damping_coefficients\n\
float64[28] damping_coefficients_min\n\
float64[28] damping_coefficients_max\n\
bool success\n\
string status_message\n\
\n\
\n\
\n\
";
  }

  static const char* value(const  ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::atlas_msgs::GetJointDampingRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GetJointDampingRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::atlas_msgs::GetJointDampingResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.damping_coefficients);
    stream.next(m.damping_coefficients_min);
    stream.next(m.damping_coefficients_max);
    stream.next(m.success);
    stream.next(m.status_message);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct GetJointDampingResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<atlas_msgs::GetJointDamping> {
  static const char* value() 
  {
    return "b90f38abe0cbace7d3c92e071b5dd30b";
  }

  static const char* value(const atlas_msgs::GetJointDamping&) { return value(); } 
};

template<>
struct DataType<atlas_msgs::GetJointDamping> {
  static const char* value() 
  {
    return "atlas_msgs/GetJointDamping";
  }

  static const char* value(const atlas_msgs::GetJointDamping&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<atlas_msgs::GetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b90f38abe0cbace7d3c92e071b5dd30b";
  }

  static const char* value(const atlas_msgs::GetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<atlas_msgs::GetJointDampingRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/GetJointDamping";
  }

  static const char* value(const atlas_msgs::GetJointDampingRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<atlas_msgs::GetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b90f38abe0cbace7d3c92e071b5dd30b";
  }

  static const char* value(const atlas_msgs::GetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<atlas_msgs::GetJointDampingResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "atlas_msgs/GetJointDamping";
  }

  static const char* value(const atlas_msgs::GetJointDampingResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // ATLAS_MSGS_SERVICE_GETJOINTDAMPING_H

