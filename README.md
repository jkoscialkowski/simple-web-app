# simple-web-app
An experimental repo for a simple web application + API with nginx, Flask, 
hosted on AWS EC2.

The Pokemon part uses a [dataset from Kaggle](
https://www.kaggle.com/rounakbanik/pokemon).

## How to launch?
Spin up some AWS instance and run
```bash
sudo init.sh
``` 

## Features

* Under `/` - text generated by the `static.html` file.
* Under `/app` - text generated by the Flask app running in the background.
* Under `/app/pokemon` - the REST API giving a Pokemon information for a 
    given number.