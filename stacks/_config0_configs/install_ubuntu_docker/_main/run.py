def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname")

    # Add host group
    stack.add_hostgroups("config0-publish:::ubuntu::18.04-docker",
                         "install_docker")

    # Initialize 
    stack.init_variables()
    stack.init_hostgroups()

    # install docker
    human_description = "Install Docker on hostname {}".format(stack.hostname)
    inputargs = {"display": True,
                 "human_description": human_description,
                 "automation_phase": "infrastructure",
                 "hostname": stack.hostname,
                 "groups": stack.install_docker}

    stack.add_groups_to_host(**inputargs)

    return stack.get_results()
