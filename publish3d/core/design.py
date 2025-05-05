#!/usr/bin/env python3
# Copyright (c) 2025 nomike Postmann <nomike@nomike.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# -*- coding: utf-8 -*-

from datetime import datetime
from typing import Dict, List

import deepcompare


class Design:
    def __init__(self):
        self.name: str = None
        self.description: str = None
        self.category: str = None
        self.license: str = None
        self.is_wip: bool = None
        self.is_published: bool = None
        self.tags: str = None
        self.authors: str = None
        self.created_date: datetime = None
        self.modified_date: datetime = None
        self.ids: Dict[str, List[str]] = {}

        self.files: List[Dict[str, str]] = []

        self.platform_specific: Dict[str, Dict[str, str]] = {}

        self.print_settings: str = None
        self.assembly_instructions: str = None
        self.usage_instructions: str = None

        # Relationships
        self.remixes: List[str] = []  # Parent designs if this is a remix

    def __eq__(self, value) -> bool:
        if not isinstance(value, Design):
            return NotImplemented
        return all(
            deepcompare.compare(getattr(self, attr), getattr(value, attr))
            for attr in self.__dict__.keys()
        )
