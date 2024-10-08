from convertor.mesh_types import FileFormat


def test_stl_to_string():
    stl = FileFormat.STL
    assert str(stl) == "stl"


def test_obj_to_string():
    obj = FileFormat.OBJ
    assert str(obj) == "obj"


def test_get_string_array():
    assert FileFormat.get_string_array() == ["stl", "obj"]


def test_get_stl_file_format_from_string():
    assert FileFormat.get_file_format_from_string("stl") == FileFormat.STL
    assert FileFormat.get_file_format_from_string("STL") == FileFormat.STL


def test_get_obj_file_format_from_string():
    assert FileFormat.get_file_format_from_string("obj") == FileFormat.OBJ
    assert FileFormat.get_file_format_from_string("OBJ") == FileFormat.OBJ


def test_get_stl_file_format_from_unkown_string():
    assert FileFormat.get_file_format_from_string("") == FileFormat.STL
    assert FileFormat.get_file_format_from_string("unkown") == FileFormat.STL
