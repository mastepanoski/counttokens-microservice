#!/bin/bash

set -e

echo "Installing test dependencies..."
pip install pytest pytest-cov requests

echo "Running tests..."
pytest --cov=counttokens src/

echo "Generating coverage report..."
coverage html

echo "Done!"
