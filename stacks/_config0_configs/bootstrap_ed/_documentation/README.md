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

### Execgroups
- [config0-publish:::github::lambda_trigger_stepf](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/exec/groups/config0-publish/github/lambda_trigger_stepf/default)

### Shelloutconfigs
- [config0-publish:::terraform::resource_wrapper](http://config0.http.redirects.s3-website-us-east-1.amazonaws.com/assets/shelloutconfigs/config0-publish/terraform/resource_wrapper/default)

## License
<pre>
Copyright (C) 2025 Gary Leong <gary@config0.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
</pre>