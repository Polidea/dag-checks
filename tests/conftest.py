import os

import pytest

from tests import TEST_FOLDER

os.environ["AIRFLOW_HOME"] = TEST_FOLDER
os.environ["AIRFLOW__CORE__SQL_ALCHEMY_CONN"] = "sqlite:///{}/airflow.db".format(TEST_FOLDER)


# pylint: disable=import-outside-toplevel


@pytest.fixture(scope="session", autouse=True)
def reset_db_fixture():
    from airflow.utils.db import resetdb

    resetdb(None)
    yield
