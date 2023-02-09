# coding: utf-8

"""
    API Облачных серверов

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.4.0
    Generated by: https://openapi-generator.tech
"""

from beget_openapi_vps.paths.v1_vps_snapshot.post import SnapshotServiceCreate
from beget_openapi_vps.paths.v1_vps_snapshot_calculator.post import SnapshotServiceCreateCalculator
from beget_openapi_vps.paths.v1_vps_snapshot_id.put import SnapshotServiceEdit
from beget_openapi_vps.paths.v1_vps_snapshot.get import SnapshotServiceGetAll
from beget_openapi_vps.paths.v1_vps_snapshot_restore.get import SnapshotServiceGetAllRestores
from beget_openapi_vps.paths.v1_vps_snapshot_id.delete import SnapshotServiceRemove
from beget_openapi_vps.paths.v1_vps_snapshot_id_restore.post import SnapshotServiceRestore


class SnapshotServiceApi(
    SnapshotServiceCreate,
    SnapshotServiceCreateCalculator,
    SnapshotServiceEdit,
    SnapshotServiceGetAll,
    SnapshotServiceGetAllRestores,
    SnapshotServiceRemove,
    SnapshotServiceRestore,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
