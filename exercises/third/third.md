# Third exercise
## Recap
In the second exercise we created a simple webservice, which has no fixed URL, but can be called with a varying parameter. This parameter was also used for creating the response afterwards. 
## Exercise
In this exercise we will introduce the concept of blueprints. Blueprints are there for clustering endpoints to logical units. In this exercise you will create a new Blueprint object with the name `greeting`, the second parameter should be `__name__` parameter and the url-prefix `/greeting`.

Afterwards create three endpoints which attach to this blueprint. The endpoints should be `/hello/<name>`, `/gday/<name>`and `bonjour/<name>`and should accordingly return a response with the message `hello`, `gday` and `bonjour` with the given name and the status 200.

For further assistance have a look here: https://flask.palletsprojects.com/en/1.1.x/blueprints/

Hint: Do not forget to attach the blueprint to the app.

Run the application with `python3 -m exercises.third.third` and call the services under `localhost:5000/greeting/hello/yourName`, `localhost:5000/greeting/gday/yourName` and `localhost:5000/greeting/bonjour/yourName`
