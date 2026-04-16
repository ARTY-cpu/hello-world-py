import unittest

from services.greeting_service import GreetingService


class TestGreetingService(unittest.TestCase):
    def test_get_greeting_text_returns_default_value(self):
        service = GreetingService()
        self.assertEqual(service.get_greeting_text(), "Hello World")


if __name__ == "__main__":
    unittest.main()
