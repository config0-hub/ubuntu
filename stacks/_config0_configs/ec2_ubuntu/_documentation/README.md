# AWS EC2 Server with Bootstrap

## Description
Creates an AWS EC2 server instance and optionally bootstraps it for remote execution with Config0.

## Variables

### Required Variables

| Name | Description | Default |
|------|-------------|---------|
| hostname | Server hostname | &nbsp; |
| ssh_key_name | Name label for SSH key | &nbsp; |
| aws_default_region | Default AWS region | us-east-1 |
| bootstrap_for_exec | Configures whether to bootstrap the server for remote execution | true |

### Optional Variables

| Name | Description | Default |
|------|-------------|---------|
| config_network | Configuration for config network (choices: private, public) | public |
| sg_id | Security group ID | &nbsp; |
| security_group_ids | Security group ID list | &nbsp; |
| subnet_ids | Subnet ID list | &nbsp; |
| iam_instance_profile | IAM instance profile | &nbsp; |
| ami | AMI ID | &nbsp; |
| ami_filter | AMI filter criteria | &nbsp; |
| ami_owner | AMI owner ID | &nbsp; |
| instance_type | EC2 instance type | t3.micro |
| disksize | Disk size in GB | 20 |
| disktype | Configuration for disktype | &nbsp; |
| ip_key | Configuration for ip key | public_ip |
| volume_name | Storage volume name | &nbsp; |
| volume_size | Storage volume size (GB) | &nbsp; |
| volume_mountpoint | Volume mount path | &nbsp; |
| volume_fstype | Volume filesystem type | &nbsp; |
| cloud_tags_hash | Resource tags for cloud provider | &nbsp; |
| user | Configuration for user | ubuntu |

## Dependencies

### Substacks
- [config0-publish:::bootstrap_ed](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/bootstrap_ed)
- [config0-publish:::aws_ec2_server](https://api-app.config0.com/web_api/v1.0/stacks/config0-publish/aws_ec2_server)

## License
<pre>
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
</pre>