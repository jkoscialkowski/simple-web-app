#!/usr/bin/env bash
sudo apt-get update

# Install Python
sudo apt-get install python-pip python-dev build-essential

# Install NGINX
sudo apt-get install nginx

# Copy the NGINX conf file and restart NGINX
sudo cp nginx.conf /etc/nginx/
sudo service restart nginx