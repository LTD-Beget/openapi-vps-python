<a id="__pageTop"></a>
# beget_openapi_vps.apis.tags.backup_service_api.BackupServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_service_get_available_copies**](#backup_service_get_available_copies) | **get** /v1/vps/backup | 
[**backup_service_get_backup_file_list**](#backup_service_get_backup_file_list) | **get** /v1/vps/{id}/backup/{copy_id} | 
[**backup_service_get_orders**](#backup_service_get_orders) | **get** /v1/vps/backup/orders | 
[**backup_service_restore_file**](#backup_service_restore_file) | **post** /v1/vps/{id}/backup/{copy_id}/file | 
[**backup_service_restore_server**](#backup_service_restore_server) | **post** /v1/vps/{id}/backup/{copy_id}/server | 

# **backup_service_get_available_copies**
<a id="backup_service_get_available_copies"></a>
> BackupGetAvailableCopiesResponse backup_service_get_available_copies()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import backup_service_api
from beget_openapi_vps.model.backup_get_available_copies_response import BackupGetAvailableCopiesResponse
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
    api_instance = backup_service_api.BackupServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'filter': "filter_example",
    }
    try:
        api_response = api_instance.backup_service_get_available_copies(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_available_copies: %s\n" % e)
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
filter | FilterSchema | | optional


# FilterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#backup_service_get_available_copies.ApiResponseFor200) | OK

#### backup_service_get_available_copies.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BackupGetAvailableCopiesResponse**](../../models/BackupGetAvailableCopiesResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **backup_service_get_backup_file_list**
<a id="backup_service_get_backup_file_list"></a>
> BackupGetBackupFileListResponse backup_service_get_backup_file_list(idcopy_id)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import backup_service_api
from beget_openapi_vps.model.backup_get_backup_file_list_response import BackupGetBackupFileListResponse
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
    api_instance = backup_service_api.BackupServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'copy_id': "copy_id_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.backup_service_get_backup_file_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_backup_file_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': "id_example",
        'copy_id': "copy_id_example",
    }
    query_params = {
        'path': "path_example",
    }
    try:
        api_response = api_instance.backup_service_get_backup_file_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_backup_file_list: %s\n" % e)
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
path | PathSchema | | optional


# PathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
copy_id | CopyIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CopyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#backup_service_get_backup_file_list.ApiResponseFor200) | OK

#### backup_service_get_backup_file_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BackupGetBackupFileListResponse**](../../models/BackupGetBackupFileListResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **backup_service_get_orders**
<a id="backup_service_get_orders"></a>
> BackupGetOrdersResponse backup_service_get_orders()



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import backup_service_api
from beget_openapi_vps.model.backup_get_orders_response import BackupGetOrdersResponse
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
    api_instance = backup_service_api.BackupServiceApi(api_client)

    # example passing only optional values
    query_params = {
        'limit': 1,
        'offset': 1,
    }
    try:
        api_response = api_instance.backup_service_get_orders(
            query_params=query_params,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_get_orders: %s\n" % e)
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
limit | LimitSchema | | optional
offset | OffsetSchema | | optional


# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OffsetSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#backup_service_get_orders.ApiResponseFor200) | OK

#### backup_service_get_orders.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BackupGetOrdersResponse**](../../models/BackupGetOrdersResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **backup_service_restore_file**
<a id="backup_service_restore_file"></a>
> BackupRestoreFileResponse backup_service_restore_file(idcopy_idbackup_restore_file_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import backup_service_api
from beget_openapi_vps.model.backup_restore_file_response import BackupRestoreFileResponse
from beget_openapi_vps.model.backup_restore_file_request import BackupRestoreFileRequest
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
    api_instance = backup_service_api.BackupServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'copy_id': "copy_id_example",
    }
    body = BackupRestoreFileRequest(
        id="id_example",
        copy_id="copy_id_example",
        path=[
            "path_example"
        ],
        affect_live=True,
        target="target_example",
    )
    try:
        api_response = api_instance.backup_service_restore_file(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_restore_file: %s\n" % e)
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
[**BackupRestoreFileRequest**](../../models/BackupRestoreFileRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
copy_id | CopyIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CopyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#backup_service_restore_file.ApiResponseFor200) | OK

#### backup_service_restore_file.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BackupRestoreFileResponse**](../../models/BackupRestoreFileResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **backup_service_restore_server**
<a id="backup_service_restore_server"></a>
> BackupRestoreServerResponse backup_service_restore_server(idcopy_idbackup_restore_server_request)



### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import beget_openapi_vps
from beget_openapi_vps.apis.tags import backup_service_api
from beget_openapi_vps.model.backup_restore_server_response import BackupRestoreServerResponse
from beget_openapi_vps.model.backup_restore_server_request import BackupRestoreServerRequest
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
    api_instance = backup_service_api.BackupServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': "id_example",
        'copy_id': "copy_id_example",
    }
    body = BackupRestoreServerRequest(
        id="id_example",
        copy_id="copy_id_example",
    )
    try:
        api_response = api_instance.backup_service_restore_server(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling BackupServiceApi->backup_service_restore_server: %s\n" % e)
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
[**BackupRestoreServerRequest**](../../models/BackupRestoreServerRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 
copy_id | CopyIdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CopyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#backup_service_restore_server.ApiResponseFor200) | OK

#### backup_service_restore_server.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BackupRestoreServerResponse**](../../models/BackupRestoreServerResponse.md) |  | 


### Authorization

[bearerAuth](../../../README.md#bearerAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

