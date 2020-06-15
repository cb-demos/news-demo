#!/bin/bash
./wait-for-it.sh db:3306
gunicorn -b 0.0.0.0:5000 hn-grabber:app -w 2 --timeout 120 --reload