#!/usr/bin/env python3

import os
from flask import Flask, request, current_app, g, make_response

app = Flask(__name__)

# Request Hook: before every request, we set the path of the app
@app.before_request
def app_path():
    # Store the current working directory (app path) in the 'g' object
    g.path = os.path.abspath(os.getcwd())

# Route for the home page
@app.route('/')
def index():
    # Get the host information from the request headers
    host = request.headers.get('Host')
    
    # Get the application name from the current_app object
    appname = current_app.name
    
    # Prepare the response body with host, app name, and the app path stored in 'g'
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    
    # Return the response with status code 200 and default headers
    return make_response(response_body, 200)

# Custom response handling with status code and headers
@app.route('/custom-response')
def custom_response():
    # Example of custom status code and headers in response
    response_body = 'This is a custom response'
    headers = {'Custom-Header': 'CustomValue'}
    return make_response(response_body, 202, headers)

# Example route that demonstrates request context handling
@app.route('/info')
def request_info():
    # Access request headers and return them as part of the response
    user_agent = request.headers.get('User-Agent')
    return f'<h1>Your user agent is {user_agent}</h1>'

# Example of redirect response
@app.route('/redirect-example')
def redirect_example():
    from flask import redirect
    return redirect('/')

# Example route that demonstrates aborting a request
@app.route('/abort-example')
def abort_example():
    from flask import abort
    abort(404)

# Run the Flask app with custom port and debug mode
if __name__ == '__main__':
    app.run(port=5555, debug=True)
