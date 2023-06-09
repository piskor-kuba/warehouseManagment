import pytest
from parameters_for_testing import *
import models.tableModel as model
from pydantic import ValidationError

#=======================================CATEGORY MODEL=======================================#
def test_correct_type_category_model():
    """
    Test case to verify that the CategoryBase model accepts correct string type values.

    """
    assert model.CategoryBase(name="Correct String type")

@pytest.mark.parametrize('params', tableModelIncorrectTypeParamsForCategory)
def test_incorrect_type_category_model(params):
    """
    Test case to verify that the CategoryBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.CategoryBase(name=params)
        assert False
    except ValidationError:
        assert True

#=======================================PRODUCT MODEL=======================================#
def test_correct_type_product_model_without_describe():
    """
    Test case to verify that the ProductBase model accepts correct string type values without describe.

    """
    assert model.ProductBase(id_category=1,name="Correct String type")

def test_correct_type_product_model_with_describe():
    """
    Test case to verify that the ProductBase model accepts correct string type values with describe.

    """
    assert model.ProductBase(id_category=1,name="Correct String type",describe="Value for the optional argument")

@pytest.mark.parametrize('id,name', tableModelIncorrectTypeParamsForProductWithoutDescribe)
def test_incorrect_type_product_model_without_describe(id,name):
    """
    Test case to verify that the ProductBase model raises a ValidationError for incorrect type values without describe.

    """
    try:
        model.ProductBase(id_category=id, name=name)
        assert False
    except ValidationError as e:
        assert True

@pytest.mark.parametrize('id,name,desc', tableModelIncorrectTypeParamsForProductWithDescribe)
def test_incorrect_type_product_model_with_describe(id,name,desc):
    """
    Test case to verify that the ProductBase model raises a ValidationError for incorrect type values with describe.

    """
    try:
        model.ProductBase(id_category=id, name=name, describe=desc)
        assert False
    except ValidationError as e:
        assert True

#=======================================PRODUCT_AMOUNT MODEL=======================================#
@pytest.mark.parametrize('id,amount', tableModelCorrectTypeParamsForProductAmount)
def test_correct_type_product_amount_model(id,amount):
    """
    Test case to verify that the ProductAmountBase model accepts correct type values for id_product and amount.

    """
    assert model.ProductAmountBase(id_product=id,amount=amount)

@pytest.mark.parametrize('id,amount', tableModelIncorrectTypeParamsForProductAmount)
def test_incorrect_type_product_amount_model(id,amount):
    """
    Test case to verify that the ProductAmountBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.ProductAmountBase(id_product=id,amount=amount)
        assert False
    except ValidationError as e:
        assert True

#=======================================PERSONS MODEL=======================================#
def test_correct_type_persons_model():
    """
    Test case to verify that the PersonsBase model accepts correct type values for name, surname, phone, and address.

    """
    assert model.PersonsBase(name="Jan",surname="Kowalski",phone="111-222-33",address="al.Tysiaclecia")

@pytest.mark.parametrize('name,surname,phone,address', tableModelIncorrectTypeParamsForPersons)
def test_incorrect_type_persons_model(name,surname,phone,address):
    """
    Test case to verify that the PersonsBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.PersonsBase(name=name,surname=surname,phone=phone,address=address)
    except ValidationError as e:
        assert True

#=======================================CLIENTS MODEL=======================================#
def test_correct_type_clients_model():
    """
    Test case to verify that the ClientsBase model accepts correct type values for id_persons and amount.

    """
    assert model.ClientsBase(id_persons=2,amount=100)

@pytest.mark.parametrize('id,amount', tableModelIncorrectTypeParamsForClients)
def test_incorrect_type_clients_model(id,amount):
    """
    Test case to verify that the ClientsBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.ClientsBase(id_persons=id,amount=amount)
        assert False
    except ValidationError as e:
        assert True

#=======================================CLIENT_PRODUCT MODEL=======================================#
def test_correct_type_client_product_model():
    """
    Test case to verify that the ClientProductBase model accepts correct type values for id_client and id_product.

    """
    assert model.ClientProductBase(id_client=22,id_product=78)

@pytest.mark.parametrize('id_product,id_client', tableModelIncorrectTypeParamsForClients)
def test_incorrect_type_client_product_model(id_product,id_client):
    """
    Test case to verify that the ClientProductBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.ClientsBase(id_persons=id_product,amount=id_client)
        assert False
    except ValidationError as e:
        assert True

#=======================================WORKPLACE MODEL=======================================#
def test_correct_type_workplace_model():
    assert model.WorkplaceBase(name="Workplace")

@pytest.mark.parametrize('name', tableModelIncorrectTypeParamsForWorkplaceAndRole)
def test_incorrect_type_workplace_model(name):
    try:
        model.WorkplaceBase(name=name)
        assert False
    except ValidationError as e:
        assert True

#=======================================ROLE MODEL=======================================#
def test_correct_type_role_model():
    """
    Test case to verify that the WorkplaceBase model accepts correct type values for the name attribute.

    """
    assert model.RoleBase(name="Role")

@pytest.mark.parametrize('name', tableModelIncorrectTypeParamsForWorkplaceAndRole)
def test_incorrect_type_role_model(name):
    """
    Test case to verify that the WorkplaceBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.RoleBase(name=name)
        assert False
    except ValidationError as e:
        assert True

#=======================================EMPLOYEES MODEL=======================================#
def test_correct_type_employees_model():
    """
    Test case to verify that the EmployeesBase model accepts correct type values for the id_persons, id_workplace, and id_role attributes.

    """
    assert model.EmployeesBase(id_persons=0,id_workplace=1,id_role=2)

@pytest.mark.parametrize('id_person,id_workplace,id_role', tableModelIncorrectTypeParamsForEmployees)
def test_incorrect_type_employees_model(id_person,id_workplace,id_role):
    """
    Test case to verify that the EmployeesBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.EmployeesBase(id_person=id_person,id_workplace=id_workplace,id_role=id_role)
        assert False
    except ValidationError as e:
        assert True

#=======================================LOGIN_DATA MODEL=======================================#
def test_correct_type_login_data_model():
    """
    Test case to verify that the LoginDataBase model accepts correct type values for the login, password, and disabled attributes.

    """
    assert model.LoginDataBase(login="login@test.pl",password="password",disabled=False)

@pytest.mark.parametrize('login,password,disabled', tableModelIncorrectTypeParamsForLoginData)
def test_incorrect_type_login_data_model(login,password,disabled):
    """
    Test case to verify that the LoginDataBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.LoginDataBase(login=login,password=password,disabled=disabled)
        assert False
    except ValidationError as e:
        assert True

#=======================================OTP MODEL=======================================#
def test_correct_type_otp_model():
    """
    Test case to verify that the OtpBase model accepts correct type values for the login and otp_code attributes.

    """
    assert model.OtpBase(login="login@test.pl",otp_code="000123")

@pytest.mark.parametrize('login,,otp', tableModelIncorrectTypeParamsForOtp)
def test_incorrect_type_otp_model(login,otp):
    """
    Test case to verify that the OtpBase model raises a ValidationError for incorrect type values.

    """
    try:
        model.OtpBase(login=login,otp_code=otp)
        assert False
    except ValidationError as e:
        assert True