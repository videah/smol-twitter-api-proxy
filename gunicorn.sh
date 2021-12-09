#!/bin/sh
gunicorn --chdir twitter_api_proxy app:app -w 2 --threads 2 -b 0.0.0.0:80
