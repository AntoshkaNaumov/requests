import requests
import os.path

class YaUploader:
    host = 'https://cloud-api.yandex.net:443'
    
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        } 

    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        return response.json().get('href')

    def upload(self, path, file_path):
        upload_link = self._get_upload_link(path)
        headers = self.get_headers()
        file_path1 = os.path.normpath(file_path)
        response = requests.put(upload_link, data=open(file_path1, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            return print('Файл успешно загружен на Яндекс Диск')
        return print('Ошибка загрузки')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'C:/Users/79633/Downloads/niterous.jpg'
    token = 'AQAAAABdbechAADLW4BNTXojlkv-phVVWMRdpww'
    yadisk = YaUploader(token)
    yadisk.upload('/niterous.jpg', path_to_file)
