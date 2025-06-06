import sys
from pathlib import Path
from unittest.mock import patch, Mock

import pytest

# Allow importing modules from the project root
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from step3_get_response import get_response


def test_get_response_returns_expected_text():
    sample_json = {
        "id": "resp_123",
        "output_text": "Hello world",
    }
    mock_resp = Mock()
    mock_resp.json.return_value = sample_json
    with patch("step3_get_response.requests.post", return_value=mock_resp):
        text, resp_id = get_response("hello")
    assert text == "Hello world"
    assert resp_id == "resp_123"
