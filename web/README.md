## Initialize environment

1. Install requirements
```shell
$ pip install -r requirements.txt
```

2. Make sure your python has sqlite3


3. Initialize database
```shell
$ ./manage.py init-db
```

You SHOULD see thesis.sqlite file in the instance directory.

## Run web server

```shell
$ ./manage.py run
```


## Run demo video capture application
```shell
$ python ./demo_vc.py
```

## The locations of all pages
1. Page1
    /page1

2. Page2
    /page2

## The location of all apis
1. Send person information from video capture application to web server
Request:
    GET /api/record?person=<the person name>
Response:
    1. Recorded
        Works well
    2. Skip
        You passed none as <person name>
    3. Off
        Record switch has been off

2. Query person information from page1 by Ajax
Request:
    GET /api/query
Response:
    1. <person name>
        Works well
    2. none
        No human face captured
