import os

from flask import Flask, request, Response
from src.disk_manager import DiskManager
from pathlib import Path
from src.validation import validate_form, validate_query
import argparse
import json

def create_app(config_path):
    app = Flask(__name__, instance_relative_config=True)
    app.config.root_path = "."
    if not app.config.from_file(config_path, load=json.load):
        assert False, "Could not read config!"    

    # Directory where DiskManager will store all the data
    data_dir = app.config["DATA_DIRECTORY"]


    # Mock DB
    manager = DiskManager(Path(data_dir))


    # Register Routes
    @app.route('/live', methods=["GET"])
    def live():
        return "live"

    @app.route('/get', methods=["GET"])
    @validate_query([("key", str)])
    def get(*args, **kwargs):
        ret = manager.read(request.args.get("key")) 
        return ret if ret is not None else Response(status=404)
    @app.route('/set', methods=["POST"])
    @validate_form([("key", str), ("value", str)])    
    def set(*args, **kwargs):        
        manager.write(request.form.get("key"), request.form.get("value"))
        return Response(status=200)
    

    return app