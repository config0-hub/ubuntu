def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname")

    # Add host group
    stack.add_hostgroups("config0-hub:::ubuntu::18.04-docker","install_docker")

    # Initialize 
    stack.init_variables()
    stack.init_hostgroups()

    # install docker
    kwargs = {"display":True}
    kwargs["human_description"] = "Install Docker on hostname {}".format(stack.hostname)
    kwargs["automation_phase"] = "infrastructure"
    kwargs["hostname"] = stack.hostname
    kwargs["groups"] = stack.install_docker
    stack.add_groups_to_host(**kwargs)

    return stack.get_results()
