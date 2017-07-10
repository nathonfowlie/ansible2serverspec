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

"""Testing utilities for Ansible 2 ServerSpec."""

from ansible2serverspec.cli.main import A2SSTestApp
from cement.utils.test import *

class A2SSTestCase(CementTestCase):
    app_class = A2SSTestApp

    def setUp(self):
        """Override setup actions (for every test)."""
        super(A2SSTestCase, self).setUp()

    def tearDown(self):
        """Override teardown actions (for every test)."""
        super(A2SSTestCase, self).tearDown()

