import unittest

from controller.view_controller import GreetingController


class TestGreetingController(unittest.TestCase):
    def test_render_home_returns_utf8_bytes(self):
        controller = GreetingController()
        self.assertEqual(controller.render_home(), b"Hello World")


if __name__ == "__main__":
    unittest.main()
