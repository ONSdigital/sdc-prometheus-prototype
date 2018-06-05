import unittest
from monitor_me.app import app


class AppTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_root(self):
        res = self.app.get("/")
        self.assertEqual(res.data, b'Hello, World!')

    def test_metrics(self):
        res = self.app.get("/metrics")
        self.assertIsNotNone(res.data)