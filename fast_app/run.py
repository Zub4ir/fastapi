from logging import debug
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app="app:application", host='0.0.0.0', port=80, reload=True, log_level='debug', reload_includes='*.html')