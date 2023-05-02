#!/bin/python
from counttokens import num_tokens_from_messages
from werkzeug.exceptions import HTTPException
from flask import Blueprint, request, jsonify, json

counttokensAPI = Blueprint('counttokensAPI', __name__)

"""
Example:

curl -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' -i http://localhost:5000/tokens/count --data '{"messages":[{"role": "system", "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English."},{"role": "system", "name":"example_user", "content": "New synergies will help drive top-line growth."},{"role": "system", "name": "example_assistant", "content": "Things working well together will increase revenue."},{"role": "system", "name":"example_user", "content": "Let'\''s circle back when we have more bandwidth to touch base on opportunities for increased leverage."},{"role": "system", "name": "example_assistant", "content": "Let'\''s talk later when we'\''re less busy about how to do better."},{"role": "user", "content": "This late pivot means we don'\''t have time to boil the ocean for the client deliverable."}],"model": "gpt-3.5-turbo-0301"}'
"""

@counttokensAPI.route("/tokens/count", methods=["POST"])
def count_tokens():
    data=request.get_json()
    total=num_tokens_from_messages(data['messages'], data['model'])
    return jsonify({
        "total": total
    })

@counttokensAPI.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response