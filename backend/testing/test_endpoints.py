import json
import pytest
from parameters_for_testing import *

#####################################################################################################################
#                                                                                                                   #
#                            Ścieżka do pliku config do wykonywania testów jednostkowych                            #
#       /mnt/d/Studia/programowanie defensywne - projekt/warehouseManagment/backend/configuration/config.yaml       #
#                                                                                                                   #
#####################################################################################################################

#=======================================CATEGORY ENDPOINT=======================================#

def test_read_category(client, user_token):
    response = client.get("/category/", headers=user_token)
    assert response.status_code == 200
    assert all(item in response.json() for item in readCategoryData)

def test_read_category_by_id(client, user_token):
    response = client.get("/category/2", headers=user_token)
    assert response.status_code == 200
    assert response.json() == readCategoryDataById

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

#=======================================PRODUCT ENDPOINT=======================================#
def test_read_product(client, user_token):
    response = client.get("/product/", headers=user_token)
    assert response.status_code == 200
    assert all(item in response.json() for item in readProductData)

def test_read_product_by_id(client, user_token):
    response = client.get("/product/4", headers=user_token)
    assert response.status_code == 200
    assert response.json() == readProductDataById

@pytest.mark.parametrize('params', createProductData)
def test_create_product(params, client, user_token):
    response = client.post("/product/", data= json.dumps(params), headers=user_token)
    assert response.status_code == 201
    assert response.json() == params

def test_read_amount(client, user_token):
    response = client.get("/product/2", headers=user_token)
    assert response.status_code == 200

def test_delete_product(client, user_token):
    response = client.delete("/product/1", headers=user_token)
    assert response.status_code == 204

#=======================================PERSON ENDPOINT=======================================#
def test_read_person(client, user_token):
    response = client.get("/person/", headers=user_token)
    assert response.status_code == 200
    assert all(item in response.json() for item in readPersonData)

def test_read_person_by_id(client, user_token):
    response = client.get("/person/1", headers=user_token)
    assert response.status_code == 200
    assert response.json() == readPersonByIdData

def test_create_person(client, user_token):
    response = client.post("/person/", data= json.dumps(createPersonData), headers=user_token)
    assert response.status_code == 201
    assert response.json() == createPersonData


def test_delete_person(client, user_token):
    response = client.delete("/person/1", headers=user_token)
    assert response.status_code == 204

#=======================================EMPLOYEE ENDPOINT=======================================#

def test_read_employee(client, user_token):
    response = client.get("/employee/", headers=user_token)
    assert response.status_code == 200
    assert all(item in response.json() for item in readEmployeeData)

def test_read_employee_by_id(client, user_token):
    response = client.get("/employee/3", headers=user_token)
    assert response.status_code == 200
    assert response.json() == readEmployeeByIdData

def test_create_employee(client, user_token):
    response = client.post("/employee/", data= json.dumps(createEmployeeData), headers=user_token)
    assert response.status_code == 201

def test_update_employee(client, user_token):
    response = client.patch("/employee/2", data=json.dumps(updateEmployeeData), headers=user_token)
    assert response.status_code == 200

def test_delete_employee(client, user_token):
    response = client.delete("/employee/1", headers=user_token)
    assert response.status_code == 204

#=======================================ROLE ENDPOINT=======================================#
def test_read_role(client, user_token):
    response = client.get("/role/", headers=user_token)
    assert response.status_code == 200
    assert all(item in response.json() for item in readRoleData)

def test_read_role_by_id(client, user_token):
    response = client.get("/role/1", headers=user_token)
    assert response.status_code == 200
    assert response.json() == readRoleByIdData

def test_create_role(client, user_token):
    response = client.post("/role/", data= json.dumps(createAndUpdateRoleData), headers=user_token)
    assert response.status_code == 201

def test_update_role(client, user_token):
    response = client.patch("/role/1", data=json.dumps(createAndUpdateRoleData), headers=user_token)
    assert response.status_code == 200

def test_delete_role(client, user_token):
    response = client.delete("/role/1", headers=user_token)
    assert response.status_code == 204

#=======================================USERS ENDPOINT=======================================#
def test_read_user(client, user_token):
    response = client.get("/users/me", headers=user_token)
    assert response.status_code == 200
    assert response.json() == readUser

def test_create_user(client):
    response = client.post("/users/create", data= json.dumps(createUserData))
    assert response.status_code == 201

def test_generate_otp_code(client):
    response = client.post("/users/OTP_code", data= json.dumps(otpCodeData))
    assert response.status_code == 200
    assert response.json() == "Code generated"
