#!/usr/bin/env python3
"""uploadfly.py
        declares `UploadflyClient` class
"""
import os
import io

import requests

from .utils.types import File


class UploadflyClient:
    """Uploadfly SDK client"""

    BASE_URL = "https://api.uploadfly.cloud"

    def __init__(self, api_key: str) -> None:
        """Initialize Uploadfly client

        Args:
            api_key (str): API key gotten from user dashboard

        Raises:
            Exception: If API key is not passed
        """
        if not api_key:
            raise Exception("An API key is required.")
        self.api_key = api_key

    def upload(self, file: File, filename: str = None):
        """Upload file to uploadfly

        Args:
            file (File): file to be uploaded. Can be a string(path to file) or a BufferedReader``
            filename (string): custom name of file

        Raises:
            Exception: If file not passed
            Exception: If file path passed does not exist
            Exception: If filename passed and filename is not a string
            Exception: If file upload failed

        Returns:
            response: Response object from file upload
        """
        if not file:
            raise Exception("A file is required.")
        if not isinstance(file, str) and not isinstance(file, io.BufferedReader):
            raise Exception("File must be a string or BufferedReader")
        if isinstance(file, str):
            if not os.path.exists(file):
                raise Exception("File Does not exist.")
            file = open(file, "rb")
        if filename and not isinstance(filename, str):
            file.close()
            raise Exception("filename must be of type string")
        filename = filename or file.name
        files = {"file": (filename, file), "filename": (None, filename)}
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.post(
                f"{self.BASE_URL}/upload", files=files, headers=headers
            )
            file.close()
            if not response.ok:
                raise Exception(f"{filename} failed to upload")
            return response.json()
        except Exception as e:
            raise Exception(f"An error occurred during file upload. {str(e)}")

    def delete(self, file_url: str):
        """delete file

        Args:
            file_url (str): File url

        Raises:
            Exception: If file url is not provided
            Exception: If file url is not a string
            Exception: If an error occurred during file deletion

        Returns:
            response: Response object
        """
        if not file_url:
            raise Exception("A file url must be provided")
        if not isinstance(file_url, str):
            raise Exception("file_url must be of type string")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {"file_url": file_url}
        try:
            response = requests.delete(
                f"{self.BASE_URL}/delete", json=data, headers=headers
            )
            if not response.ok:
                raise Exception(f"Failed to delete {file_url}")
            return response.json()
        except Exception as e:
            raise Exception(f"An error occurred during file deletion. {str(e)}")

    def image_upload(
        self,
        file: File,
        filename: str = None,
        max_file_size: str = None,
        width: int = None,
        height: int = None,
    ):
        """Image upload

        Args:
            file (File): file to upload
            filename (string): file name
            max_file_size (string): max file size
            width (int): width
            height (int): height

        Raises:
            Exception: If file is not passed
            Exception: If file path passed does not exist
            Exception: If optional arguments are not passed in the correct type
            Exception: An error occurred during image upload

        Returns:
            response: Response object
        """
        if not file:
            raise Exception("A file is required.")
        if not isinstance(file, str) and not isinstance(file, io.BufferedReader):
            raise Exception("File must be a string or BufferedReader")
        if isinstance(file, str):
            if not os.path.exists(file):
                raise Exception("File Does not exist.")
            file = open(file, "rb")
        if filename and not isinstance(filename, str):
            file.close()
            raise Exception("filename must be of type string")
        if max_file_size and not isinstance(max_file_size, str):
            file.close()
            raise Exception("max_file_size must be of type string")
        if width and not isinstance(width, int):
            file.close()
            raise Exception("width must be of type int")
        if height and not isinstance(height, int):
            file.close()
            raise Exception("height must be of type int")
        filename = filename or file.name
        max_file_size = max_file_size or ""
        width = width or ""
        height = height or ""
        files = {
            "file": (filename, file),
            "filename": (None, filename),
            "maxFileSize": (None, max_file_size),
            "width": (None, width),
            "height": (None, height),
        }
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.post(
                f"{self.BASE_URL}/image/upload", files=files, headers=headers
            )
            file.close()
            if not response.ok:
                raise Exception(f"{filename} failed to upload")
            return response.json()
        except Exception as e:
            raise Exception(f"An error occurred during file upload. {str(e)}")
