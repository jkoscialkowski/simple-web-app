#!/usr/bin/env bash
sudo apt-get update

# Install Python
sudo apt-get install python3 python3-pip

# Create Flask environment, download packages
pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt

# Run the app
chmod a+x app.py
nohup ./app.py &

# Install NGINX
sudo apt-get install nginx

# Copy the NGINX conf file and restart NGINX
sudo cp nginx.conf /etc/nginx/
sudo service nginx restart