#!/bin/sh
mongoimport -u "root" -p "example" --type csv --authenticationDatabase admin -d sitecontent -c cards --headerline /docker-entrypoint-initdb.d/homepage.csv