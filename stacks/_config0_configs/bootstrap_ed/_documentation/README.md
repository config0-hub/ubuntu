# Host Add and Bootstrap

## Description
This stack adds a host to the config0 engine and performs host bootstrapping operations. It enables seamless integration of standalone hosts into the Config0 platform.

## Variables

### Required Variables
| Name | Description | Default |
|------|-------------|---------|
| hostname | Server hostname |  |

### Optional Variables
| Name | Description | Default |
|------|-------------|---------|
| ssh_key_name | Name label for SSH key | null |
| ip_key | Configuration for ip key | public_ip |
| user | Configuration for user | ubuntu |

## Features
- Host registration with Config0 platform
- Host bootstrapping process 
- Support for custom SSH key configuration
- IP address specification for connectivity

### Builtin Commands
- host add
- host bootstrap

## License
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.