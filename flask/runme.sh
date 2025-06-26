#!/bin/bash
# Run this Flask app in debug mode so it will reload on file change
#

#env FLASK_DEBUG=1 flask run --host=0.0.0.0

# After refactor to move into app/__init.py__:
flask --app app --debug run
