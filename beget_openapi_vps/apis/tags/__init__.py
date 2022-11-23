# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from beget_openapi_vps.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BACKUP_SERVICE = "BackupService"
    MANAGE_SERVICE = "ManageService"
    MARKETPLACE_SERVICE = "MarketplaceService"
    NETWORK_SERVICE = "NetworkService"
    SNAPSHOT_SERVICE = "SnapshotService"
    SSH_KEY_SERVICE = "SshKeyService"
    STATISTIC_SERVICE = "StatisticService"
