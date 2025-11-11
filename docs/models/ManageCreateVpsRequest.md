# beget_openapi_vps.model.manage_create_vps_request.ManageCreateVpsRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**display_name** | str,  | str,  |  | [optional] 
**hostname** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**configuration_id** | str,  | str,  |  | [optional] 
**configuration_params** | [**StructuresConfigurationParams**](StructuresConfigurationParams.md) | [**StructuresConfigurationParams**](StructuresConfigurationParams.md) |  | [optional] 
**software** | [**ManageSoftwareInstallInfo**](ManageSoftwareInstallInfo.md) | [**ManageSoftwareInstallInfo**](ManageSoftwareInstallInfo.md) |  | [optional] 
**snapshot_id** | str,  | str,  |  | [optional] 
**image_id** | str,  | str,  |  | [optional] 
**[ssh_keys](#ssh_keys)** | list, tuple,  | tuple,  |  | [optional] 
**password** | str,  | str,  |  | [optional] 
**beget_ssh_access_allowed** | bool,  | BoolClass,  |  | [optional] 
**[private_networks](#private_networks)** | list, tuple,  | tuple,  |  | [optional] 
**link_slug** | str,  | str,  |  | [optional] 
**license_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**region** | str,  | str,  |  | [optional] 
**configuration_group** | str,  | str,  |  | [optional] 
**ui_pinned** | bool,  | BoolClass,  |  | [optional] 
**project_id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssh_keys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# private_networks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ManagePrivateNetworkInfo**](ManagePrivateNetworkInfo.md) | [**ManagePrivateNetworkInfo**](ManagePrivateNetworkInfo.md) | [**ManagePrivateNetworkInfo**](ManagePrivateNetworkInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

