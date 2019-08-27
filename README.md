## Python 3.6 install

 ``` bash
$ sudo apt-get update
$ sudo apt-get install python3.6

# pip3 Install 
$ sudo apt-get -y install python3-pip

# Install Virtualenv
$ sudo pip3 install virtualenv

```



## Start using virtualenv

``` bash
# Make virtualenv
$ virtualenv -p python3.6 venv

# Activate venv
$ source venv/bin/activate

# Install dependencies
$ pip3 install requirements.txt

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
```

## Endpoints

* GET     /app
* POST    /app
* PUT     /app/:id
* DELETE  /app/:id


### Header
Content-Type:   application/json

token: