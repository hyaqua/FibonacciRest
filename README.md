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

### Containerization
Containerizing this API is pretty straightforward and could enhance the aase of deploying and running the application consistently across many different environments.
By using Docker and the official python base image, you can package the app and all of its dependencies into a single image,
ensuring that it always runs the same way.
### Continuous Integration/Continuous Deployment
#### Continuous Integration
We could use GitHub actions, and the pytest framework to be able to test and validate the correctness of the API ensuring that the app's logic and endpointss work as expected.

#### Continuous Deployment
After passing tests the app could be deployed to a staging environment for further testing and validation in a production-like environmont

Once the API is validated in staging it can be manually approved for deployment to the production environment. This ensures that only stable and tested versions of the Fibonacci API are released.
### Monitoring
For monitoring the application an established flask dashboard could be used, such as ```Flask-MonitoringDashboard``` which has performance and utilization monitoring, request and enpoint profling, and much more.

But for a simple API such as this, a dashboard like that may be too much. A better suited method could be just to use the built-in python logging module
The most important things to monitor would be the requests that are sent, what they return and the fibonacci function calls
### Scalability
As it is the API is already very scalable, it follows a stateless design meaning that each request is independent of others. This makes it easier to scale it horizontally, by adding more instances of the API server.

Because this API currently uses a recursive function that calls two instances of itself each time it could become very resource intensive, so we could implement caching of results of the fibonacci sequences that have already been computed. By caching the frequently requested sequences in-memory, the load on the API and the response times could be significantly reduced.
