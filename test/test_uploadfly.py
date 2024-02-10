import unittest
from uploadfly import UploadflyClient


class TestUploadflyClient(unittest.TestCase):

    def test_client_creation(self):
        with self.assertRaises(Exception):
            UploadflyClient()
        UploadflyClient("api-key")


if __name__ == "__main__":
    unittest.main()
