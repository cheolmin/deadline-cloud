# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

"""
This file makes "python -m deadline ..." equivalent to "deadline ..."
"""
import sys
from .client.cli import main

from typing import Dict as dict
from typing import List as list
# Override the program name to always be "deadline"
sys.exit(main())
