# beget_openapi_vps.model.manage_vps_configuration.ManageVpsConfiguration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**cpu_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**disk_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**memory** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**price_day** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**price_month** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**available** | bool,  | BoolClass,  |  | [optional] 
**custom** | bool,  | BoolClass,  |  | [optional] 
**configurable** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

