"""
# Copyright (C) 2025 Gary Leong <gary@config0.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

def run(stackargs):

    stackargs["add_cluster"] = False
    stackargs["add_instance"] = False

    # instantiate stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname",
                             tags="host,bootstrap",
                             types="str")

    stack.parse.add_optional(key="ssh_key_name",
                             tags="host,bootstrap",
                             default="null",
                             types="str")

    stack.parse.add_optional(key="ip_key",
                             tags="bootstrap",
                             default="public_ip",
                             types="str")

    stack.parse.add_optional(key="user",
                             tags="bootstrap",
                             default="ubuntu",
                             types="str")

    # Initialize Variables in stack
    stack.init_variables()

    # register hostname as a host resource with config0
    stack.add_host(stack.hostname,
                   stack.ssh_key_name)

    # Bootstrap host to the config0 engine
    arguments = stack.get_tagged_vars(tag="bootstrap",
                                      output="dict")

    # ── CONFIG0-REWRITE · EXPECTED-BROKEN · EB-0001 ──────────────────────
    # host_bootstrap is REMOVED (obsolete): SSM auto-bootstraps the host, so
    # this SSH-enablement step is gone. Host execution moves to the onboarding
    # SSM Step Function (task-token output). Raises until removed.
    # Ref: current/expected-broken-registry.md#eb-0001
    # ─────────────────────────────────────────────────────────────────────
    stack.host_bootstrap(**arguments)

    return stack.get_results()
