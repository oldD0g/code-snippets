# Simple webhook server

This is just a basic Flask server that you can use to run webhooks against.

The initial code (simple as it is) is pasted from https://towardsdatascience.com/intro-to-webhooks-and-how-to-receive-them-with-python-d5f6dd634476

Run the server using something like:

```
env FLASK_APP=__init__.py flask run --host=192.168.86.41
```

Then the /webhook target can be demonstrated using curl like:

```
curl -X POST -H 'Content-Type: application/json' -d '{"hello": "world" }' http://127.0.0.1:5000/webhook
```
