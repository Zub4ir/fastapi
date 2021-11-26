# FastAPI

This is a FastAPI Docker-Compose project with Nginx. I prefer creating a docker-compose project to accomodate additional project containers.

_***Important notes in notes_

## To Run

When testing and developing on this projetc, it is possible to run in debug (non-production) mode environment. This mode does not use Docker functionality.

```bash
# dev mode
# within root folder
python fast_app/run.py 
```

If on localhost, go to http://localhost to access the first page.

In production mode, run using Docker

```bash
# Navigate to root folder and run
docker-compose up --build -d
```

If on localhost access via http://localhost.

## Project Setup Notes

This Docker poject has two containers, FastAPI on port 8000 and Nginx on port 80/443 listening for requests. The FastAPI component is in a Router format for easy extension.

Please enable authentication if deployed in cloud.