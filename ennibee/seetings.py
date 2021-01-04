from fastapi.templating import Jinja2Templates
DEBUG = True

######################### setting up where to get the app template i.e html files###########
template = Jinja2Templates(directory="./ennibee/templates").TemplateResponse