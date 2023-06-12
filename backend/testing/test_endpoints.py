import json
import pytest
from parameters_for_testing import *

#=======================================CATEGORY ENDPOINT=======================================#

def test_read_category(client, user_token):
    response = client.get("/category/", headers=user_token)
    assert response.status_code == 200
    assert all(item in response.json() for item in readCategoryData)

@pytest.mark.parametrize('params', createCategoryData)
def test_create_category(params, client, user_token):
    response = client.post("/category/", data= json.dumps(params), headers=user_token)
    assert response.status_code == 201

def test_update_category(client, user_token):
    response = client.patch("/category/2", data=json.dumps(updateCategoryData), headers=user_token)
    assert response.status_code == 200

def test_delete_category(client, user_token):
    response = client.delete("/category/1", headers=user_token)
    assert response.status_code == 204