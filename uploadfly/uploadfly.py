#!/usr/bin/env python3
"""uploadfly.py
        declares `UploadflyClient` class
"""
import os

import requests

from utils.types import UploadConfig, ImageUploadConfig, File


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

    def upload(self, file: File, config: UploadConfig = {}):
        """Upload file to uploadfly

        Args:
            file (File): file to be uploaded. Can be a string(path to file) or a ReadableBuffer``
            config (`{ "filename": "filename" }`, optional): Config dictionary. Defaults to {}.

        Raises:
            Exception: If file not passed
            Exception: If file path passed does not exist
            Exception: If file upload failed

        Returns:
            response: Response object from file upload
        """
        if not file:
            raise Exception("A file is required.")
        if isinstance(file, str):
            if not os.path.exists(file):
                raise Exception("File Does not exist.")
            file = open(file, "rb")
        filename = config.get("filename", file.name)
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
            raise Exception(f"An error occurred during file upload. {e.message}")

    def delete(self, file_url: str):
        """delete file

        Args:
            file_url (str): File url

        Raises:
            Exception: If file url is not provided
            Exception: If an error occurred during file deletion

        Returns:
            response: Response object
        """
        if not file_url:
            raise Exception("A file url must be provided")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        data = {"file_url": file_url}
        try:
            response = requests.delete(
                f"{self.BASE_URL}/delete", data=data, headers=headers
            )
            if not response.ok:
                raise Exception(f"Failed to delete {file_url}")
            return response.json()
        except Exception as e:
            raise Exception(f"An error occurred during file deletion. {e.message}")

    def image_upload(self, file: File, config: ImageUploadConfig = {}):
        """Image upload

        Args:
            file (File): file to upload
            config (ImageUploadConfig, optional): has properties like: filename, maxFileSize, width, height. Defaults to {}.

        Raises:
            Exception: If file is not passed
            Exception: If file path passed does not exist
            Exception: An error occurred during image upload

        Returns:
            response: Response object
        """
        if not file:
            raise Exception("A file is required.")
        if isinstance(file, str):
            if not os.path.exists(file):
                raise Exception("File Does not exist.")
            file = open(file, "rb")
        filename = config.get("filename", file.name)
        max_file_size = config.get("max_file_size", "")
        width = config.get("width", "").__str__()
        height = config.get("height", "").__str__()
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
            raise Exception(f"An error occurred during file upload. {e.message}")
