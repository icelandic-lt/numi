import pytest
from numi import spell_out




@pytest.mark.parametrize("test_input, expected", [
    ((92, "ft_kvk_þgf"), ["níutíu og tveimur", "níutíu og tveim"]),
    ((124, "ft_kk_nf"), ["eitt hundrað tuttugu og fjórir", "hundrað tuttugu og fjórir"]),
    ((791, "et_hk_nf"), ["sjö hundruð níutíu og eitt"]),
    ((100, "at_af"), ["eitt hundrað", "hundrað"])
])
def test_integer(test_input, expected):
    assert spell_out(test_input[0],test_input[1]) == expected

