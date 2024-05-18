**Description**

  - This stack wrappers around Ec2 creation of Ubuntu instance
  - Optionally, we can bootstrap the Ubuntu instance to Config0 (Config0)

**Required**

| argument      | description                            | var type | default      |
| ------------- | -------------------------------------- | -------- | ------------ |
| hostname   | hostname of the ec2 server                 | string   | None         |
| ssh_key_name   | ssh_key_name for the ec2 server                 | string   | None         |
| aws_default_region   | default aws region               | string   | us-east-1         |

**Optional**

| argument           | description                                       | var type | default                                                   |
|--------------------|---------------------------------------------------| -------- |-----------------------------------------------------------|
| config_network     | the configuration network                         | choice public/private   | private                                                   |
| bootstrap_for_exec | bootstrap to Config0 for remote execution         | boolean   | True                                                      |
| sg_id              | the single security group id for the ec2 instance | string   | None                                                      |
| security_group_ids | the security group ids for the ec2 instance       | list   | None                                                      |
| subnet_ids         | the subnet_ids to select from                     | string (csv)    | None                                                      |
| ami   | the ami ami               | string   | None |
| ami_filter   | the AMI filter used for searches      | string       | ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-\*  | 
| ami_owner   | the AMI owner used for searches        | string    | 099720109477 (canonical) |
| instance_type               | the instance size                                 | string    | t2.micro                                                  |
| disksize           | the instance root disk size                       | string    | 40                                                        |
| disktype           | the instance root disk type                       | string    | None                                                      |
| ip_key             | the ip_key from boto used for connection          | public_ip/private_ip    | public_ip                                                 |
| volume_name        | the name of volume to be attached                 | string    | None                                                      |
| volume_size        | the size of volume to be created                  | string    | None                                                      |
| volume_mount       | the mount point of the extra volume               | string    | None                                                      |
| volume_fstype      | the fileystem of the extra volume                 | string    | None                                                      |
