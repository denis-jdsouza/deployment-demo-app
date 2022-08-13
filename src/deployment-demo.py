"""
Simple web application which displays 'App version' and 'K8s Pod name'.
Useful for demo/testing deployment strategies (blue-green, rolling, canary, etc.), request routing, load-balancer algorithms, session stickiness, etc.
"""

import os
from flask import Flask
from waitress import serve

app_version = 'v1.0' # variable for demo/testing 'deployment strategies' (ie. simulate a new app version release)

# Retrive env variable
pod_name = os.getenv('MY_POD_NAME', '"MY_POD_NAME" env variable undefined')

def web_api():
    """ Web API function """
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def return_podname_appversion():
        return f'Pod-Name: {pod_name} <br/> App-Version: {app_version}'

    @app.route('/version', methods=['GET'])
    def return_appversion():
        return f'App-Version: {app_version}'

    @app.route('/pod', methods=['GET'])
    def return_podname():
        return f'Pod-Name: {pod_name}'

    return app

if __name__ == "__main__":
    serve(web_api(), port='8080')
