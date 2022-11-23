# beget_openapi_vps.model.manage_get_statuses_response_status_info.ManageGetStatusesResponseStatusInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**status** | str,  | str,  |  | [optional] must be one of ["UNKNOWN", "CREATING", "RUNNING", "STOPPING", "RESTARTING", "REMOVING", "REMOVED", "STOPPED", "STARTING", "RECONFIGURING", "REINSTALLING", ] 
**rescue_mode** | bool,  | BoolClass,  |  | [optional] 
**migrating** | bool,  | BoolClass,  |  | [optional] 
**manage_enabled** | bool,  | BoolClass,  |  | [optional] 
**restoring** | bool,  | BoolClass,  |  | [optional] 
**archived** | bool,  | BoolClass,  |  | [optional] 
**unblocking** | bool,  | BoolClass,  |  | [optional] 
**unarchiving** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

