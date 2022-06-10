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


@pytest.mark.parametrize("test_input, expected", [
    ((92, None), [[92, 'ft_hk_ef', ['níutíu og tveggja']], [92, 'ft_hk_nf', ['níutíu og tvö']], [92, 'ft_hk_þf', ['níutíu og tvö']], [92, 'ft_hk_þgf', ['níutíu og tveimur', 'níutíu og tveim']], [92, 'ft_kk_ef', ['níutíu og tvegga']], [92, 'ft_kk_nf', ['níutíu og tveir']], [92, 'ft_kk_þf', ['níutíu og tvo']], [92, 'ft_kk_þgf', ['níutíu og tveimur', 'níutíu og tveim']], [92, 'ft_kvk_ef', ['níutíu og tveggja']], [92, 'ft_kvk_nf', ['níutíu og tvær']], [92, 'ft_kvk_þf', ['níutíu og tvær']], [92, 'ft_kvk_þgf', ['níutíu og tveimur', 'níutíu og tveim']]]),
    ((92, "þgf_ft_kvk"), ['níutíu og tveimur', 'níutíu og tveim']),
    ((92, "kvk"), [[92, 'ft_kvk_nf', ['níutíu og tvær']], [92, 'ft_kvk_þf', ['níutíu og tvær']], [92, 'ft_kvk_þgf', ['níutíu og tveimur', 'níutíu og tveim']], [92, 'ft_kvk_ef', ['níutíu og tveggja']]]),
    ((92, "ft_kvk"), [[92, 'ft_kvk_nf', ['níutíu og tvær']], [92, 'ft_kvk_þf', ['níutíu og tvær']], [92, 'ft_kvk_þgf', ['níutíu og tveimur', 'níutíu og tveim']], [92, 'ft_kvk_ef', ['níutíu og tveggja']]]),
    ((100, "at_af"), ["eitt hundrað", "hundrað"]),
    ((79, "at_af"), ['sjötíu og níu']),
    ((13, "at_af"), ["þrettán"]),
    ((121, None), [[121, 'et_hk_ef', ['eitt hundrað tuttugu og eins', 'hundrað tuttugu og eins']], [121, 'et_hk_nf', ['eitt hundrað tuttugu og eitt', 'hundrað tuttugu og eitt']], [121, 'et_hk_þf', ['eitt hundrað tuttugu og eitt', 'hundrað tuttugu og eitt']], [121, 'et_hk_þgf', ['eitt hundrað tuttugu og einu', 'hundrað tuttugu og einu']], [121, 'et_kk_ef', ['eitt hundrað tuttugu og eins', 'hundrað tuttugu og eins']], [121, 'et_kk_nf', ['eitt hundrað tuttugu og einn', 'hundrað tuttugu og einn']], [121, 'et_kk_þf', ['eitt hundrað tuttugu og einn', 'hundrað tuttugu og einn']], [121, 'et_kk_þgf', ['eitt hundrað tuttugu og einum', 'hundrað tuttugu og einum']], [121, 'et_kvk_ef', ['eitt hundrað tuttugu og einnar', 'hundrað tuttugu og einnar']], [121, 'et_kvk_nf', ['eitt hundrað tuttugu og ein', 'hundrað tuttugu og ein']], [121, 'et_kvk_þf', ['eitt hundrað tuttugu og eina', 'hundrað tuttugu og eina']], [121, 'et_kvk_þgf', ['eitt hundrað tuttugu og einni', 'hundrað tuttugu og einni']], [121, 'ft_hk_ef', ['eitt hundrað tuttugu og einna', 'hundrað tuttugu og einna']], [121, 'ft_hk_nf', ['eitt hundrað tuttugu og ein', 'hundrað tuttugu og ein']], [121, 'ft_hk_þf', ['eitt hundrað tuttugu og ein', 'hundrað tuttugu og ein']], [121, 'ft_hk_þgf', ['eitt hundrað tuttugu og einum', 'hundrað tuttugu og einum']], [121, 'ft_kk_ef', ['eitt hundrað tuttugu og einna', 'hundrað tuttugu og einna']], [121, 'ft_kk_nf', ['eitt hundrað tuttugu og einir', 'hundrað tuttugu og einir']], [121, 'ft_kk_þf', ['eitt hundrað tuttugu og eina', 'hundrað tuttugu og eina']], [121, 'ft_kk_þgf', ['eitt hundrað tuttugu og einum', 'hundrað tuttugu og einum']], [121, 'ft_kvk_ef', ['eitt hundrað tuttugu og einna', 'hundrað tuttugu og einna']], [121, 'ft_kvk_nf', ['eitt hundrað tuttugu og einar', 'hundrað tuttugu og einar']], [121, 'ft_kvk_þf', ['eitt hundrað tuttugu og einar', 'hundrað tuttugu og einar']], [121, 'ft_kvk_þgf', ['eitt hundrað tuttugu og einum', 'hundrað tuttugu og einum']]])
    ])
def test_messy_integer_input(test_input, expected):
    assert spell_out(test_input[0],test_input[1]) == expected




