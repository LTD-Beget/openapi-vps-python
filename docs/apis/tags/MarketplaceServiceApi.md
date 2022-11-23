<a name="__pageTop"></a>
# beget_openapi_vps.apis.tags.marketplace_service_api.MarketplaceServiceApi

All URIs are relative to *https://api.beget.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketplace_service_get_software_list**](#marketplace_service_get_software_list) | **get** /v1/vps/marketplace/software/list | 

# **marketplace_service_get_software_list**
<a name="marketplace_service_get_software_list"></a>
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

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.marketplace_service_get_software_list()
        pprint(api_response)
    except beget_openapi_vps.ApiException as e:
        print("Exception when calling MarketplaceServiceApi->marketplace_service_get_software_list: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

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

