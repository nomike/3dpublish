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

import requests
from core.model import Design
from plugins.base import DestinationPlugin, SourcePlugin

class ThingiverseBase:
    """Shared functionality for Thingiverse operations"""
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.thingiverse.com"

    def _make_request(self, endpoint):
        # shared request logic
        pass

    def _convert_to_design(self, api_data):
        # shared conversion logic
        pass

class ThingiverseSource(ThingiverseBase, SourcePlugin):
    name = "thingiverse"

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.thingiverse.com"

    def read_design(self, thing_id) -> Design:
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(f"{self.base_url}/things/{thing_id}", headers=headers)
        response.raise_for_status()

        thing_data = response.json()
        design = Design()

        # Map Thingiverse fields to our canonical model
        design.name = thing_data.get("name")
        design.description = thing_data.get("description")
        # ... map other fields

        # Store platform-specific data
        design.thingiverse_metadata = {
            "license": thing_data.get("license"),
            "details": thing_data.get("details"),
            # etc.
        }

        return design


class ThingiverseDestination(ThingiverseBase, DestinationPlugin):
    # Similar structure but for writing data
    pass
