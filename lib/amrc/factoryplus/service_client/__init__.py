# Factory+ Python client library
# Service Client
# Copyright 2023 AMRC

from    functools       import cached_property

from    .directory      import Directory
from    .discovery      import Discovery
from    .http           import HTTP

class ServiceClient:
    def __init__ (self, **opts):
        self.opts = opts

    @cached_property
    def directory (self):
        return Directory(self)

    @cached_property
    def discovery (self):
        return Discovery(self)

    @cached_property
    def http (self):
        return HTTP(self)
