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

# Standard Ansible default values as defined by the Ansible API.
from ansible.constants import \
    DEFAULT_ASK_PASS, \
    DEFAULT_ASK_VAULT_PASS, \
    DEFAULT_BECOME, \
    DEFAULT_BECOME_ASK_PASS, \
    DEFAULT_BECOME_METHOD, \
    DEFAULT_BECOME_USER, \
    DEFAULT_FORKS, \
    DEFAULT_HOST_LIST, \
    DEFAULT_PRIVATE_KEY_FILE, \
    DEFAULT_REMOTE_USER, \
    DEFAULT_SUBSET, \
    DEFAULT_TRANSPORT, \
    DEFAULT_VAULT_PASSWORD_FILE

# Additional defaults used by playbooks, that don't exist as constants within the Ansible API.
DEFAULT_LIMIT = None
DEFAULT_EXTRA_VARS = {}
DEFAULT_FLUSH_CACHE = False
DEFAULT_INVENTORY = '/etc/ansible/hosts'
DEFAULT_MODULE_PATH = None
DEFAULT_SKIP_TAGS = None
DEFAULT_TAGS = None
DEFAULT_CONNECTION_TIMEOUT = 10
DEFAULT_SSH_COMMON_ARGS = None
DEFAULT_SFTP_EXTRA_ARGS = None
DEFAULT_SSH_EXTRA_ARGS = None
DEFAULT_SCP_EXTRA_ARGS = None

DEFAULT_OUTPUT_LOCATION = None
