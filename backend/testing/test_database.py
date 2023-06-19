import pytest
from parameters_for_testing import *
from database.database import engine


@pytest.mark.parametrize('url', databaseIncorrectUrlParams)
def test_incorrect_database_url(url):
    """
    Test case to check if the provided URL is incorrect.

    Args:
        url (str): Database URL.

    """
    assert str(engine.url) not in url

def test_correct_database_url():
    """
    Test case to check if the provided URL is correct.

    """
    assert str(engine.url) in databaseCorrectUrlParams

