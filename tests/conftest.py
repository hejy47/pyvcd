"""Custom test fixtures for pyvcd."""

import io

import pytest


@pytest.yield_fixture
def gtkw():
    import vcd.gtkw

    sio = io.StringIO()
    gtkw = vcd.gtkw.GTKWSave(sio)
    try:
        yield gtkw
    finally:
        sio.close()
