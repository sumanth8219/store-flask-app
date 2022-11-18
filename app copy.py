import uuid
from flask_smorest import abort
from flask import Flask, request
from db import db

from resource.item import ItemBlueprint
from resource.Store import StoreBlueprint

app = Flask(__name__)
app.config["PROPOGATE_EXCEPTIONS"] = True
app.config["API_TITLE"]="Stores Rest API"
app.config["API_VERSION"]="V1.0"
app.config["OPENAPI_VERSION"]="3.0.3"
app.config["OPENAPI_SWAGGER_UIPATH"]="/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

