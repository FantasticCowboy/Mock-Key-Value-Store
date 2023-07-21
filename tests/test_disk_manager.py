from src.disk_manager import DiskManager


def test_simple():
    manager = DiskManager("./")    
    manager.write("a", "b")
    manager.write("b", "b")
    assert manager.read("a") == "b"
    manager.expand()
    assert manager.read("a") == "b"
    assert manager.read("b") == "b"