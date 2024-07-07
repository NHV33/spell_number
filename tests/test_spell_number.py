import pytest
from spell_number.spell_number import SpellNumber

def test_digit_length():
    # Check that digit_length method produces the same output as len(string) for positive integers.
    for i in range(1000):
        assert SpellNumber.digit_length(i) == len(str(i))

def test_spell_number():
    for i,pair in enumerate(list(SpellNumber.initialize_spelling_hash().items())[:21]):
        assert SpellNumber(i).spelling == pair[1]

    assert SpellNumber(123).spelling == "one hundred twenty three"
    assert SpellNumber(0).spelling == "zero"
    assert SpellNumber(10001).spelling == "ten thousand one"
    assert SpellNumber(-123).spelling == "negative one hundred twenty three"
    assert SpellNumber(45.67).spelling == "forty five point six seven"

def test_initialize_spelling_hash():
    spelling_hash = SpellNumber.initialize_spelling_hash()
    assert spelling_hash[1] == "one"
    assert spelling_hash[20] == "twenty"

def test_generate_group_names():
    group_names = SpellNumber.generate_group_names()
    assert group_names[0] == ""
    assert group_names[1] == "thousand"
    assert "million" in group_names
