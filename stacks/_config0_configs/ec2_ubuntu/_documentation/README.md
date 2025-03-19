# AWS EC2 Server with Bootstrap

## Description
Creates an AWS EC2 server instance and optionally bootstraps it for remote execution with Config0.

## Variables

### Required Variables

| Name | Description | Default |
|------|-------------|---------|
| hostname | Server hostname | |
| ssh_key_name | Name label for SSH key | |
| aws_default_region | Default AWS region | us-east-1 |
| bootstrap_for_exec | 99checkme99 Configures whether to bootstrap the server for remote execution | true |

### Optional Variables

| Name | Description | Default |
|------|-------------|---------|
| config_network | Configuration for config network (choices: private, public) | public |
| sg_id | Security group ID | |
| security_group_ids | Security group ID list | |
| subnet_ids | Subnet ID list | |
| iam_instance_profile | IAM instance profile | |
| ami | AMI ID | |
| ami_filter | AMI filter criteria | |
| ami_owner | AMI owner ID | |
| instance_type | EC2 instance type | t3.micro |
| disksize | Disk size in GB | 20 |
| disktype | Configuration for disktype | |
| ip_key | Configuration for ip key | public_ip |
| volume_name | Storage volume name | |
| volume_size | Storage volume size (GB) | |
| volume_mountpoint | Volume mount path | |
| volume_fstype | Volume filesystem type | |
| cloud_tags_hash | Resource tags for cloud provider | |
| user | Configuration for user | ubuntu |

## Features
- Creates an EC2 instance with specified configurations
- Supports custom AMI selection
- Configurable instance type, disk size, and networking options
- Optional bootstrapping for remote execution
- Support for attaching additional volumes

## Dependencies

### Substacks
- [config0-publish:::bootstrap_ed](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/bootstrap_ed)
- [config0-publish:::aws_ec2_server](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/aws_ec2_server)

## License
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.