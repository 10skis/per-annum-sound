#!/bin/sh
# Starts Per Annum Sound on port 8080, reachable from other devices on the home network.
cd "$(dirname "$0")"
exec .venv/bin/uvicorn server:app --host 0.0.0.0 --port 8080
