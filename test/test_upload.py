import unittest
from unittest.mock import patch, Mock
from uploadfly import UploadflyClient


class TestUploadflyClientUpload(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = UploadflyClient("api-key")

    def test_raises_error_on_bad_arguments(self):
        with self.assertRaises(Exception):
            self.client.upload()
        with self.assertRaises(Exception):
            self.client.upload("")
        with self.assertRaises(Exception):
            self.client.upload(222)
        with self.assertRaises(Exception):
            self.client.upload("none-existent.file")

    @patch("uploadfly.uploadfly.requests.post")
    def test_upload(self, mock_request_post: Mock):
        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = {
            "success": True,
            "status": 201,
            "data": {
                "url": "https://cdn.uploadfly.cloud/Emmo00/custom-filename.plain",
                "path": "Emmo00/f2r5er-custom-filename.plain",
                "type": "text/plain",
                "size": "11.00 Bytes",
                "name": "custom-filename.plain",
            },
        }
        mock_request_post.return_value = mock_response

        file = open("test/testfile.txt", "rb")
        response = self.client.upload(file, filename="custom-filename")

        assert mock_request_post.called
        self.assertEqual(mock_response.json(), response)

        mock_response.ok = False

        with self.assertRaises(Exception):
            self.client.upload(file)


if __name__ == "__main__":
    unittest.main()
