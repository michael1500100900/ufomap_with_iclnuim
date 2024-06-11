// Generated by gencpp from file ufomap_srvs/GetMap.msg
// DO NOT EDIT!


#ifndef UFOMAP_SRVS_MESSAGE_GETMAP_H
#define UFOMAP_SRVS_MESSAGE_GETMAP_H

#include <ros/service_traits.h>


#include <ufomap_srvs/GetMapRequest.h>
#include <ufomap_srvs/GetMapResponse.h>


namespace ufomap_srvs
{

struct GetMap
{

typedef GetMapRequest Request;
typedef GetMapResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct GetMap
} // namespace ufomap_srvs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ufomap_srvs::GetMap > {
  static const char* value()
  {
    return "47cd0cd4e998ca314e6ccaf9f3b259df";
  }

  static const char* value(const ::ufomap_srvs::GetMap&) { return value(); }
};

template<>
struct DataType< ::ufomap_srvs::GetMap > {
  static const char* value()
  {
    return "ufomap_srvs/GetMap";
  }

  static const char* value(const ::ufomap_srvs::GetMap&) { return value(); }
};


// service_traits::MD5Sum< ::ufomap_srvs::GetMapRequest> should match
// service_traits::MD5Sum< ::ufomap_srvs::GetMap >
template<>
struct MD5Sum< ::ufomap_srvs::GetMapRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ufomap_srvs::GetMap >::value();
  }
  static const char* value(const ::ufomap_srvs::GetMapRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ufomap_srvs::GetMapRequest> should match
// service_traits::DataType< ::ufomap_srvs::GetMap >
template<>
struct DataType< ::ufomap_srvs::GetMapRequest>
{
  static const char* value()
  {
    return DataType< ::ufomap_srvs::GetMap >::value();
  }
  static const char* value(const ::ufomap_srvs::GetMapRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ufomap_srvs::GetMapResponse> should match
// service_traits::MD5Sum< ::ufomap_srvs::GetMap >
template<>
struct MD5Sum< ::ufomap_srvs::GetMapResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ufomap_srvs::GetMap >::value();
  }
  static const char* value(const ::ufomap_srvs::GetMapResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ufomap_srvs::GetMapResponse> should match
// service_traits::DataType< ::ufomap_srvs::GetMap >
template<>
struct DataType< ::ufomap_srvs::GetMapResponse>
{
  static const char* value()
  {
    return DataType< ::ufomap_srvs::GetMap >::value();
  }
  static const char* value(const ::ufomap_srvs::GetMapResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // UFOMAP_SRVS_MESSAGE_GETMAP_H