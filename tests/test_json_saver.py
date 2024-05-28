# test_save_to_json.py
import json
from unittest.mock import mock_open, patch
import pytest
from proto_rag.utils.json_saver import save_to_json

@pytest.mark.parametrize("data, expected_output", [
    ({"key": "value"}, '{\n    "key": "value"\n}'),
    ([1, 2, 3], '[\n    1,\n    2,\n    3\n]'),
    ("string", '"string"'),
    (123, '123')
])
def test_save_to_json(data, expected_output):
    mock = mock_open()
    with patch("builtins.open", mock):
        save_to_json(data, "dummy_path.json")
        
    mock.assert_called_once_with("dummy_path.json", 'w')
    handle = mock()
    
    # Combine all the write calls into a single string
    written_content = ''.join(call.args[0] for call in handle.write.mock_calls)
    
    assert written_content == expected_output
