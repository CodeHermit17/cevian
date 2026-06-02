import cevian

def test_import():
    """Cevian imports successfully."""
    assert cevian is not None

def test_core_import():
    """C++ core module loads."""
    assert cevian._core is not None

def test_version():
    """Version string exists."""
    assert cevian.__version__ == "0.1.0-dev"