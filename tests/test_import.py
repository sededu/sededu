import pytest

import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

def test_import():
    from sededu.root import Runner

def test_readme_parsed_file_exists():
    assert os.path.isfile(os.path.join('sededu', '_readme.json'))
