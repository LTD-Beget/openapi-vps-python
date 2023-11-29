import typing_extensions

from beget_openapi_vps.paths import PathValues
from beget_openapi_vps.apis.paths.v1_vps_archive_id import V1VpsArchiveId
from beget_openapi_vps.apis.paths.v1_vps_backup import V1VpsBackup
from beget_openapi_vps.apis.paths.v1_vps_backup_orders import V1VpsBackupOrders
from beget_openapi_vps.apis.paths.v1_vps_configuration import V1VpsConfiguration
from beget_openapi_vps.apis.paths.v1_vps_configurator_calculation import V1VpsConfiguratorCalculation
from beget_openapi_vps.apis.paths.v1_vps_configurator_info import V1VpsConfiguratorInfo
from beget_openapi_vps.apis.paths.v1_vps_marketplace_software_list import V1VpsMarketplaceSoftwareList
from beget_openapi_vps.apis.paths.v1_vps_marketplace_software_name_version import V1VpsMarketplaceSoftwareNameVersion
from beget_openapi_vps.apis.paths.v1_vps_network import V1VpsNetwork
from beget_openapi_vps.apis.paths.v1_vps_network_detach_ip_address import V1VpsNetworkDetachIpAddress
from beget_openapi_vps.apis.paths.v1_vps_network_ip_address import V1VpsNetworkIpAddress
from beget_openapi_vps.apis.paths.v1_vps_private_network import V1VpsPrivateNetwork
from beget_openapi_vps.apis.paths.v1_vps_private_network_network_id_suggested_address import V1VpsPrivateNetworkNetworkIdSuggestedAddress
from beget_openapi_vps.apis.paths.v1_vps_region import V1VpsRegion
from beget_openapi_vps.apis.paths.v1_vps_server import V1VpsServer
from beget_openapi_vps.apis.paths.v1_vps_server_list import V1VpsServerList
from beget_openapi_vps.apis.paths.v1_vps_server_statuses import V1VpsServerStatuses
from beget_openapi_vps.apis.paths.v1_vps_server_id import V1VpsServerId
from beget_openapi_vps.apis.paths.v1_vps_server_id_configuration import V1VpsServerIdConfiguration
from beget_openapi_vps.apis.paths.v1_vps_server_id_info import V1VpsServerIdInfo
from beget_openapi_vps.apis.paths.v1_vps_server_id_reboot import V1VpsServerIdReboot
from beget_openapi_vps.apis.paths.v1_vps_server_id_reinstall import V1VpsServerIdReinstall
from beget_openapi_vps.apis.paths.v1_vps_server_id_remove import V1VpsServerIdRemove
from beget_openapi_vps.apis.paths.v1_vps_server_id_rescue import V1VpsServerIdRescue
from beget_openapi_vps.apis.paths.v1_vps_server_id_reset import V1VpsServerIdReset
from beget_openapi_vps.apis.paths.v1_vps_server_id_start import V1VpsServerIdStart
from beget_openapi_vps.apis.paths.v1_vps_server_id_stop import V1VpsServerIdStop
from beget_openapi_vps.apis.paths.v1_vps_snapshot import V1VpsSnapshot
from beget_openapi_vps.apis.paths.v1_vps_snapshot_calculator import V1VpsSnapshotCalculator
from beget_openapi_vps.apis.paths.v1_vps_snapshot_restore import V1VpsSnapshotRestore
from beget_openapi_vps.apis.paths.v1_vps_snapshot_id import V1VpsSnapshotId
from beget_openapi_vps.apis.paths.v1_vps_snapshot_id_restore import V1VpsSnapshotIdRestore
from beget_openapi_vps.apis.paths.v1_vps_software_license import V1VpsSoftwareLicense
from beget_openapi_vps.apis.paths.v1_vps_software_license_vps_id import V1VpsSoftwareLicenseVpsId
from beget_openapi_vps.apis.paths.v1_vps_software_requirements import V1VpsSoftwareRequirements
from beget_openapi_vps.apis.paths.v1_vps_ssh_key import V1VpsSshKey
from beget_openapi_vps.apis.paths.v1_vps_ssh_key_id import V1VpsSshKeyId
from beget_openapi_vps.apis.paths.v1_vps_statistic_cpu_details_id import V1VpsStatisticCpuDetailsId
from beget_openapi_vps.apis.paths.v1_vps_statistic_cpu_id import V1VpsStatisticCpuId
from beget_openapi_vps.apis.paths.v1_vps_statistic_disk_usage_id import V1VpsStatisticDiskUsageId
from beget_openapi_vps.apis.paths.v1_vps_statistic_disk_id import V1VpsStatisticDiskId
from beget_openapi_vps.apis.paths.v1_vps_statistic_load_average_id import V1VpsStatisticLoadAverageId
from beget_openapi_vps.apis.paths.v1_vps_statistic_memory_id import V1VpsStatisticMemoryId
from beget_openapi_vps.apis.paths.v1_vps_statistic_network_id import V1VpsStatisticNetworkId
from beget_openapi_vps.apis.paths.v1_vps_statistic_processes_id import V1VpsStatisticProcessesId
from beget_openapi_vps.apis.paths.v1_vps_subdomain_reserve import V1VpsSubdomainReserve
from beget_openapi_vps.apis.paths.v1_vps_id_backup_copy_id import V1VpsIdBackupCopyId
from beget_openapi_vps.apis.paths.v1_vps_id_backup_copy_id_file import V1VpsIdBackupCopyIdFile
from beget_openapi_vps.apis.paths.v1_vps_id_backup_copy_id_server import V1VpsIdBackupCopyIdServer
from beget_openapi_vps.apis.paths.v1_vps_id_fm import V1VpsIdFm
from beget_openapi_vps.apis.paths.v1_vps_id_history import V1VpsIdHistory
from beget_openapi_vps.apis.paths.v1_vps_id_network_ip_address import V1VpsIdNetworkIpAddress
from beget_openapi_vps.apis.paths.v1_vps_id_password import V1VpsIdPassword
from beget_openapi_vps.apis.paths.v1_vps_id_private_network_network_id import V1VpsIdPrivateNetworkNetworkId
from beget_openapi_vps.apis.paths.v1_vps_id_software import V1VpsIdSoftware
from beget_openapi_vps.apis.paths.v1_vps_id_software_post_install_alert import V1VpsIdSoftwarePostInstallAlert
from beget_openapi_vps.apis.paths.v1_vps_id_ssh_access import V1VpsIdSshAccess
from beget_openapi_vps.apis.paths.v1_vps_id_ssh_key_ssh_key_id import V1VpsIdSshKeySshKeyId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_VPS_ARCHIVE_ID: V1VpsArchiveId,
        PathValues.V1_VPS_BACKUP: V1VpsBackup,
        PathValues.V1_VPS_BACKUP_ORDERS: V1VpsBackupOrders,
        PathValues.V1_VPS_CONFIGURATION: V1VpsConfiguration,
        PathValues.V1_VPS_CONFIGURATOR_CALCULATION: V1VpsConfiguratorCalculation,
        PathValues.V1_VPS_CONFIGURATOR_INFO: V1VpsConfiguratorInfo,
        PathValues.V1_VPS_MARKETPLACE_SOFTWARE_LIST: V1VpsMarketplaceSoftwareList,
        PathValues.V1_VPS_MARKETPLACE_SOFTWARE_NAME_VERSION: V1VpsMarketplaceSoftwareNameVersion,
        PathValues.V1_VPS_NETWORK: V1VpsNetwork,
        PathValues.V1_VPS_NETWORK_DETACH_IP_ADDRESS: V1VpsNetworkDetachIpAddress,
        PathValues.V1_VPS_NETWORK_IP_ADDRESS: V1VpsNetworkIpAddress,
        PathValues.V1_VPS_PRIVATENETWORK: V1VpsPrivateNetwork,
        PathValues.V1_VPS_PRIVATENETWORK_NETWORK_ID_SUGGESTEDADDRESS: V1VpsPrivateNetworkNetworkIdSuggestedAddress,
        PathValues.V1_VPS_REGION: V1VpsRegion,
        PathValues.V1_VPS_SERVER: V1VpsServer,
        PathValues.V1_VPS_SERVER_LIST: V1VpsServerList,
        PathValues.V1_VPS_SERVER_STATUSES: V1VpsServerStatuses,
        PathValues.V1_VPS_SERVER_ID: V1VpsServerId,
        PathValues.V1_VPS_SERVER_ID_CONFIGURATION: V1VpsServerIdConfiguration,
        PathValues.V1_VPS_SERVER_ID_INFO: V1VpsServerIdInfo,
        PathValues.V1_VPS_SERVER_ID_REBOOT: V1VpsServerIdReboot,
        PathValues.V1_VPS_SERVER_ID_REINSTALL: V1VpsServerIdReinstall,
        PathValues.V1_VPS_SERVER_ID_REMOVE: V1VpsServerIdRemove,
        PathValues.V1_VPS_SERVER_ID_RESCUE: V1VpsServerIdRescue,
        PathValues.V1_VPS_SERVER_ID_RESET: V1VpsServerIdReset,
        PathValues.V1_VPS_SERVER_ID_START: V1VpsServerIdStart,
        PathValues.V1_VPS_SERVER_ID_STOP: V1VpsServerIdStop,
        PathValues.V1_VPS_SNAPSHOT: V1VpsSnapshot,
        PathValues.V1_VPS_SNAPSHOT_CALCULATOR: V1VpsSnapshotCalculator,
        PathValues.V1_VPS_SNAPSHOT_RESTORE: V1VpsSnapshotRestore,
        PathValues.V1_VPS_SNAPSHOT_ID: V1VpsSnapshotId,
        PathValues.V1_VPS_SNAPSHOT_ID_RESTORE: V1VpsSnapshotIdRestore,
        PathValues.V1_VPS_SOFTWARE_LICENSE: V1VpsSoftwareLicense,
        PathValues.V1_VPS_SOFTWARE_LICENSE_VPS_ID: V1VpsSoftwareLicenseVpsId,
        PathValues.V1_VPS_SOFTWARE_REQUIREMENTS: V1VpsSoftwareRequirements,
        PathValues.V1_VPS_SSH_KEY: V1VpsSshKey,
        PathValues.V1_VPS_SSH_KEY_ID: V1VpsSshKeyId,
        PathValues.V1_VPS_STATISTIC_CPUDETAILS_ID: V1VpsStatisticCpuDetailsId,
        PathValues.V1_VPS_STATISTIC_CPU_ID: V1VpsStatisticCpuId,
        PathValues.V1_VPS_STATISTIC_DISKUSAGE_ID: V1VpsStatisticDiskUsageId,
        PathValues.V1_VPS_STATISTIC_DISK_ID: V1VpsStatisticDiskId,
        PathValues.V1_VPS_STATISTIC_LOADAVERAGE_ID: V1VpsStatisticLoadAverageId,
        PathValues.V1_VPS_STATISTIC_MEMORY_ID: V1VpsStatisticMemoryId,
        PathValues.V1_VPS_STATISTIC_NETWORK_ID: V1VpsStatisticNetworkId,
        PathValues.V1_VPS_STATISTIC_PROCESSES_ID: V1VpsStatisticProcessesId,
        PathValues.V1_VPS_SUBDOMAIN_RESERVE: V1VpsSubdomainReserve,
        PathValues.V1_VPS_ID_BACKUP_COPY_ID: V1VpsIdBackupCopyId,
        PathValues.V1_VPS_ID_BACKUP_COPY_ID_FILE: V1VpsIdBackupCopyIdFile,
        PathValues.V1_VPS_ID_BACKUP_COPY_ID_SERVER: V1VpsIdBackupCopyIdServer,
        PathValues.V1_VPS_ID_FM: V1VpsIdFm,
        PathValues.V1_VPS_ID_HISTORY: V1VpsIdHistory,
        PathValues.V1_VPS_ID_NETWORK_IP_ADDRESS: V1VpsIdNetworkIpAddress,
        PathValues.V1_VPS_ID_PASSWORD: V1VpsIdPassword,
        PathValues.V1_VPS_ID_PRIVATENETWORK_NETWORK_ID: V1VpsIdPrivateNetworkNetworkId,
        PathValues.V1_VPS_ID_SOFTWARE: V1VpsIdSoftware,
        PathValues.V1_VPS_ID_SOFTWARE_POSTINSTALLALERT: V1VpsIdSoftwarePostInstallAlert,
        PathValues.V1_VPS_ID_SSH_ACCESS: V1VpsIdSshAccess,
        PathValues.V1_VPS_ID_SSH_KEY_SSH_KEY_ID: V1VpsIdSshKeySshKeyId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_VPS_ARCHIVE_ID: V1VpsArchiveId,
        PathValues.V1_VPS_BACKUP: V1VpsBackup,
        PathValues.V1_VPS_BACKUP_ORDERS: V1VpsBackupOrders,
        PathValues.V1_VPS_CONFIGURATION: V1VpsConfiguration,
        PathValues.V1_VPS_CONFIGURATOR_CALCULATION: V1VpsConfiguratorCalculation,
        PathValues.V1_VPS_CONFIGURATOR_INFO: V1VpsConfiguratorInfo,
        PathValues.V1_VPS_MARKETPLACE_SOFTWARE_LIST: V1VpsMarketplaceSoftwareList,
        PathValues.V1_VPS_MARKETPLACE_SOFTWARE_NAME_VERSION: V1VpsMarketplaceSoftwareNameVersion,
        PathValues.V1_VPS_NETWORK: V1VpsNetwork,
        PathValues.V1_VPS_NETWORK_DETACH_IP_ADDRESS: V1VpsNetworkDetachIpAddress,
        PathValues.V1_VPS_NETWORK_IP_ADDRESS: V1VpsNetworkIpAddress,
        PathValues.V1_VPS_PRIVATENETWORK: V1VpsPrivateNetwork,
        PathValues.V1_VPS_PRIVATENETWORK_NETWORK_ID_SUGGESTEDADDRESS: V1VpsPrivateNetworkNetworkIdSuggestedAddress,
        PathValues.V1_VPS_REGION: V1VpsRegion,
        PathValues.V1_VPS_SERVER: V1VpsServer,
        PathValues.V1_VPS_SERVER_LIST: V1VpsServerList,
        PathValues.V1_VPS_SERVER_STATUSES: V1VpsServerStatuses,
        PathValues.V1_VPS_SERVER_ID: V1VpsServerId,
        PathValues.V1_VPS_SERVER_ID_CONFIGURATION: V1VpsServerIdConfiguration,
        PathValues.V1_VPS_SERVER_ID_INFO: V1VpsServerIdInfo,
        PathValues.V1_VPS_SERVER_ID_REBOOT: V1VpsServerIdReboot,
        PathValues.V1_VPS_SERVER_ID_REINSTALL: V1VpsServerIdReinstall,
        PathValues.V1_VPS_SERVER_ID_REMOVE: V1VpsServerIdRemove,
        PathValues.V1_VPS_SERVER_ID_RESCUE: V1VpsServerIdRescue,
        PathValues.V1_VPS_SERVER_ID_RESET: V1VpsServerIdReset,
        PathValues.V1_VPS_SERVER_ID_START: V1VpsServerIdStart,
        PathValues.V1_VPS_SERVER_ID_STOP: V1VpsServerIdStop,
        PathValues.V1_VPS_SNAPSHOT: V1VpsSnapshot,
        PathValues.V1_VPS_SNAPSHOT_CALCULATOR: V1VpsSnapshotCalculator,
        PathValues.V1_VPS_SNAPSHOT_RESTORE: V1VpsSnapshotRestore,
        PathValues.V1_VPS_SNAPSHOT_ID: V1VpsSnapshotId,
        PathValues.V1_VPS_SNAPSHOT_ID_RESTORE: V1VpsSnapshotIdRestore,
        PathValues.V1_VPS_SOFTWARE_LICENSE: V1VpsSoftwareLicense,
        PathValues.V1_VPS_SOFTWARE_LICENSE_VPS_ID: V1VpsSoftwareLicenseVpsId,
        PathValues.V1_VPS_SOFTWARE_REQUIREMENTS: V1VpsSoftwareRequirements,
        PathValues.V1_VPS_SSH_KEY: V1VpsSshKey,
        PathValues.V1_VPS_SSH_KEY_ID: V1VpsSshKeyId,
        PathValues.V1_VPS_STATISTIC_CPUDETAILS_ID: V1VpsStatisticCpuDetailsId,
        PathValues.V1_VPS_STATISTIC_CPU_ID: V1VpsStatisticCpuId,
        PathValues.V1_VPS_STATISTIC_DISKUSAGE_ID: V1VpsStatisticDiskUsageId,
        PathValues.V1_VPS_STATISTIC_DISK_ID: V1VpsStatisticDiskId,
        PathValues.V1_VPS_STATISTIC_LOADAVERAGE_ID: V1VpsStatisticLoadAverageId,
        PathValues.V1_VPS_STATISTIC_MEMORY_ID: V1VpsStatisticMemoryId,
        PathValues.V1_VPS_STATISTIC_NETWORK_ID: V1VpsStatisticNetworkId,
        PathValues.V1_VPS_STATISTIC_PROCESSES_ID: V1VpsStatisticProcessesId,
        PathValues.V1_VPS_SUBDOMAIN_RESERVE: V1VpsSubdomainReserve,
        PathValues.V1_VPS_ID_BACKUP_COPY_ID: V1VpsIdBackupCopyId,
        PathValues.V1_VPS_ID_BACKUP_COPY_ID_FILE: V1VpsIdBackupCopyIdFile,
        PathValues.V1_VPS_ID_BACKUP_COPY_ID_SERVER: V1VpsIdBackupCopyIdServer,
        PathValues.V1_VPS_ID_FM: V1VpsIdFm,
        PathValues.V1_VPS_ID_HISTORY: V1VpsIdHistory,
        PathValues.V1_VPS_ID_NETWORK_IP_ADDRESS: V1VpsIdNetworkIpAddress,
        PathValues.V1_VPS_ID_PASSWORD: V1VpsIdPassword,
        PathValues.V1_VPS_ID_PRIVATENETWORK_NETWORK_ID: V1VpsIdPrivateNetworkNetworkId,
        PathValues.V1_VPS_ID_SOFTWARE: V1VpsIdSoftware,
        PathValues.V1_VPS_ID_SOFTWARE_POSTINSTALLALERT: V1VpsIdSoftwarePostInstallAlert,
        PathValues.V1_VPS_ID_SSH_ACCESS: V1VpsIdSshAccess,
        PathValues.V1_VPS_ID_SSH_KEY_SSH_KEY_ID: V1VpsIdSshKeySshKeyId,
    }
)
