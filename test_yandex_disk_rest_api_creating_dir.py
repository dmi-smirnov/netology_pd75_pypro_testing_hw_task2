import pytest

from yadisk_rest_api import Yadisk
from yatoken import yatoken


class TestYadiskCreatingDir():
  @pytest.fixture(scope='class')
  def yadisk(self):
    return Yadisk(yatoken)
  
  @pytest.fixture(scope='class')
  def dir_path(self):
    return'/test_dir'
  
  @pytest.fixture
  def dir_not_exists(self, yadisk, dir_path):
    if yadisk.get_file_info(dir_path).status_code != 404:
      raise Exception(f'The directory {dir_path} already exists.')

  @pytest.fixture
  def dir_exists(self, yadisk, dir_path):
    file_info_resp = yadisk.get_file_info(dir_path)
    if file_info_resp.status_code == 200:
      return
    elif file_info_resp.status_code == 404:
      yadisk.create_dir(dir_path)
      if yadisk.get_file_info(dir_path).status_code == 200:
        return
    raise Exception(f'Failed to create directory.')

  @pytest.fixture
  def delete_dir_after(self, yadisk, dir_path):
    yield
    yadisk.delete_file(dir_path)

  def test_http_status_code_201(self, dir_not_exists, yadisk, dir_path,
    delete_dir_after):
    # HTTP status code must be 201
    assert yadisk.create_dir(dir_path).status_code == 201

  def test_dir_created(self, dir_not_exists, yadisk, dir_path,
    delete_dir_after):
    yadisk.create_dir(dir_path)
    file_info_resp = yadisk.get_file_info(dir_path)
    # HTTP status code must be 200
    assert file_info_resp.status_code == 200
    # File type must be 'dir'
    assert file_info_resp.json()['type'] == 'dir'

  def test_dir_already_exists(self, dir_exists, yadisk, dir_path,
    delete_dir_after):
    # HTTP status code must be 409
    assert yadisk.create_dir(dir_path).status_code == 409

  def test_unauthorized(self, dir_not_exists, dir_path):
    # HTTP status code must be 401
    assert Yadisk('abc').create_dir(dir_path).status_code == 401