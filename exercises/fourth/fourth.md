# Fourth exercise
## Recap
In the last exercise we created some blueprints, to cluster endpoints together.
## Exercise
In this exercise we will serve static files as the answer of an endpoint. These files need to be inside a folder called `static`. So therefore create a static html file or copy the static folder from solutions/fourth.

To serve static files, simply add a second parameter to the app creation. The parameter is called `static_url_path` and needs to be set to the path of the static folder, relative to the python file with the app inside. 

Now create an endpoint for the root-path and return `app.send_static_file('nameOfTheFile.html')`. This will then return the static file as answer to the endpoint.

Run the application with `python3 -m exercises.fourth.fourth`.
