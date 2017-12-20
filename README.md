## Artvark - (Shazam for art)

Web application which uses machine learning to identify the artist from a previously unseen image of a painting.

### Getting started

We hosted the web app locally so to get it up and running you will need to:

* Install Python 3
```
brew install python3
brew postinstall python3
```
* Install numpy and scipy
```
pip3 install --user numpy
pip3 install --user scipy
```
* Install Scikit-Learn
```
pip3 install -U scikit-learn
```

* Install Scikit Image
```
pip install -U scikit-image
```
* Install Django
```
pip3 install django
```
Clone this repo and navigate to ./imageuploader/manage.py

Apply the migrations

```
python3 manage.py migrate
```
Run the server

```
python3 manage.py runserver
```

Open your browser and head to http://127.0.0.1:8000/images

Upload an image of a painting and see how it does!

## Built with

* [Python3](https://www.python.org/download/releases/3.0/)
* [Django](https://www.djangoproject.com/) - Web Framework for Python
* [PyTest](https://docs.pytest.org/en/latest/) - Testing Framework
* [Scikit Image](http://scikit-image.org/) - Image Processing in Python
* [Scikit Learn](http://scikit-learn.org/stable/) - Machine Learning in Python

## Overview of Project

The project was Ed's idea and we joined together as a group of four to work on it as our final project in Weeks 11 and 12 of Makers Academy. The aim was to learn Python, learn about machine learning and have fun. We managed loads of all three!

In rough chronolgoical order we focussed on:

* MVP - Using Python Scripts to scrape images, scikit image to process them and skicit learn to generate a model and make a prediction.
* Improving test coverage
* Accuracy improvement by altering the image data passed to the ML algo and changing the ML algos
* Persisting the model
* Building the Django Framework with TDD
* Joining the Web App with the ML logic
* Styling and User experience

## Where would we take it next?

The aspiration would certainly have been to break into the Scikit Learn machine learning algorithms and replace one of them with our own.
Even if it was just a very 'simple' perceptron it would have given us really valuable insight into the detail of ML algos.

It would also be extremely exciting to continue the work on image processing to either use more of the feature extraction functionality of scikit learn to try and improve accuracy and also to perhaps pivot this project to try and identify whether there was a face in a painting. 

## Authors

* Tom Spencer
* Ed Lowther
* Rory Collins
* Tim Jones
