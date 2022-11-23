import typing_extensions

from beget_openapi_vps.apis.tags import TagValues
from beget_openapi_vps.apis.tags.backup_service_api import BackupServiceApi
from beget_openapi_vps.apis.tags.manage_service_api import ManageServiceApi
from beget_openapi_vps.apis.tags.marketplace_service_api import MarketplaceServiceApi
from beget_openapi_vps.apis.tags.network_service_api import NetworkServiceApi
from beget_openapi_vps.apis.tags.snapshot_service_api import SnapshotServiceApi
from beget_openapi_vps.apis.tags.ssh_key_service_api import SshKeyServiceApi
from beget_openapi_vps.apis.tags.statistic_service_api import StatisticServiceApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BACKUP_SERVICE: BackupServiceApi,
        TagValues.MANAGE_SERVICE: ManageServiceApi,
        TagValues.MARKETPLACE_SERVICE: MarketplaceServiceApi,
        TagValues.NETWORK_SERVICE: NetworkServiceApi,
        TagValues.SNAPSHOT_SERVICE: SnapshotServiceApi,
        TagValues.SSH_KEY_SERVICE: SshKeyServiceApi,
        TagValues.STATISTIC_SERVICE: StatisticServiceApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BACKUP_SERVICE: BackupServiceApi,
        TagValues.MANAGE_SERVICE: ManageServiceApi,
        TagValues.MARKETPLACE_SERVICE: MarketplaceServiceApi,
        TagValues.NETWORK_SERVICE: NetworkServiceApi,
        TagValues.SNAPSHOT_SERVICE: SnapshotServiceApi,
        TagValues.SSH_KEY_SERVICE: SshKeyServiceApi,
        TagValues.STATISTIC_SERVICE: StatisticServiceApi,
    }
)
