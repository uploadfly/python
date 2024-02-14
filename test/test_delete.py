import unittest
from unittest.mock import patch, Mock
from uploadfly import UploadflyClient


class TestUploadflyClientDelete(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = UploadflyClient("api-key")

    def test_raises_error_on_bad_arguments(self):
        with self.assertRaises(Exception):
            self.client.delete()
        with self.assertRaises(Exception):
            self.client.delete("")
        with self.assertRaises(Exception):
            self.client.delete(222)

    @patch("uploadfly.uploadfly.requests.delete")
    def test_delete(self, mock_request_delete: Mock):
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "success": True,
            "status": 200,
            "data": {"message": "File deleted successfully"},
        }
        mock_request_delete.return_value = mock_response

        response = self.client.delete("file-url")

        assert mock_request_delete.called
        self.assertEqual(mock_response.json(), response)

        mock_response.ok = False

        with self.assertRaises(Exception):
            self.client.delete("")


if __name__ == "__main__":
    unittest.main()
