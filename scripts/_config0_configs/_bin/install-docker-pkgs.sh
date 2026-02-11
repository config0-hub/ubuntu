#!/bin/bash
#
# Docker Installation Script
#
# This script updates package lists and installs Docker and related tools
# on Debian/Ubuntu systems. It exits with error code 9 if the installation fails.
#

# Update package lists
apt-get update -y 

# Install Docker and related packages
apt-get install gnupg2 pass docker.io docker-compose -y || exit 9