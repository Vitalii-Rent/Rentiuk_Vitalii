import requests
import pytest


class DropboxAPIFactory:
    @staticmethod
    def create_api(access_token):
        return DropboxAPI(access_token)


class DropboxAPI:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_path):
        api_url = 'https://content.dropboxapi.com/2/files/upload'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/octet-stream',
            'Dropbox-API-Arg': f'{{"path": "/{file_path}"}}'
        }

        with open(file_path, 'rb') as file:
            response = requests.post(api_url, headers=headers, data=file)

        assert response.status_code == 200, f'File upload failed. Status code: {response.status_code}'

    def get_file_metadata(self, file_path):
        api_url = 'https://api.dropboxapi.com/2/files/get_metadata'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'path': f'/{file_path}',
            'include_media_info': False,
            'include_deleted': False,
            'include_has_explicit_shared_members': False
        }

        response = requests.post(api_url, headers=headers, json=data)
        assert response.status_code == 200, f'Get file metadata failed. Status code: {response.status_code}'

        metadata = response.json()
        return metadata

    def delete_file(self, file_path):
        api_url = 'https://api.dropboxapi.com/2/files/delete_v2'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'path': f'/{file_path}'
        }

        response = requests.post(api_url, headers=headers, json=data)
        assert response.status_code == 200, f'Delete file failed. Status code: {response.status_code}'



