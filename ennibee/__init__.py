from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mongoengine import register_connection, disconnect
from ennibee.views.home import router
from ennibee.seetings import DEBUG

########################### initializing ennibee app########################
app = FastAPI(debug=DEBUG, title="EnniBee", 
description="Ennibee is an ecommerce website for fashion desigher", docs_url="/api/v1/docs", redoc_url=None)

############################ setting up app to use static files such as images, css, js files#########
app.mount("/static",   app= StaticFiles(directory="./ennibee/static"), name="static")

###################### connecting database on start up###################
@app.on_event("startup")
def initializeDb():
    register_connection(alias="core", db="ennibee", name="ennibee")

##################### disconnecting database on shutdown##############
@app.on_event("shutdown")
def uninitializeDb():
    disconnect(alias="core")



########################### all app routers #####################

app.include_router(router)