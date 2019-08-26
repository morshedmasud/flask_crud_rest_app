## Start using virtualenv

``` bash
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