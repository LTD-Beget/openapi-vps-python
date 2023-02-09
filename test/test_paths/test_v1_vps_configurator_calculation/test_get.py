# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import beget_openapi_vps
from beget_openapi_vps.paths.v1_vps_configurator_calculation import get  # noqa: E501
from beget_openapi_vps import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1VpsConfiguratorCalculation(ApiTestMixin, unittest.TestCase):
    """
    V1VpsConfiguratorCalculation unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
