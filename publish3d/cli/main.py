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
"""
Usage:
    publish3d sync <source> <source_id> <dest>
    publish3d sync -h | --help
    publish3d sync --version
"""
import docopt

# from core.engine import DesignSyncEngine

# from publish3d.plugins.thingiverse import ThingiverseSource
# from publish3d.plugins.printables import PrintablesDestination


def sync(source, source_id, dest):
    pass
    # engine = DesignSyncEngine()
    # engine.register_plugin(ThingiverseSource(API_KEY))
    # engine.register_plugin(PrintablesDestination(API_KEY))

    # new_id = engine.sync_design(source, source_id, dest)
    # print(f"Design synced to {dest} with ID {new_id}")


if __name__ == "__main__":
    arguments = docopt.docopt(__doc__, version="Publish3D CLI 1.0")
    # sync()
