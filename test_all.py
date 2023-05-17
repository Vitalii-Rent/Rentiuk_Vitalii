from api import DropboxAPIFactory
import pytest


def test_upload_file(request, file_path='test.txt'):
    token = request.config.getoption("--token")
    api = DropboxAPIFactory.create_api(token)
    api.upload_file(file_path)


def test_get_file_metadata(request, file_path='test.txt'):
    token = request.config.getoption("--token")
    api = DropboxAPIFactory.create_api(token)
    api.upload_file(file_path)


def test_delete_file(request, file_path='test.txt'):
    token = request.config.getoption("--token")
    api = DropboxAPIFactory.create_api(token)
    api.upload_file(file_path)
