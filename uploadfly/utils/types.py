#!/usr/bin/env python3
"""Types for uploadfly client
"""
from typing import Union
import io


File = Union[io.BufferedReader, str]
