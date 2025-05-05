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

# encoding: utf-8

import json
import os
from typing import Dict, List, Union

from core.design import Design
from plugins.base import Plugin


class LocalDirectory(Plugin):
    """Plugin for importing and exporting designs from a local directory."""

    _MAPPING_FIELDS = {
        "name": ("thing", "name"),
        "category": ("thing", "category"),
        "description": ("thing", "description"),
        "authors": ("thing", "authors"),
        "license": ("thing", "license"),
        "tags": ("thing", "tags"),
        "is_wip": ("thing", "is_wip"),
    }

    _MAPPING_LICENSES = {
        "cc-by-nc": "cc-by-nc",
        "cc-by": "cc-by",
        "cc-by-nc-sa": "cc-by-nc-sa",
        "cc-by-sa": "cc-by-sa",
        "cc0": "cc0",
        "gpl": "gpl",
        "mit": "mit",
        "apache": "apache",
    }

    __CONFIG_FILENAME = ".thingiverse_publisher.json"

    def __init__(self, design_id: str):
        super().__init__()
        self.directory = design_id

    def read_design(self) -> Design:

        with open(
            os.path.join(self.directory, LocalDirectory.__CONFIG_FILENAME), "r"
        ) as f:
            design_data = json.load(f)

        design = Design()

        for design_property, json_path in LocalDirectory._MAPPING_FIELDS.items():
            try:
                value = design_data[json_path[0]][json_path[1]]
                setattr(design, design_property, value)
            except KeyError:
                pass

        return design

    def write_design(self, design: Design) -> None:
        design_data: Dict[str, Union[str, Dict, List]] = {}

        for design_property, json_path in LocalDirectory._MAPPING_FIELDS.items():
            value = getattr(design, design_property)

            def set_nested_value(data, path, value):
                if len(path) == 1:
                    data[path[0]] = value
                    return

                if path[0] not in data:
                    data[path[0]] = {}

                set_nested_value(data[path[0]], path[1:], value)

            set_nested_value(design_data, json_path, value)

            with open(
                os.path.join(self.directory, LocalDirectory.__CONFIG_FILENAME), "w"
            ) as f:
                json.dump(design_data, f, indent=4)
