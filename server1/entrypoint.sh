#!/bin/bash
service php7.4-fpm start
service nginx start
tail -f /var/log/nginx/access.log /var/log/nginx/error.log

python3 app/main.py

echo "main.py is running"