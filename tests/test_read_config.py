from src.config import Config
import pytest
import json
import os
import logging
import pdb
TEST_JSON_PATH = "test_config.json"

@pytest.fixture
def json_fixture():
    with open(TEST_JSON_PATH, "x") as fp:
        fp.write("{\"Test\" : 1}")
    yield
    os.remove(TEST_JSON_PATH)

def test_read_configs(json_fixture):
    logging.basicConfig(filename="out.log", filemode="w", level=logging.INFO)

    logging.info("creating config")
    c = Config(TEST_JSON_PATH)
    assert c.Test == 1