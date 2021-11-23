# Theme
* default UIkit theme is in node_modules/@vuikit/theme/dist/vuikit.css


## Git 
* add remote repo to track origin
`
git remote add origin https://github.com/cahillsf/funvue-project.git
git branch -M main
git push -u origin main
`

## Flask App
from /Users/scahill/Desktop/funvue-project/flask-server
- activate virtual environment: `source .venv/bin/activate`

run the app:
- python app.py
- ddtrace-run python app.py

to get idle: `idle` from terminal

https://github.com/tensorflow/tensorboard/issues/1566

## Mongodb 
cd docker-entrypoint-initdb.d


mongoimport -u "root" -p "example" --type csv --authenticationDatabase admin -d sitecontent -c cards --headerline homepage.csv

./mongo-db/mongo-db-init-files
* mongo -uroot -pexample

from the container bash: `mongosh --username root --password example --authenticationDatabase admin`

`mongosh --username flask-role --password toor --authenticationDatabase sitecontent`

use sitecontent
var col = db.cards
col.find()


#  db.getCollection('cards').find()

use sitecontent
db.createCollection('cards')
var myCards=
	[
		{
            '_id': 0,
            'title':'CardOne',
            'msg':'testOne',
            'animation':'fade-up'
          },
          {
            '_id': 1,
            'title':'CardTwo',
            'msg':'testTwo',
            'animation':'fade-up'
          },
          {
            '_id': 2,
            'title':'CardThree',
            'msg':'testTwo',
            'animation':'fade-up'
          },
          {
            '_id': 3,
            'title':'CardFour',
            'msg':'testTwo',
            'animation':'fade-up'
          },

	];

	db.cards.insert(myCards);


## ToDo

* better routing--> can i create a router-link within a different element?

* styling-- figure out a way to keep theming (currently in nodemodules which are in the .gitignore)

* hide dropdown menu after user has returned to full page view so that when the browser size is reduced below the breakpoint, it will not be visible

