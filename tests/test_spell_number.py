import pytest
from spell_number.spell_number import SpellNumber

def test_spell_number():
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
