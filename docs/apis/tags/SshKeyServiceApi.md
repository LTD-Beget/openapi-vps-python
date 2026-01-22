<a id="__pageTop"></a>
# beget_openapi_vps.apis.tags.ssh_key_service_api.SshKeyServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssh_key_service_add**](#ssh_key_service_add) | **post** /v1/vps/sshKey | 
[**ssh_key_service_get_all**](#ssh_key_service_get_all) | **get** /v1/vps/sshKey | 
[**ssh_key_service_remove**](#ssh_key_service_remove) | **delete** /v1/vps/sshKey/{id} | 
[**ssh_key_service_update**](#ssh_key_service_update) | **put** /v1/vps/sshKey/{id} | 

# **ssh_key_service_add**
<a id="ssh_key_service_add"></a>
> SshKeyAddResponse ssh_key_service_add(ssh_key_add_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import ssh_key_service_api
from beget_openapi_vps.model.ssh_key_add_response import SshKeyAddResponse
from beget_openapi_vps.model.ssh_key_add_request import SshKeyAddRequest
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
    api_instance = ssh_key_service_api.SshKeyServiceApi(api_client)

    # example passing only required values which don't have defaults set
    body = SshKeyAddRequest(
        name="name_example",
        public_key="public_key_example",
    )
    try:
        api_response = api_instance.ssh_key_service_add(
            body=body,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_add: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SshKeyAddRequest**](../../models/SshKeyAddRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ssh_key_service_add.ApiResponseFor200) | OK

#### ssh_key_service_add.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SshKeyAddResponse**](../../models/SshKeyAddResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **ssh_key_service_get_all**
<a id="ssh_key_service_get_all"></a>
> SshKeyGetAllResponse ssh_key_service_get_all()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import ssh_key_service_api
from beget_openapi_vps.model.ssh_key_get_all_response import SshKeyGetAllResponse
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
    api_instance = ssh_key_service_api.SshKeyServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.ssh_key_service_get_all()
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_get_all: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ssh_key_service_get_all.ApiResponseFor200) | OK

#### ssh_key_service_get_all.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SshKeyGetAllResponse**](../../models/SshKeyGetAllResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **ssh_key_service_remove**
<a id="ssh_key_service_remove"></a>
> SshKeyRemoveResponse ssh_key_service_remove(id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import ssh_key_service_api
from beget_openapi_vps.model.ssh_key_remove_response import SshKeyRemoveResponse
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
    api_instance = ssh_key_service_api.SshKeyServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        api_response = api_instance.ssh_key_service_remove(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_remove: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    query_params = {
        'force': True,
    }
    try:
        api_response = api_instance.ssh_key_service_remove(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_remove: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
force | ForceSchema | | optional


# ForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ssh_key_service_remove.ApiResponseFor200) | OK

#### ssh_key_service_remove.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SshKeyRemoveResponse**](../../models/SshKeyRemoveResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **ssh_key_service_update**
<a id="ssh_key_service_update"></a>
> SshKeyUpdateResponse ssh_key_service_update(idssh_key_update_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import ssh_key_service_api
from beget_openapi_vps.model.ssh_key_update_request import SshKeyUpdateRequest
from beget_openapi_vps.model.ssh_key_update_response import SshKeyUpdateResponse
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
    api_instance = ssh_key_service_api.SshKeyServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = SshKeyUpdateRequest(
        id=1,
        name="name_example",
    )
    try:
        api_response = api_instance.ssh_key_service_update(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling SshKeyServiceApi->ssh_key_service_update: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SshKeyUpdateRequest**](../../models/SshKeyUpdateRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#ssh_key_service_update.ApiResponseFor200) | OK

#### ssh_key_service_update.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SshKeyUpdateResponse**](../../models/SshKeyUpdateResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

