import pytest
import yaml
from typographeur import typographeur



with open("tests_contexte.yaml") as f:
    tests = yaml.safe_load(f)


# The x.values() rely on the fact that with python3.7+ dictionary keep
# insertion order, in order to have input equal to the value
# associated with the key "input", and similarly for "expected".
@pytest.mark.parametrize("input,expected", [x.values() for x in tests])
def tests_yaml(input, expected):
    output = typographeur(input)
    assert output == expected
