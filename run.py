from uvicorn import run
from ennibee.seetings import DEBUG

if __name__ == "__main__":
    run("ennibee:app", debug=DEBUG, reload=True, workers=2)