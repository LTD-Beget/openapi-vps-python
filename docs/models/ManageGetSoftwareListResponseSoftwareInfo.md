# beget_openapi_vps.model.manage_get_software_list_response_software_info.ManageGetSoftwareListResponseSoftwareInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**display_name** | str,  | str,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["PANEL", "SOFTWARE", ] 
**description** | str,  | str,  |  | [optional] 
**description_version** | str,  | str,  |  | [optional] 
**[image_id](#image_id)** | list, tuple,  | tuple,  |  | [optional] 
**[variable](#variable)** | list, tuple,  | tuple,  |  | [optional] 
**requirements** | [**ManageGetSoftwareListResponseSoftwareInfoRequirements**](ManageGetSoftwareListResponseSoftwareInfoRequirements.md) | [**ManageGetSoftwareListResponseSoftwareInfoRequirements**](ManageGetSoftwareListResponseSoftwareInfoRequirements.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# image_id

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# variable

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
