# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import beget_openapi_vps
from beget_openapi_vps.paths.v1_vps_software_license_vps_id import patch  # noqa: E501
from beget_openapi_vps import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1VpsSoftwareLicenseVpsId(ApiTestMixin, unittest.TestCase):
    """
    V1VpsSoftwareLicenseVpsId unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()