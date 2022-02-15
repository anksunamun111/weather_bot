import unittest

class TgBotTests(unittest.TestCase):

    def test_d(self):
        from wbot import f
        self.assertEqual(f(), 2)

if __name__ == "__main__":
    unittest.main()

