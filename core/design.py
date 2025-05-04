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


class Design:
    def __init__(self):
        # Core metadata
        self.name = None
        self.category = None
        self.description = None
        self.license = None
        self.is_wip = None
        self.tags = None
        self.authors = None
        self.created_date = None
        self.modified_date = None
        self.thingiverse_id = None

        # Content
        self.main_files = []  # STL, STEP, etc.
        self.images = []  # Renders, photos
        self.source_files = []  # CAD source files
        self.attachments = []  # Additional files

        # Platform-specific fields (stored as dicts to preserve structure)
        self.thingiverse_metadata = {}
        self.printables_metadata = {}

        # Common content that might be split differently across platforms
        self.print_settings = ""
        self.assembly_instructions = ""
        self.usage_instructions = ""

        # Relationships
        self.derivatives = []  # Links to other designs
        self.remixes = []  # Parent designs if this is a remix

    def __eq__(self, value):
        if not isinstance(value, Design):
            return NotImplemented
        return all(
            getattr(self, attr) == getattr(value, attr) for attr in self.__dict__.keys()
        )
