####################################################################################################
# Copyright 2017 Nathon Fowlie
#
# Licensed under the Apache License, Version 2.0(the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
#
# http: // www.apache.org / licenses / LICENSE - 2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
####################################################################################################

"""Ansible 2 ServerSpec exception classes."""

class A2SSError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg

class A2SSConfigError(A2SSError):
    """Config related errors."""
    pass

class A2SSRuntimeError(A2SSError):
    """Generic runtime errors."""
    pass

class A2SSArgumentError(A2SSError):
    """Argument related errors."""
    pass
