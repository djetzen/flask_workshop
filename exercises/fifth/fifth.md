# Fifth exercise
## Recap
In the last exercise we created an endpoint, which served static files. 
## Exercise
In this exercise, we will finally get to unit-testing our application, especially checking if the hello endpoint is available. 

Have a look at the file fifth.py, which contains a very simple implementation of the hello endpoint. 

For testing purpose we here use pytest, documentation can be found here: https://pytest.org/en/latest/. Tests always should start with `test_` and can be run using `pytest -v` for the whole project.

The test can be done here by creating a new app and registering the blueprint `greeting`. Just import the blueprint by writing `from exercises.fifth.fifth import greeting`. Inside the method, create a new test client by calling `app.test_client()` and perform a get request at the endpoint from fifth. 

Delivered back is a response object, which can be checked for the status_code and the data, using an assert. 

Run your test with `pytest -v`. 