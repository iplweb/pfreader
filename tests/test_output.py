from pfreader.output import get_databook
from .conftest import TEST_YEAR, TEST_LOXFILE


def test_get_tablib(pfmachine):
    data = pfmachine.get_loxfile_data(TEST_YEAR, TEST_LOXFILE)
    db = get_databook(data)
    with open("test.xlsx", "wb") as f:
        f.write(db.xlsx)
    assert db is not None
