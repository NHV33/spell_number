import pytest
from spell_number.spell_number import SpellNumber

def test_digit_length():
    # Check that digit_length method produces the same output as len(string) for positive integers.
    for i in range(1000):
        assert SpellNumber.digit_length(i) == len(str(i))

def test_spell_number():
    for i,pair in enumerate(list(SpellNumber.initialize_spelling_hash().items())[:21]):
        assert SpellNumber(i).spelling == pair[1]

    assert SpellNumber(0).spelling == "zero"
    assert SpellNumber(123).spelling == "one hundred twenty three"
    assert SpellNumber(-123).spelling == "negative one hundred twenty three"
    assert SpellNumber(45.67).spelling == "forty five point six seven"
    assert SpellNumber(10001).spelling == "ten thousand one"
