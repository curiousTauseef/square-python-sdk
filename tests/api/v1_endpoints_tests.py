# -*- coding: utf-8 -*-

import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.v1_locations_api import V1LocationsApi


class V1EndpointsTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(V1EndpointsTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = V1LocationsApi(cls.config, cls.response_catcher)

    # You can only test V1 endpoint with production access token. 
    # Uncomment this section if you choose to do so.

    # def test_v1_endpoints_journey(self):
    #     # delete
    #     response = self.controller.list_locations()
    #     self.assertIsInstance(response.body, list)
    #     self.assertEquals(response.status_code, 200)


