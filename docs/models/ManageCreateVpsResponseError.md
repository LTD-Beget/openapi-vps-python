# beget_openapi_vps.model.manage_create_vps_response_error.ManageCreateVpsResponseError

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**code** | str,  | str,  |  | [optional] must be one of ["INTERNAL_ERROR", "INVALID_DISPLAY_NAME", "INVALID_HOSTNAME", "INVALID_PARAMS", "INSUFFICIENT_FUNDS", "SERVICE_DISABLED", "INVALID_SECURITY_CONFIGURATION", "INVALID_PASSWORD", "TEMPORARILY_UNAVAILABLE", "SOFTWARE_INVALID_TYPE", "SOFTWARE_NOT_ENOUGH_RESOURCES", "SOFTWARE_VARIABLE_REQUIRED", "SOFTWARE_VARIABLE_INVALID", "SNAPSHOT_NOT_DONE", "SNAPSHOT_NOT_ENOUGH_CONFIGURATION", "INVALID_PRIVATE_NETWORK_CONFIGURATION", "INVALID_ADDRESS", "ADDRESS_SUBNET_MISMATCH", "ADDRESS_ALREADY_RESERVED", "ADDRESS_UNAVAILABLE", "BLACKLISTED_PASSWORD", ] 
**message** | str,  | str,  |  | [optional] 
**variable_error** | [**ManageCreateVpsResponseErrorSoftwareVariableError**](ManageCreateVpsResponseErrorSoftwareVariableError.md) | [**ManageCreateVpsResponseErrorSoftwareVariableError**](ManageCreateVpsResponseErrorSoftwareVariableError.md) |  | [optional] 
**insufficient_funds_error** | [**ManageCreateVpsResponseErrorInsufficientFundsError**](ManageCreateVpsResponseErrorInsufficientFundsError.md) | [**ManageCreateVpsResponseErrorInsufficientFundsError**](ManageCreateVpsResponseErrorInsufficientFundsError.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

