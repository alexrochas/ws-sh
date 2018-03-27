# Webserver to Shell Script
> Minor webserver with python to run shell scripts

## How-to
Start webserver
```sh
~/[path_to_repository]$ python server.py
```

Hit `http://localhost:8000/jobs/start.py`:
```sh
~/[path_to_repository]$ curl http://localhost:8000/jobs/start.py
```

Curl will return an OK and the python server will log job script outputs.

## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas)
