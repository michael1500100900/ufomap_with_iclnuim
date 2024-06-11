// Generated by gencpp from file ufomap_srvs/Reset.msg
// DO NOT EDIT!


#ifndef UFOMAP_SRVS_MESSAGE_RESET_H
#define UFOMAP_SRVS_MESSAGE_RESET_H

#include <ros/service_traits.h>


#include <ufomap_srvs/ResetRequest.h>
#include <ufomap_srvs/ResetResponse.h>


namespace ufomap_srvs
{

struct Reset
{

typedef ResetRequest Request;
typedef ResetResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Reset
} // namespace ufomap_srvs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ufomap_srvs::Reset > {
  static const char* value()
  {
    return "98aeec308656a857be8d59d1fb3f81a9";
  }

  static const char* value(const ::ufomap_srvs::Reset&) { return value(); }
};

template<>
struct DataType< ::ufomap_srvs::Reset > {
  static const char* value()
  {
    return "ufomap_srvs/Reset";
  }

  static const char* value(const ::ufomap_srvs::Reset&) { return value(); }
};


// service_traits::MD5Sum< ::ufomap_srvs::ResetRequest> should match
// service_traits::MD5Sum< ::ufomap_srvs::Reset >
template<>
struct MD5Sum< ::ufomap_srvs::ResetRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ufomap_srvs::Reset >::value();
  }
  static const char* value(const ::ufomap_srvs::ResetRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ufomap_srvs::ResetRequest> should match
// service_traits::DataType< ::ufomap_srvs::Reset >
template<>
struct DataType< ::ufomap_srvs::ResetRequest>
{
  static const char* value()
  {
    return DataType< ::ufomap_srvs::Reset >::value();
  }
  static const char* value(const ::ufomap_srvs::ResetRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ufomap_srvs::ResetResponse> should match
// service_traits::MD5Sum< ::ufomap_srvs::Reset >
template<>
struct MD5Sum< ::ufomap_srvs::ResetResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ufomap_srvs::Reset >::value();
  }
  static const char* value(const ::ufomap_srvs::ResetResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ufomap_srvs::ResetResponse> should match
// service_traits::DataType< ::ufomap_srvs::Reset >
template<>
struct DataType< ::ufomap_srvs::ResetResponse>
{
  static const char* value()
  {
    return DataType< ::ufomap_srvs::Reset >::value();
  }
  static const char* value(const ::ufomap_srvs::ResetResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // UFOMAP_SRVS_MESSAGE_RESET_H
