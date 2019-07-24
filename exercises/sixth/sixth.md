# Sixth exercise
## Recap
In the last exercise we finally wrote a test for our endpoints and let it run with pytest. 

## Exercise
In this exercise we have a working example flask application in the file sixth.py and want to deploy it using Docker. Therefore you have an empty Dockerfile which you need to fill.

- Start your Dockerfile from the image `python:3.7.3-alpine`.
- Afterwards copy the requirements.txt and the sixth.py file to the image at the same path as it is now.
- To install all the dependencies, let the command run `pip3 install -r requirements.txt`as we also did at the beginning of all these exercises here.
- Expose the port 5000 of your flask application.
- Finally let your application run by calling in a CMD `python3 -m exercises.sixth.sixth`. Please note, that the CMD needs to be called in square brackets and each word needs to be separated.


Build your docker image with `docker build -t flask_sixth -f exercises/sixth/Dockerfile .` and let it run with `docker container run -p 5000:5000 flask_sixth `. Open up `localhost:5000/hello` in your browser and have a look, whether the container is working as expected.