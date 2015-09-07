# Wording

## How to use
```bash
# Start api server and web server
./start_all.sh

# Use servers
open http://127.0.0.1:5001/cor
curl http://127.0.0.1:5000/cor

# Stop api server and web server
./stop_all.sh
```



#### How to only use api
```bash
cd api
./initialize.sh
python3 api.py 

# In another terminal window
curl http://127.0.0.1:5000/cor
```

#### How to only use web
```bash
# Start api server first
cd web
. ../api/env/bin/activate
python3 site.py

# Go to site
open http://127.0.0.1:5001/
```

#### How to only use login
```bash
cd login
./create-env.sh
python main.py
```

## How to use the login system in API
```bash
# First start the api
cd api
./initialize.sh
python3 api.py

# For registering users, do:
curl -i -X POST -H "Content-Type: application/json" -d '{"username":"username","password":"password","email":"valid_email"}' http://127.0.0.1:5000/register

# For Viewing your lists, do:
curl -u username:password -i -X GET http://127.0.0.1:5000/username
```