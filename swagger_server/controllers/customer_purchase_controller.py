import connexion
import six
import os
from logging import log, ERROR

from flask import request, app, abort
from werkzeug.utils import secure_filename

from services.tab_delim_parser_service import TabDelimParserService
from repositories.purchase_repository import PurchaseRepository
from repositories.customer_repository import CustomerRepository
from repositories.product_repository import ProductRepository

from swagger_server.models.upload_response import UploadResponse  # noqa: E501


def uploadcustomerpurchasefile(upfile=None):  # noqa: E501
    """Upload a datafile to the database

     # noqa: E501

    :param upfile: The file to upload.
    :type upfile: werkzeug.datastructures.FileStorage

    :rtype: UploadResponse
    """
    # get the file from the request
    file = _save_file(req=request)
    if not file:
        abort(400, 'No file included with request')

    # parse it
    parser = TabDelimParserService()
    repository = PurchaseRepository(CustomerRepository(), ProductRepository())
    errors = 0
    num_parsed = 0
    for purchase in parser.parse_file(file):
        if purchase:
            # store it
            try:
                repository.create(purchase)
                num_parsed += 1
            except Exception as e:
                log(ERROR, 'Error storing result', e)
                errors += 1
        else:
            errors += 1

    # create response
    return UploadResponse(number_of_rows_stored=num_parsed, number_of_error_rows=errors)


def _save_file(req):
    file = req.files['upfile']
    if file:
        filename = secure_filename(file.filename)
        datafolder = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..', 'data')
        destfile = os.path.join(datafolder, filename)
        file.save(destfile)

    return destfile

