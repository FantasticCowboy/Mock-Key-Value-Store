# Mock-Key-Value-Store

A sleek key value store that can be easily configured

## Requirements

Python 3.10
Everything else in the requirements.txt

## Running in docker
make sure to have docker and docker-compose isntalled

Run the following command from the directory to start the service on localhost:5001
```
docker-compose up
```
## API

### Get
```
/get?key=<KEY, string>

return the corresponding value if it exists
```

### Set
```
/set

body={
    key : <KEY,string>,
    value : <VALUE,string>
}
```