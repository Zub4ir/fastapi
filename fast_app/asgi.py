import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="app.main:application", host="0.0.0.0", port=8001, reload=True)