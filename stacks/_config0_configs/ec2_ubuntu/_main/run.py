def run(stackargs):

    import random

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
                             choices=["private","public"],
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

    # spot request
    stack.parse.add_optional(key="spot",
                             types="bool")

    stack.parse.add_optional(key="spot_max_price",
                             types="float")

    stack.parse.add_optional(key="spot_type",
                             types="str",
                             default="persistent")

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
    stack.add_substack("config0-publish:::ec2_server")  # use shellout/boto3 since spot required
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
        "automation_phase":"infrastructure",
        "human_description": human_description
    }

    # spot uses boto shellout
    if stack.get_attr("spot"):
        inputargs["arguments"]["spot"] = "True"
        inputargs["arguments"]["spot_type"] = stack.spot_type
        if stack.get_attr("spot_max_price"):
            inputargs["arguments"]["spot_max_price"] = stack.spot_max_price
        stack.ec2_server.insert(display=None,
                                **inputargs)
    # non-spot, uses terraform
    else:
        stack.aws_ec2_server.insert(display=None,
                                    **inputargs)

    # this will register server as a host for remote execution
    if stack.get_attr("bootstrap_for_exec"):

        # Call to bootstrap_ed to config0
        arguments = stack.get_tagged_vars(tag="bootstrap",
                                          output="dict")

        inputargs = {
            "arguments": arguments,
            "automation_phase":"infrastructure",
            "human_description": "Bootstraps host to Jiffy database"
        }

        stack.bootstrap_ed.insert(display=None,
                                  **inputargs)

    return stack.get_results()