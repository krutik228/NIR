#!/bin/bash
service mysql start

python3 app/main.py

echo "main.py is running"