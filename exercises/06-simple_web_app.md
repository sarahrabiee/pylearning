# Simple Web App

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a simple python web framework. In this
exercise, we will use it to build a basic web app. Before we can do that, we need to set up a few
things.

## Setting up a virtual environment

To use flask, we need to install it as a python package. It is good practice to install it in a
virtual environment separate from any other apps that you might be working on. To create a python
virtual environment, you can run:
```bash
$ python -m venv venv
```
This will create a new directory called `venv` where the virtual environment will be stored. This should not be committed to git, so you will see that directory included in the `.gitignore`
file.

Next we need to activate the virtual environment. To do that, run:
```bash
$ source venv/bin/activate
```

You will need to do that every time you work on this project in a new terminal. When a virtualenv is active, you can run `deactivate` to deactivate it.

## Installing the Flask package

```bash
$ pip install Flask
```

## Building the app

To get a basic flask app up and running, follow the [Quickstart guide](https://flask.palletsprojects.com/en/1.1.x/)

## Running the app

Assuming your app is in a file called `06-simple_web_app.py`, you can run the server as follows:
```bash
$ FLASK_APP=06-simple_web_app.py flask run
```
This will start the server on `localhost (127.0.0.1)` on port `5000`.

## Calling the app

When the server is running, you can call it either by opening a browser and typing
`localhost:5000?name=Sara` in the address bar, or by running:
```bash
$ curl localhost:5000?name=Sara
```

## Exercise

Create a simple web app that will take a single request parameter called `name` and respond with a
greeting: `Hello, <name>!`.

## Example

```bash
$ curl localhost:5000?name=Sara
Hello, Sara!
```
