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

"""Ansible 2 ServerSpec main application entry point."""

from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from cement.core.exc import FrameworkError, CaughtSignal
from ansible2serverspec.core import exc

# Application default.  Should update config/ansible2serverspec.conf to reflect any
# changes, or additions here.
defaults = init_defaults('ansible2serverspec')

# All internal/external plugin configurations are loaded from here
defaults['ansible2serverspec']['plugin_config_dir'] = '/etc/ansible2serverspec/plugins.d'

# External plugins (generally, do not ship with application code)
defaults['ansible2serverspec']['plugin_dir'] = '/var/lib/ansible2serverspec/plugins'

# External templates (generally, do not ship with application code)
defaults['ansible2serverspec']['template_dir'] = '/var/lib/ansible2serverspec/templates'

# Ansible playbook default parameters
defaults['ansible2serverspec']['playbook']  = 'site.yml'
defaults['ansible2serverspec']['inventory'] = 'hosts'

class A2SSApp(CementApp):
    class Meta:
        label = 'ansible2serverspec'
        config_defaults = defaults

        # All built-in application bootstrapping (always run)
        bootstrap = 'ansible2serverspec.cli.bootstrap'

        # Internal plugins (ship with application code)
        plugin_bootstrap = 'ansible2serverspec.cli.plugins'

        # Internal templates (ship with application code)
        template_module = 'ansible2serverspec.cli.templates'

        # call sys.exit() when app.close() is called
        exit_on_close = True


class A2SSTestApp(A2SSApp):
    """A test app that is better suited for testing."""
    class Meta:
        # default argv to empty (don't use sys.argv)
        argv = []

        # don't look for config files (could break tests)
        config_files = []

        # don't call sys.exit() when app.close() is called in tests
        exit_on_close = False

        extensions = ['argcomplete']


# Define the applicaiton object outside of main, as some libraries might wish
# to import it as a global (rather than passing it into another class/func)
app = A2SSApp()

def main():
    with app:
        try:
            app.run()

        except exc.A2SSError as e:
            # Catch our application errors and exit 1 (error)
            print('A2SSError > %s' % e)
            app.exit_code = 1

        except FrameworkError as e:
            # Catch framework errors and exit 1 (error)
            print('FrameworkError > %s' % e)
            app.exit_code = 1

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('CaughtSignal > %s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
