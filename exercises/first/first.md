# First exercise
## Installation
To be able to participate in this exercise, please install the dependencies from root folder with this command: `pip3 install -r requirements.txt`. If you do not have pip on the command line available, please follow the installation instructions at the python website.

## General
In this workshop you should fill out the exercises located in the exercises folder. Therefore each package has an empty python file, where you should put the solution. Solutions can be found inside the solutions folder.

## Exercise
The documentation for flask can be found here: https://flask.palletsprojects.com/en/1.1.x/

In the first exercise you should create two simple webservices. 

First of all create an application using this snippet 
```
from flask import Flask
app = Flask(__name__)
```
also create a main function which looks like this:
```
if __name__ == "__main__":
    app.run(host="0.0.0.0")
```

Please be aware, that the main function has to be at the end of the file, otherwise the app will not work correctly.

Now you can run the empty app, without any webservice provided using `python3 -m exercises.first.first`.

Lets create some webservices, to have them available on running the app again.

The first webservice should be available with the URL `/hello` and is of type GET. It should deliver back a Response object (from flask package) with the status `status.HTTP_200_OK` and the message `Hello Flask!`. A response object is created using `Response('your message', status.HTTP_200_OK)`. Have a look at the QuickStart page how to set the Path.

The second webservice is of type POST and available with the URL `/hello/post`. It should return a Response object with the message `b"The data sent is: "+request.data` and also status 200. How to create POST calls, you can have a look here: https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods

You can test the post request with curl. The snippet therefore is: `curl -H "Content-Type: application/json" -X POST -d 'My Data to send' http://localhost:5000/hello/post`

Run the application with `python3 -m exercises.first.first`
