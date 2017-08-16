#!/bin/bash

set -e

# lsof -t -i:7000 | xargs kill

# Set absolute path
cd "/Users/glamcocks/playa-sign"

python run.py 