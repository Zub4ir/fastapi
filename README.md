# FastAPI

This is FastAPI Docker-Compose project with NginX. I prefer creating a docker-compose project to accomodate additional project containers.

## To Run

When testing and developing on this projetc it is possible to run in debug (non-production) mode environment. This mode does not use Docker functionality.

```bash
# dev mode
# within root folder
python fast_app/run.py 
```

If on localhost, go to http://localhost/ to access the first page.

In production mode, run using Docker

```bash
# Navigate to root folder and run
docker-compose up --build -d
```

## Project Setup Notes

Hello
