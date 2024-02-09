#!/usr/bin/env python3
"""Types for uploadfly client
"""
from typing import TypedDict, TypeAlias, Union, Optional
import io


File: TypeAlias = Union[io.BufferedReader, str]


class UploadConfig(TypedDict):
    """Type for config argument for the upload function"""

    filename: Optional[str]


class ImageUploadConfig(TypedDict):
    """Type for config argument for the image upload function"""
    
    filename: Optional[str]
    max_file_size: Optional[str]
    width: Optional[int]
    height: Optional[int]
