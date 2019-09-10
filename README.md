# FLASK API - Logger
```
Takes in HTTP, shits out syslog
```

## Log Ingesting

- HTTP GET to endpoint /logs/pub for a list of acceptable values
- HTTP POST to Endpoint /logs/pub will take the values and push them to ur siem

## Building :D
```sh
git clone <this_repo> && cd <this_repo>

docker build -t  flask_logger .

docker run -d -8001:8001 flask_logger

docker ps
```

Example output:
```
CONTAINER ID        IMAGE               COMMAND             CREATED                   
d714c689dac2        flask_logger        "python app.py"     About a minute ago
```

## API Docs
1. Deploy docker container
2. Go to the '/' once deployed.
    - there is a swagger api doc that lives here!
