import unittest
from code import get_schema


class TestGetSchema(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_get_schema(self):
        data = {
            "attributes": {
                "appName": "ABCDEFGHIJKLMNOPQRSTUVW",
                "eventType": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                "subEventType": "ABCDEFGHIJKLMNO",
                "sensitive": False
            },
            "message": {
                "user": {
                    "id": "ABCDEFGHIJKLMNOP",
                    "nickname": "ABCD",
                    "title": "ABCDEFGHIJKLMNOPQRSTUVWXYZABC",
                    "accountType": "ABCDEFGHIJKLMNOPQRSTUVWX",
                    "countryCode": "ABCDEFGHIJKLMNOPQRSTUVWX",
                    "orientation": "ABCDEFGHIJKLMNOPQRSTU"
                },
                "time": 890,
                "acl": [],
                "publicFeed": False,
                "internationalCountries": [
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
                    "ABCDEFGHIJKLMNOPQ",
                    "ABCDEFGHIJKLMNOPQRSTUVW",
                    "ABCDEFGHIJKLMNOPQRSTUVWXY",
                    "ABCDEFGHIJK",
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    "ABCDEFGHIJKLMNOPQR",
                    "ABCDEFG",
                    "ABCDEFGHIJKLM"
                ],
                "topTraderFeed": True
            }
        }
        schema = get_schema(data)
        expected_schema = {
            "user": {
                "type": "object",
                "properties": {
                    "id": {"type": "string", "description": "", "required": False},
                    "nickname": {"type": "string", "description": "", "required": False},
                    "title": {"type": "string", "description": "", "required": False},
                    "accountType": {"type": "string", "description": "", "required": False},
                    "countryCode": {"type": "string", "description": "", "required": False},
                    "orientation": {"type": "string", "description": "", "required": False}
                }
            },
            "time": {"type": "integer", "description": "", "required": False},
            "acl": {"type": "array", "description": "", "items": {"type": "string", "description": "", "required": False}},
            "publicFeed": {"type": "boolean", "description": "", "required": False},
            "internationalCountries": {"type": "array", "description": "", "items": {"type": "string", "description": "", "required": False}},
            "topTraderFeed": {"type": "boolean", "description": "", "required": False}
        }
        self.assertEqual(schema, expected_schema)

    def test_get_schema_empty_data(self):
        data = {}
        schema = get_schema(data)
        expected_schema = {}
        self.assertEqual(schema, expected_schema)


if __name__ == '__main__':
    unittest.main()
