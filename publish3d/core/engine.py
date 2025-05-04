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

from plugins import DestinationPlugin, FileHandlerPlugin, SourcePlugin


class Engine:
    def __init__(self):
        self.source_plugins = {}
        self.destination_plugins = {}
        self.file_handlers = []

    def register_plugin(self, plugin):
        if isinstance(plugin, SourcePlugin):
            self.source_plugins[plugin.name] = plugin
        elif isinstance(plugin, DestinationPlugin):
            self.destination_plugins[plugin.name] = plugin
        elif isinstance(plugin, FileHandlerPlugin):
            self.file_handlers.append(plugin)
        else:
            raise ValueError(
                f"Invalid type of plugin: {type(plugin)}. Must be SourcePlugin, DestinationPlugin, or FileHandlerPlugin."
            )

    def sync_design(self, source_name, source_id, dest_name):
        source = self.source_plugins[source_name]
        destination = self.destination_plugins[dest_name]

        design = source.read_design(source_id)
        return destination.write_design(design)

    def update_design(self, source_name, source_id, dest_name, dest_id):
        source = self.source_plugins[source_name]
        destination = self.destination_plugins[dest_name]

        design = source.read_design(source_id)
        return destination.update_design(dest_id, design)
