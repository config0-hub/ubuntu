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
    """Create and bootstrap an EC2 server instance."""

    # Do not add cluster and instance
    stackargs["add_cluster"] = False
    stackargs["add_instance"] = False

    # instantiate stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname",
                             tags="server,bootstrap",
                             types="str")

    stack.parse.add_required(key="ssh_key_name",
                             tags="server,bootstrap",
                             types="str")

    stack.parse.add_required(key="aws_default_region",
                             default="us-east-1",
                             tags="server",
                             types="str")

    stack.parse.add_required(key="bootstrap_for_exec",
                             types="bool",
                             default="true")

    stack.parse.add_optional(key="config_network",
                             choices=["private", "public"],
                             tags="server",
                             default="public")

    stack.parse.add_optional(key="sg_id",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="security_group_ids",  # csv format
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="subnet_ids",
                             tags="server",
                             types="str")

    # instance profile
    stack.parse.add_optional(key="iam_instance_profile",
                             tags="server",
                             types="str")

    # ami info
    stack.parse.add_optional(key="ami",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="ami_filter",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="ami_owner",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="instance_type",
                             tags="server",
                             types="str",
                             default="t3.micro")

    stack.parse.add_optional(key="disksize",
                             tags="server",
                             types="int",
                             default="20")

    stack.parse.add_optional(key="disktype",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="ip_key",
                             tags="bootstrap",
                             types="str",
                             default="public_ip")

    # extra disk
    stack.parse.add_optional(key="volume_name",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="volume_size",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="volume_mountpoint",
                             tags="server",
                             types="str")

    stack.parse.add_optional(key="volume_fstype",
                             tags="server",
                             types="str")

    # tags and labels
    stack.parse.add_optional(key="cloud_tags_hash",
                             tags="server,bootstrap",
                             types="str")

    stack.parse.add_optional(key="user",
                             tags="bootstrap",
                             default="ubuntu",
                             types="str")

    # Add substacks
    stack.add_substack("config0-publish:::bootstrap_ed")
    stack.add_substack("config0-publish:::aws_ec2_server")  # use terraform

    # init the stack namespace
    stack.init_variables()
    stack.init_substacks()

    arguments = stack.get_tagged_vars(tag="server",
                                      output="dict")

    arguments["timeout"] = 600

    human_description = "Instruction: Creates a Server on Ec2"
    inputargs = {
        "arguments": arguments,
        "automation_phase": "infrastructure",
        "human_description": human_description
    }

    stack.aws_ec2_server.insert(display=None,
                                **inputargs)

    # this will register server as a host for remote execution
    if stack.get_attr("bootstrap_for_exec"):
        # Call to bootstrap_ed to config0
        arguments = stack.get_tagged_vars(tag="bootstrap",
                                          output="dict")

        inputargs = {
            "arguments": arguments,
            "automation_phase": "infrastructure",
            "human_description": "Bootstraps host to Jiffy database"
        }

        stack.bootstrap_ed.insert(display=None,
                                  **inputargs)

    return stack.get_results()