# Django Rest API

To get started download the project `git clone https://github.com/medoedoff/restapi.git`
After go to the project directory `cd directory/where/project/downloaded/restapi-master`
Install requirement packages for work (you shoud have python3 and pip) `pip install requirements.txt`

Run django server `python3 manage.py runserver`
Open second terminal to test our Rest API server

### GET
`curl localhost:8000/library/` -All books in Library
`curl localhost:8000/library/1/` -Detail book in Library

### POST (only for authenticated users)
`curl -u satori:satori -d author=TestAuthor localhost:8000/library/`

### PUT (only for authenticated users)
`curl -u satori:satori -X PUT -d author=TestUserChanged http://localhost:8000/library/4/`

### DELETE (only for authenticated users)
`curl -u satori:satori -X DELETE localhost:8000/library/4/`

### Notice
You have only 10 requests per 10 minutes, to change it, go to djapi/settings.py file, on line 121 find DEFAULT_THROTTLE_RATES, below you will see `'anon':10/m` and `user:10/m`. Anon - not authenticated, User - authenticated. 10 - means how much request anon or user will have, m - means per minute. You can change it how it will comfortable for you.

P.S Sorry for my English :)
