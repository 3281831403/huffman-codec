import pytest

from codec import huffman as mod

CASES = [
    ('frequencies', ['aab'], {'a': 2, 'b': 1}, False),
    ('frequencies', [''], {}, False),
    ('build_codes', [{'a': 1, 'b': 1}], {'a': '0', 'b': '1'}, False),
    ('build_codes', [{'a': 3}], {'a': '0'}, False),
    ('encode', ['ab', {'a': '0', 'b': '1'}], '01', False),
    ('decode', ['01', {'a': '0', 'b': '1'}], 'ab', False),
    ('compression_ratio', ['abcd', '01010101'], 0.25, True),
    ('compression_ratio', ['', ''], 0.0, True),
    ('frequencies', ['aaa'], {'a': 3}, False),
    ('build_codes', [{'a': 2, 'b': 1}], {'b': '0', 'a': '1'}, False),
    ('encode', ['', {}], '', False),
    ('encode', ['aa', {'a': '1'}], '11', False),
    ('decode', ['', {'a': '0'}], '', False),
    ('decode', ['111', {'a': '1'}], 'aaa', False),
    ('compression_ratio', ['ab', '0'], 0.0625, True),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_huffman_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
