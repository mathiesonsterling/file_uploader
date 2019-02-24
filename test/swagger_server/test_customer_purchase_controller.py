# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO
import os

from swagger_server.models.upload_response import UploadResponse  # noqa: E501
from test.swagger_server import BaseTestCase


class TestCustomerPurchaseController(BaseTestCase):
    """CustomerPurchaseController integration test stubs"""

    def test_uploadcustomerpurchasefile(self):
        """Test case for uploadcustomerpurchasefile

        Upload a datafile to the database
        """
        testfile = os.path.join(os.getcwd(), '..', 'test_input_file.dat')
        in_file = open(testfile, 'rb')
        filec = in_file.read()
        in_file.close()
        data = dict(upfile=(BytesIO(filec), testfile))
        response = self.client.open(
            '/v1/customerpurchases/upload',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
