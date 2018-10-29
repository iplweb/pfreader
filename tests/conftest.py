import os

import pytest

from pfreader.core import get_loxfile_data
from pfreader.pfreader import PFMachineData

TEST_MACHINE = "PA020548"
TEST_YEAR = 2017
TEST_LOXFILE = "F31I999D.LOX"


@pytest.fixture
def testdir():
    return os.path.join(
        os.path.dirname(__file__),
        "testdata")


@pytest.fixture
def not_testdir():
    return os.path.join(
        os.path.dirname(__file__),
        ".."
    )


@pytest.fixture
def testmachine(testdir):
    return os.path.join(testdir, TEST_MACHINE)


@pytest.fixture
def pfmachine(testdir):
    return PFMachineData(testdir, TEST_MACHINE)


@pytest.fixture
def testloxfile(testmachine):
    return os.path.join(testmachine, str(TEST_YEAR), TEST_LOXFILE)


@pytest.fixture
def loxdata(testloxfile):
    return get_loxfile_data(testloxfile)
