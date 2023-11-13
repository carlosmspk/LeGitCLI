from legitcli.typeutils.guards import assert_type
import pytest
import unittest


class TestAssertType(unittest.TestCase):
    def test_exception_raise_for_bad_type(self):
        with pytest.raises(TypeError) as e_info:
            not_a_string = {}
            assert_type(not_a_string, str, "not_a_string")
        assert "not_a_string" in str(e_info)

    def test_no_exception_raised_for_good_type(self):
        assert_type("a_string", str, "var_name")

    def test_exception_raise_for_none_type(self):
        with pytest.raises(TypeError) as e_info:
            not_a_string = None
            assert_type(not_a_string, str, "not_a_string")
        assert "not_a_string" in str(e_info)


if __name__ == "__main__":
    unittest.main()
