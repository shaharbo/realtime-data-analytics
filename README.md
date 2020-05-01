# Realtime Data Analytics

This project contains three modules.<br />
First module send in various iterations a json object contains path to invoice file, file format and table name to load file into.<br />
Second module is a consumer of the first queue - this module listen to the queue and every time a message arrives, it will load the file into the db and notify third queue with the response.<br />
Third module is a consumer of the second queue - this module analyze the data from db and presents a realtime graph.

In order to use this project you will need a running RabbitMQ server and SQLite database.

## Requirements

Please run the following command to install project dependencies
```
   pip install -r requirements.txt
```
## Start the project

In order to start the project, please run
```
   python Main.py
```

## Run tests

In order to perform tests, please run


