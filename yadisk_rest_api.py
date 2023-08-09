import requests

class Yadisk():
  api_url = 'https://cloud-api.yandex.net'
  
  def __init__(self, token):
    self.token = token

  def create_dir(self, dir_path):
    api_route = '/v1/disk/resources'
    api_req_url = self.api_url + api_route
    api_req_headers = {'Authorization': self.token}
    api_req_params = {'path': dir_path}

    api_resp = requests.put(
      url=api_req_url,
      headers=api_req_headers,
      params=api_req_params
    )
    
    return api_resp
  
  def delete_file(self, dir_path):
    api_route = '/v1/disk/resources'
    api_req_url = self.api_url + api_route
    api_req_headers = {'Authorization': self.token}
    api_req_params = {'path': dir_path}

    api_resp = requests.delete(
      url=api_req_url,
      headers=api_req_headers,
      params=api_req_params
    )
    
    return api_resp

  def get_file_info(self, dir_path):
    api_route = '/v1/disk/resources'
    api_req_url = self.api_url + api_route
    api_req_headers = {'Authorization': self.token}
    api_req_params = {'path': dir_path}

    api_resp = requests.get(
      url=api_req_url,
      headers=api_req_headers,
      params=api_req_params
    )
    
    return api_resp 