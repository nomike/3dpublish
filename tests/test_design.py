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

import copy

import pytest

from core.design import Design


@pytest.fixture
def design():
    # Create a sample design
    design = Design()
    design.name = "Test Design"
    design.category = "Household"
    design.description = "A test design"
    design.license = "cc-by-nc"
    design.is_wip = True
    design.tags = ["test", "design"]
    design.authors = ["Author1", "Author2"]
    design.created_date = "2023-01-01"
    design.modified_date = "2023-01-02"
    design.thingiverse_id = "123456"
    return design


class TestDesign:
    def test_compare(self, design):
        new_design = copy.deepcopy(design)
        assert design == new_design
