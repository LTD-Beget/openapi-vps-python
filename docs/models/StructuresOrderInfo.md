# beget_openapi_vps.model.structures_order_info.StructuresOrderInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**items** | str,  | str,  |  | [optional] 
**vps_name** | str,  | str,  |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["DOWNLOAD", "RESTORE", ] 
**date_create** | str,  | str,  |  | [optional] 
**date_complete** | str,  | str,  |  | [optional] 
**[path](#path)** | list, tuple,  | tuple,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["PROCESSING", "COMPLETED", "ERROR", "COMPLETED_PARTIALLY", ] 
**copy_info** | [**StructuresCopyInfo**](StructuresCopyInfo.md) | [**StructuresCopyInfo**](StructuresCopyInfo.md) |  | [optional] 
**affect_live** | bool,  | BoolClass,  |  | [optional] 
**target** | str,  | str,  |  | [optional] 
**error_details** | [**StructuresOrderInfoErrorDetails**](StructuresOrderInfoErrorDetails.md) | [**StructuresOrderInfoErrorDetails**](StructuresOrderInfoErrorDetails.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# path

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

