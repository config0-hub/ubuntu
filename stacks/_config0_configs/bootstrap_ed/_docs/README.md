# Host Add and Bootstrap

## Description
This stack adds a host to the config0 engine and performs host bootstrapping operations. It enables seamless integration of standalone hosts into the Config0 platform.

## Variables

### Required Variables
| Name | Description | Default |
|------|-------------|---------|
| hostname | Server hostname | &nbsp; |

### Optional Variables
| Name | Description | Default |
|------|-------------|---------|
| ssh_key_name | Name label for SSH key | null |
| ip_key | Configuration for ip key | public_ip |
| user | Configuration for user | ubuntu |

## Dependencies

The code doesn't contain any explicit dependencies (substacks, execgroups, or shelloutconfigs).

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