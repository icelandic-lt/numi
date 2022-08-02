import pytest
from numi import spell_out


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            (92, None),
            [
                [92, "ft_hk_ef", ["níutíu og tveggja"]],
                [92, "ft_hk_nf", ["níutíu og tvö"]],
                [92, "ft_hk_þf", ["níutíu og tvö"]],
                [92, "ft_hk_þgf", ["níutíu og tveimur", "níutíu og tveim"]],
                [92, "ft_kk_ef", ["níutíu og tvegga"]],
                [92, "ft_kk_nf", ["níutíu og tveir"]],
                [92, "ft_kk_þf", ["níutíu og tvo"]],
                [92, "ft_kk_þgf", ["níutíu og tveimur", "níutíu og tveim"]],
                [92, "ft_kvk_ef", ["níutíu og tveggja"]],
                [92, "ft_kvk_nf", ["níutíu og tvær"]],
                [92, "ft_kvk_þf", ["níutíu og tvær"]],
                [92, "ft_kvk_þgf", ["níutíu og tveimur", "níutíu og tveim"]],
            ],
        ),
        ((92, "þgf_ft_kvk"), ["níutíu og tveimur", "níutíu og tveim"]),
        (
            (92, "kvk"),
            [
                [92, "ft_kvk_nf", ["níutíu og tvær"]],
                [92, "ft_kvk_þf", ["níutíu og tvær"]],
                [92, "ft_kvk_þgf", ["níutíu og tveimur", "níutíu og tveim"]],
                [92, "ft_kvk_ef", ["níutíu og tveggja"]],
            ],
        ),
        (
            (92, "ft_kvk"),
            [
                [92, "ft_kvk_nf", ["níutíu og tvær"]],
                [92, "ft_kvk_þf", ["níutíu og tvær"]],
                [92, "ft_kvk_þgf", ["níutíu og tveimur", "níutíu og tveim"]],
                [92, "ft_kvk_ef", ["níutíu og tveggja"]],
            ],
        ),
        ((100, "at_af"), ["eitt hundrað", "hundrað"]),
        ((79, "at_af"), ["sjötíu og níu"]),
        ((13, "at_af"), ["þrettán"]),
        (
            (121, None),
            [
                [
                    121,
                    "et_hk_ef",
                    ["eitt hundrað tuttugu og eins", "hundrað tuttugu og eins"],
                ],
                [
                    121,
                    "et_hk_nf",
                    ["eitt hundrað tuttugu og eitt", "hundrað tuttugu og eitt"],
                ],
                [
                    121,
                    "et_hk_þf",
                    ["eitt hundrað tuttugu og eitt", "hundrað tuttugu og eitt"],
                ],
                [
                    121,
                    "et_hk_þgf",
                    ["eitt hundrað tuttugu og einu", "hundrað tuttugu og einu"],
                ],
                [
                    121,
                    "et_kk_ef",
                    ["eitt hundrað tuttugu og eins", "hundrað tuttugu og eins"],
                ],
                [
                    121,
                    "et_kk_nf",
                    ["eitt hundrað tuttugu og einn", "hundrað tuttugu og einn"],
                ],
                [
                    121,
                    "et_kk_þf",
                    ["eitt hundrað tuttugu og einn", "hundrað tuttugu og einn"],
                ],
                [
                    121,
                    "et_kk_þgf",
                    ["eitt hundrað tuttugu og einum", "hundrað tuttugu og einum"],
                ],
                [
                    121,
                    "et_kvk_ef",
                    ["eitt hundrað tuttugu og einnar", "hundrað tuttugu og einnar"],
                ],
                [
                    121,
                    "et_kvk_nf",
                    ["eitt hundrað tuttugu og ein", "hundrað tuttugu og ein"],
                ],
                [
                    121,
                    "et_kvk_þf",
                    ["eitt hundrað tuttugu og eina", "hundrað tuttugu og eina"],
                ],
                [
                    121,
                    "et_kvk_þgf",
                    ["eitt hundrað tuttugu og einni", "hundrað tuttugu og einni"],
                ],
                [
                    121,
                    "ft_hk_ef",
                    ["eitt hundrað tuttugu og einna", "hundrað tuttugu og einna"],
                ],
                [
                    121,
                    "ft_hk_nf",
                    ["eitt hundrað tuttugu og ein", "hundrað tuttugu og ein"],
                ],
                [
                    121,
                    "ft_hk_þf",
                    ["eitt hundrað tuttugu og ein", "hundrað tuttugu og ein"],
                ],
                [
                    121,
                    "ft_hk_þgf",
                    ["eitt hundrað tuttugu og einum", "hundrað tuttugu og einum"],
                ],
                [
                    121,
                    "ft_kk_ef",
                    ["eitt hundrað tuttugu og einna", "hundrað tuttugu og einna"],
                ],
                [
                    121,
                    "ft_kk_nf",
                    ["eitt hundrað tuttugu og einir", "hundrað tuttugu og einir"],
                ],
                [
                    121,
                    "ft_kk_þf",
                    ["eitt hundrað tuttugu og eina", "hundrað tuttugu og eina"],
                ],
                [
                    121,
                    "ft_kk_þgf",
                    ["eitt hundrað tuttugu og einum", "hundrað tuttugu og einum"],
                ],
                [
                    121,
                    "ft_kvk_ef",
                    ["eitt hundrað tuttugu og einna", "hundrað tuttugu og einna"],
                ],
                [
                    121,
                    "ft_kvk_nf",
                    ["eitt hundrað tuttugu og einar", "hundrað tuttugu og einar"],
                ],
                [
                    121,
                    "ft_kvk_þf",
                    ["eitt hundrað tuttugu og einar", "hundrað tuttugu og einar"],
                ],
                [
                    121,
                    "ft_kvk_þgf",
                    ["eitt hundrað tuttugu og einum", "hundrað tuttugu og einum"],
                ],
            ],
        ),
    ],
)
def test_messy_integer(test_input, expected):
    assert spell_out(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((92, "ft_kvk_þgf"), ["níutíu og tveimur", "níutíu og tveim"]),
        (
            (124, "ft_kk_nf"),
            ["eitt hundrað tuttugu og fjórir", "hundrað tuttugu og fjórir"],
        ),
        ((791, "et_hk_nf"), ["sjö hundruð níutíu og eitt"]),
        ((100, "at_af"), ["eitt hundrað", "hundrað"]),
        (
            (1, None),
            [
                [1, "et_hk_ef", ["eins"]],
                [1, "et_hk_nf", ["eitt"]],
                [1, "et_hk_þf", ["eitt"]],
                [1, "et_hk_þgf", ["einu"]],
                [1, "et_kk_ef", ["eins"]],
                [1, "et_kk_nf", ["einn"]],
                [1, "et_kk_þf", ["einn"]],
                [1, "et_kk_þgf", ["einum"]],
                [1, "et_kvk_ef", ["einnar"]],
                [1, "et_kvk_nf", ["ein"]],
                [1, "et_kvk_þf", ["eina"]],
                [1, "et_kvk_þgf", ["einni"]],
                [1, "ft_hk_ef", ["einna"]],
                [1, "ft_hk_nf", ["ein"]],
                [1, "ft_hk_þf", ["ein"]],
                [1, "ft_hk_þgf", ["einum"]],
                [1, "ft_kk_ef", ["einna"]],
                [1, "ft_kk_nf", ["einir"]],
                [1, "ft_kk_þf", ["eina"]],
                [1, "ft_kk_þgf", ["einum"]],
                [1, "ft_kvk_ef", ["einna"]],
                [1, "ft_kvk_nf", ["einar"]],
                [1, "ft_kvk_þf", ["einar"]],
                [1, "ft_kvk_þgf", ["einum"]],
            ],
        ),
    ],
)
def test_0_999(test_input, expected):
    assert spell_out(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ((1000, "at_af"), ["eitt þúsund", "þúsund"]),
        ((3124, "ft_kk_nf"), ["þrjú þúsund eitt hundrað tuttugu og fjórir"]),
        ((1791, "et_hk_nf"), ["eitt þúsund sjö hundruð níutíu og eitt"]),
        ((5001, "et_kk_nf"), ["fimm þúsund og einn"]),
    ],
)
def test_1000_9999(test_input, expected):
    assert spell_out(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            (21123, None),
            [
                [
                    21123,
                    "ft_hk_ef",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þriggja"],
                ],
                [
                    21123,
                    "ft_hk_nf",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þrjú"],
                ],
                [
                    21123,
                    "ft_hk_þf",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þrjú"],
                ],
                [
                    21123,
                    "ft_hk_þgf",
                    [
                        "tuttugu og eitt þúsund eitt hundrað tuttugu og þremur",
                        "tuttugu og eitt þúsund eitt hundrað tuttugu og þrem",
                    ],
                ],
                [
                    21123,
                    "ft_kk_ef",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þriggja"],
                ],
                [
                    21123,
                    "ft_kk_nf",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þrír"],
                ],
                [
                    21123,
                    "ft_kk_þf",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þrjá"],
                ],
                [
                    21123,
                    "ft_kk_þgf",
                    [
                        "tuttugu og eitt þúsund eitt hundrað tuttugu og þremur",
                        "tuttugu og eitt þúsund eitt hundrað tuttugu og þrem",
                    ],
                ],
                [
                    21123,
                    "ft_kvk_ef",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þriggja"],
                ],
                [
                    21123,
                    "ft_kvk_nf",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þrjár"],
                ],
                [
                    21123,
                    "ft_kvk_þf",
                    ["tuttugu og eitt þúsund eitt hundrað tuttugu og þrjár"],
                ],
                [
                    21123,
                    "ft_kvk_þgf",
                    [
                        "tuttugu og eitt þúsund eitt hundrað tuttugu og þremur",
                        "tuttugu og eitt þúsund eitt hundrað tuttugu og þrem",
                    ],
                ],
            ],
        ),
        ((10000, None), ["tíu þúsund"]),
        (
            (92, None),
            [
                [92, "ft_hk_ef", ["níutíu og tveggja"]],
                [92, "ft_hk_nf", ["níutíu og tvö"]],
                [92, "ft_hk_þf", ["níutíu og tvö"]],
                [92, "ft_hk_þgf", ["níutíu og tveimur", "níutíu og tveim"]],
                [92, "ft_kk_ef", ["níutíu og tvegga"]],
                [92, "ft_kk_nf", ["níutíu og tveir"]],
                [92, "ft_kk_þf", ["níutíu og tvo"]],
                [92, "ft_kk_þgf", ["níutíu og tveimur", "níutíu og tveim"]],
                [92, "ft_kvk_ef", ["níutíu og tveggja"]],
                [92, "ft_kvk_nf", ["níutíu og tvær"]],
                [92, "ft_kvk_þf", ["níutíu og tvær"]],
                [92, "ft_kvk_þgf", ["níutíu og tveimur", "níutíu og tveim"]],
            ],
        ),
        (
            (512321, None),
            [
                [
                    512321,
                    "et_hk_ef",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og eins"],
                ],
                [
                    512321,
                    "et_hk_nf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og eitt"],
                ],
                [
                    512321,
                    "et_hk_þf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og eitt"],
                ],
                [
                    512321,
                    "et_hk_þgf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einu"],
                ],
                [
                    512321,
                    "et_kk_ef",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og eins"],
                ],
                [
                    512321,
                    "et_kk_nf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einn"],
                ],
                [
                    512321,
                    "et_kk_þf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einn"],
                ],
                [
                    512321,
                    "et_kk_þgf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einum"],
                ],
                [
                    512321,
                    "et_kvk_ef",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einnar"],
                ],
                [
                    512321,
                    "et_kvk_nf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og ein"],
                ],
                [
                    512321,
                    "et_kvk_þf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og eina"],
                ],
                [
                    512321,
                    "et_kvk_þgf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einni"],
                ],
                [
                    512321,
                    "ft_hk_ef",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einna"],
                ],
                [
                    512321,
                    "ft_hk_nf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og ein"],
                ],
                [
                    512321,
                    "ft_hk_þf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og ein"],
                ],
                [
                    512321,
                    "ft_hk_þgf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einum"],
                ],
                [
                    512321,
                    "ft_kk_ef",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einna"],
                ],
                [
                    512321,
                    "ft_kk_nf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einir"],
                ],
                [
                    512321,
                    "ft_kk_þf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og eina"],
                ],
                [
                    512321,
                    "ft_kk_þgf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einum"],
                ],
                [
                    512321,
                    "ft_kvk_ef",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einna"],
                ],
                [
                    512321,
                    "ft_kvk_nf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einar"],
                ],
                [
                    512321,
                    "ft_kvk_þf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einar"],
                ],
                [
                    512321,
                    "ft_kvk_þgf",
                    ["fimm hundruð og tólf þúsund þrjú hundruð tuttugu og einum"],
                ],
            ],
        ),
        ((100021, "et_kvk_ef"), ["hundrað þúsund tuttugu og einnar"]),
        ((100011, None), ["hundrað þúsund og ellefu"]),
        ((100001, "et_kvk_ef"), ["hundrað þúsund og einnar"]),
        ((100221, "et_kvk_ef"), ["hundrað þúsund tvö hundruð tuttugu og einnar"]),
        ((100020, None), ["hundrað þúsund og tuttugu"]),
        ((10021, "et_kvk_ef"), ["tíu þúsund tuttugu og einnar"]),
        ((10011, None), ["tíu þúsund og ellefu"]),
        ((10001, "et_kvk_ef"), ["tíu þúsund og einnar"]),
        ((10221, "et_kvk_ef"), ["tíu þúsund tvö hundruð tuttugu og einnar"]),
        ((10020, None), ["tíu þúsund og tuttugu"]),
    ],
)
def test_10000_999999(test_input, expected):
    assert spell_out(test_input[0], test_input[1]) == expected
