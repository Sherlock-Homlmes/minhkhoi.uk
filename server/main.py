# libraries
import uvicorn

# local
from core.conf import *
from core.event_handler import *
from core.routers import *
from all_env import ENVIRONMENT

if __name__ == '__main__':
  if ENVIRONMENT != "docker": 
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)