<a id="__pageTop"></a>
# beget_openapi_vps.apis.tags.marketplace_service_api.MarketplaceServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketplace_service_get_software_info**](#marketplace_service_get_software_info) | **get** /v1/vps/marketplace/software/{name}/{version} | 
[**marketplace_service_get_software_list**](#marketplace_service_get_software_list) | **get** /v1/vps/marketplace/software/list | 

# **marketplace_service_get_software_info**
<a id="marketplace_service_get_software_info"></a>
> MarketplaceGetSoftwareInfoResponse marketplace_service_get_software_info(nameversion)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import marketplace_service_api
from beget_openapi_vps.model.marketplace_get_software_info_response import MarketplaceGetSoftwareInfoResponse
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
    api_instance = marketplace_service_api.MarketplaceServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'version': "version_example",
    }
    try:
        api_response = api_instance.marketplace_service_get_software_info(
            path_params=path_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling MarketplaceServiceApi->marketplace_service_get_software_info: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
version | VersionSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#marketplace_service_get_software_info.ApiResponseFor200) | OK

#### marketplace_service_get_software_info.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MarketplaceGetSoftwareInfoResponse**](../../models/MarketplaceGetSoftwareInfoResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **marketplace_service_get_software_list**
<a id="marketplace_service_get_software_list"></a>
> MarketplaceGetSoftwareListResponse marketplace_service_get_software_list()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import marketplace_service_api
from beget_openapi_vps.model.marketplace_get_software_list_response import MarketplaceGetSoftwareListResponse
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
    api_instance = marketplace_service_api.MarketplaceServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'category_name': "category_name_example",
        'display_name': "display_name_example",
        'is_pinned': True,
    }
    try:
        api_response = api_instance.marketplace_service_get_software_list(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling MarketplaceServiceApi->marketplace_service_get_software_list: %s\n" % e)
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
category_name | CategoryNameSchema | | optional
display_name | DisplayNameSchema | | optional
is_pinned | IsPinnedSchema | | optional


# CategoryNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DisplayNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IsPinnedSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#marketplace_service_get_software_list.ApiResponseFor200) | OK

#### marketplace_service_get_software_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MarketplaceGetSoftwareListResponse**](../../models/MarketplaceGetSoftwareListResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

