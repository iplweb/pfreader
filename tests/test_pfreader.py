import os

from pfreader.core import dir_contains_pflex_data, get_machines, get_loxfiles, get_year_dirs, get_loxfile_data
from pfreader.pfreader import UserEvents, SystemEvents, PLC, Tare, PLI, PLL, RepositioningData, CalibrationScaleData, \
    CalibrationPressureData, Summary
from .conftest import TEST_MACHINE, TEST_YEAR, TEST_LOXFILE


def test_not_dir_contains_pflex_data(not_testdir):
    assert not dir_contains_pflex_data(not_testdir)


def test_dir_contains_pflex_data(testdir):
    assert dir_contains_pflex_data(testdir)


def test_get_machines(testdir):
    assert list(get_machines(testdir)) == [TEST_MACHINE]


def test_get_years(testmachine):
    assert list(get_year_dirs(testmachine)) == [TEST_YEAR]


def test_get_loxfiles(testmachine):
    assert list(get_loxfiles(os.path.join(testmachine, str(TEST_YEAR)))) == [TEST_LOXFILE]


def test_get_loxfile_data(testloxfile):
    assert get_loxfile_data(testloxfile) is not None


def test_PFMachineData_get_year_dirs(pfmachine):
    assert list(pfmachine.get_year_dirs()) == [TEST_YEAR]


def test_PFMachineData_get_loxfiles(pfmachine):
    assert list(pfmachine.get_loxfiles(TEST_YEAR)) == [TEST_LOXFILE]


def test_PFMachineData_get_loxfile_data(pfmachine):
    data = pfmachine.get_loxfile_data(TEST_YEAR, TEST_LOXFILE)
    assert data['Pressure'] is not None
    assert len(data['Pressure']) == 231


def test_UserEvents(loxdata):
    ue = UserEvents(loxdata["User events"])

    metrics = ue.get_metrics()
    assert metrics[0][0] == "MonitorID"

    header = ue.get_header()
    assert header[0] == "Index"

    assert len(ue.get_data()) == 221


def test_CalibrationPressureData(loxdata):
    cpd = CalibrationPressureData(loxdata['User events'])
    assert cpd.get_header()[0] == "Pressure:"
    assert len(cpd.get_data()) == 6


def test_CalibrationScaleData(loxdata):
    csd = CalibrationScaleData(loxdata['User events'])
    assert csd.get_header()[0] == "Scale:"
    assert len(csd.get_data()) == 4


def test_RepositioningData(loxdata):
    rpd = RepositioningData(loxdata['User events'])
    assert rpd.get_header()[0] == "Repositioning data:"
    assert len(rpd.get_data()) == 3


def test_SystemEvents(loxdata):
    se = SystemEvents(loxdata["System events"])
    data = list(se.get_data())
    assert data[0][1] == "Cal ent"


def test_PLC(loxdata):
    plc = PLC(loxdata["PLC"])
    assert plc.get_header()[0] == "Index"
    assert len(plc.get_data()) == 38


def test_PLI(loxdata):
    pli = PLI(loxdata["PLI"])
    assert pli.get_header()[0] == "Index"
    assert len(pli.get_data()) == 47

def test_Summary(loxdata):
    s = Summary(loxdata["User events"])
    r = list(s.get_data())
    assert r[2][1] == "as planned"
    assert r[5][1] == "TPE"

def test_PLL(loxdata):
    pll = PLL(loxdata["PLL"])
    assert pll.get_header()[0] == "Index"
    assert len(pll.get_data()) == 37


def test_Tare(loxdata):
    plt = Tare(loxdata["Tare"])
    assert plt.get_header()[0] == "Index"
    assert len(plt.get_data()) == 12


def test_Fluids(loxdata):
    plt = Tare(loxdata["Fluids"])
    assert plt.get_header()[0] == "Index"
    assert len(plt.get_data()) == 224
