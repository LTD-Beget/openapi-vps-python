<a id="__pageTop"></a>
# beget_openapi_vps.apis.tags.configurator_service_api.ConfiguratorServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurator_service_get_calculation**](#configurator_service_get_calculation) | **get** /v1/vps/configurator/calculation | 
[**configurator_service_get_configurator_info**](#configurator_service_get_configurator_info) | **get** /v1/vps/configurator/info | 

# **configurator_service_get_calculation**
<a id="configurator_service_get_calculation"></a>
> ConfiguratorGetCalculationResponse configurator_service_get_calculation()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import configurator_service_api
from beget_openapi_vps.model.configurator_get_calculation_response import ConfiguratorGetCalculationResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurator_service_api.ConfiguratorServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'params.cpu_count': 1,
        'params.disk_size': 1,
        'params.memory': 1,
        'region': "region_example",
        'vps_id': "vps_id_example",
        'software_id': 1,
        'snapshot_id': "snapshot_id_example",
        'image_id': "image_id_example",
        'configuration_group': "configuration_group_example",
    }
    try:
        api_response = api_instance.configurator_service_get_calculation(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling ConfiguratorServiceApi->configurator_service_get_calculation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
params.cpu_count | ParamsCpuCountSchema | | optional
params.disk_size | ParamsDiskSizeSchema | | optional
params.memory | ParamsMemorySchema | | optional
region | RegionSchema | | optional
vps_id | VpsIdSchema | | optional
software_id | SoftwareIdSchema | | optional
snapshot_id | SnapshotIdSchema | | optional
image_id | ImageIdSchema | | optional
configuration_group | ConfigurationGroupSchema | | optional


# ParamsCpuCountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ParamsDiskSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ParamsMemorySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VpsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SoftwareIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# SnapshotIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ImageIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConfigurationGroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#configurator_service_get_calculation.ApiResponseFor200) | OK

#### configurator_service_get_calculation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfiguratorGetCalculationResponse**](../../models/ConfiguratorGetCalculationResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **configurator_service_get_configurator_info**
<a id="configurator_service_get_configurator_info"></a>
> ConfiguratorGetConfiguratorInfoResponse configurator_service_get_configurator_info()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import configurator_service_api
from beget_openapi_vps.model.configurator_get_configurator_info_response import ConfiguratorGetConfiguratorInfoResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.beget.com
# See configuration.py for a list of all supported configuration parameters.
configuration = beget_openapi_vps.Configuration(
    host = "https://api.beget.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = beget_openapi_vps.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with beget_openapi_vps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configurator_service_api.ConfiguratorServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'region': "region_example",
        'configuration_group': "configuration_group_example",
    }
    try:
        api_response = api_instance.configurator_service_get_configurator_info(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling ConfiguratorServiceApi->configurator_service_get_configurator_info: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
region | RegionSchema | | optional
configuration_group | ConfigurationGroupSchema | | optional


# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ConfigurationGroupSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#configurator_service_get_configurator_info.ApiResponseFor200) | OK

#### configurator_service_get_configurator_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConfiguratorGetConfiguratorInfoResponse**](../../models/ConfiguratorGetConfiguratorInfoResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

