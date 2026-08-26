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

    # instantiate authoring stack
    stack = newStack(stackargs)

    # add default variables
    stack.parse.add_required(key="hostname",
                             types="str")

    # selects the ssm_ec2_exec_eventbridge install the host order runs through
    stack.parse.add_required(key="install_name",
                             types="str")

    # add host group
    stack.add_hostgroups("config0-hub:::ubuntu::docker", "install_docker")

    # Initialize
    stack.init_variables()
    stack.init_hostgroups()

    # install docker on the host
    inputargs = {
        "display": True,
        "human_description": f"Install Docker on host {stack.hostname}",
        "automation_phase": "infrastructure",
        "hostname": stack.hostname,
        "install_name": stack.install_name,
        "groups": stack.install_docker
    }
    stack.add_groups_to_host(**inputargs)

    return stack.get_results()
