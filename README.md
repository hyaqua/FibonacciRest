# FibonacciRest
 A REST API that computes and returns the nth number in the Fibonacci sequence

# Prerequisites
- Python 3.8 and newer

## Running the application
First we need to activate the python virtual environment
### Windows
```
python3 -m venv .\.venv
.\.venv\Scripts\activate.bat    
```
### Linux / MacOS
```
python3 -m venv .\.venv
source ./.venv/bin/activate
```
### Installing python dependencies
```
pip3 install -r requirements.txt
```

### Running the program
```
flask --app main run --port=8080
```

## Testing the application
To test the application you can navigate to this address in your browser
``localhost:8080/<n>`` where ``n`` is a number 

This should return a number that corresponds to the fibonacci number

So for example if ``n`` was ``10`` then you would get a response of ``55``

## Considerations
TODO
