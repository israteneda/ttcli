from tests.data import constants
from tt.instructions import banner
from tt.instructions import usage
from tt.instructions import options
from tt.instructions import examples


def test_instructions__return_instructions__when_calling_the_banner_function():
    assert banner() == constants.banner


def test_instructions__return_usage__when_calling_the_usage_function():
    assert usage() == constants.usage


def test_instructions_return_options__when_calling_the_options_function():
    assert options() == constants.options


def test_instructions_return_examples__when_calling_the_examples_function():
    assert examples() == constants.examples



