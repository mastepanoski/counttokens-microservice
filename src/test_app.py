from __future__ import absolute_import
import unittest
import json
from app import create_app
from endpoints import num_tokens_from_messages

class TestCountTokens(unittest.TestCase):
    def test_count_tokens(self):
        capp = create_app()
        with capp.test_client() as client:
            data = {
                "messages": [
                    {"role": "system", "content": "Test message 1."},
                    {"role": "system", "content": "Test message 2."}
                ],
                "model": "gpt-3.5-turbo-0301"
            }
            response = client.post(
                "/tokens/count",
                data=json.dumps(data),
                content_type="application/json"
            )
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)["total"], num_tokens_from_messages(data["messages"], data["model"]))


if __name__ == "__main__":
    unittest.main()
