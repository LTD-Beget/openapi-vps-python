# beget_openapi_vps.model.manage_vps_info.ManageVpsInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**slug** | str,  | str,  |  | [optional] 
**display_name** | str,  | str,  |  | [optional] 
**hostname** | str,  | str,  |  | [optional] 
**configuration** | [**ManageVpsConfiguration**](ManageVpsConfiguration.md) | [**ManageVpsConfiguration**](ManageVpsConfiguration.md) |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["UNKNOWN", "CREATING", "RUNNING", "STOPPING", "RESTARTING", "REMOVING", "REMOVED", "STOPPED", "STARTING", "RECONFIGURING", "REINSTALLING", ] 
**[ssh_keys](#ssh_keys)** | list, tuple,  | tuple,  |  | [optional] 
**has_password** | bool,  | BoolClass,  |  | [optional] 
**manage_enabled** | bool,  | BoolClass,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**date_create** | str,  | str,  |  | [optional] 
**ip_address** | str,  | str,  |  | [optional] 
**rescue_mode** | bool,  | BoolClass,  |  | [optional] 
**migrating** | bool,  | BoolClass,  |  | [optional] 
**host_unavailable** | bool,  | BoolClass,  |  | [optional] 
**unblocking** | bool,  | BoolClass,  |  | [optional] 
**restoring** | bool,  | BoolClass,  |  | [optional] 
**disk_used** | str,  | str,  |  | [optional] 
**disk_left** | str,  | str,  |  | [optional] 
**[additional_ip_address](#additional_ip_address)** | list, tuple,  | tuple,  |  | [optional] 
**beget_ssh_access_allowed** | bool,  | BoolClass,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**unarchiving** | bool,  | BoolClass,  |  | [optional] 
**[private_network](#private_network)** | list, tuple,  | tuple,  |  | [optional] 
**technical_domain** | str,  | str,  |  | [optional] 
**software_domain** | str,  | str,  |  | [optional] 
**software** | [**StructuresInstalledSoftwareInfo**](StructuresInstalledSoftwareInfo.md) | [**StructuresInstalledSoftwareInfo**](StructuresInstalledSoftwareInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ssh_keys

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**StructuresSshKeyInfo**](StructuresSshKeyInfo.md) | [**StructuresSshKeyInfo**](StructuresSshKeyInfo.md) | [**StructuresSshKeyInfo**](StructuresSshKeyInfo.md) |  | 

# additional_ip_address

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# private_network

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**StructuresAttachedPrivateNetwork**](StructuresAttachedPrivateNetwork.md) | [**StructuresAttachedPrivateNetwork**](StructuresAttachedPrivateNetwork.md) | [**StructuresAttachedPrivateNetwork**](StructuresAttachedPrivateNetwork.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

