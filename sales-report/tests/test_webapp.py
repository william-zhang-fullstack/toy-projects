import os
import sys


webapp_path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(webapp_path)


def test_app_exists():
    from webapp import app

def test_dummy():
    assert 1 + 1 == 2
