import os

import pytest

from tests import TEST_FOLDER

os.environ["AIRFLOW_HOME"] = TEST_FOLDER
os.environ["AIRFLOW__CORE__SQL_ALCHEMY_CONN"] = "sqlite:///{}/airflow.db".format(TEST_FOLDER)


# pylint: disable=import-outside-toplevel


@pytest.fixture(scope="session", autouse=True)
def reset_db_fixture():
    from airflow.utils.db import resetdb

    try:
        resetdb(None)  # Airflow 1.10
    except TypeError:
        resetdb()  # pylint: disable=no-value-for-parameter
    yield
