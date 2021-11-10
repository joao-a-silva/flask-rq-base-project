#!/bin/bash

if [ "$SERVICE" = "api" ]
then
    echo "Running web..."
    python run.py
else
    echo "Running worker..."
    python run_worker.py
fi
