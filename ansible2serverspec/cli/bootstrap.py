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

"""Ansible 2 ServerSpec bootstrapping."""

# All built-in application controllers should be imported, and registered
# in this file in the same way as A2SSBaseController.

from ansible2serverspec.cli.controllers.base import A2SSBaseController

def load(app):
    app.handler.register(A2SSBaseController)
