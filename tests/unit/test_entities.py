import unittest

from entities.greeting import Greeting


class TestGreetingEntity(unittest.TestCase):
    def test_default_message(self):
        greeting = Greeting()
        self.assertEqual(greeting.as_text(), "Hello World")

    def test_empty_message_falls_back_to_default(self):
        greeting = Greeting(message="   ")
        self.assertEqual(greeting.as_text(), "Hello World")


if __name__ == "__main__":
    unittest.main()
