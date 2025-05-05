# Copyright (c) 2025 nomike Postmann <nomike@nomike.com234>
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

import os

import pytest

from publish3d.core.design import Design
from publish3d.plugins.localdirectory import LocalDirectory


@pytest.fixture
def design():
    # Create a sample design
    design = Design()
    design.name = "test_design"
    design.description = "A test design"
    return design


class TestLocalDirectory:
    def test_read_and_write_design(self, tmp_path, design):
        os.makedirs(tmp_path, exist_ok=True)

        # Write the design to the directory
        local_dir = LocalDirectory(tmp_path)

        # Write the design to the directory
        local_dir = LocalDirectory(tmp_path)
        local_dir.write_design(design)

        # Read the design back from the directory
        read_design = local_dir.read_design()

        # Assert that the read design matches the original design
        assert design == read_design
