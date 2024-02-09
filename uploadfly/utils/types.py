#!/usr/bin/env python3
"""Types for uploadfly client
"""
from typing import TypeAlias, Union
import io


File: TypeAlias = Union[io.BufferedReader, str]
