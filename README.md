# Stock Exchange Prediction using Machine Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/lokesh45/StockPrediction.svg?branch=master)](https://travis-ci.org/lokesh45/StockPrediction)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![DOI](https://zenodo.org/badge/301582156.svg)](https://zenodo.org/badge/latestdoi/301582156)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Video

Below is the video which describes our project's idea

[![Stock Market Predictions using Machine Learning](https://github.com/lokesh45/StockPrediction/blob/master/Video.png)](https://youtu.be/7ZUhyTCfLUM)

### Go through the wiki page containing project details and user manual.

## [Wiki](https://github.com/lokesh45/StockPrediction/wiki)

## Test Plan

1. Go to [TestPlan](https://docs.google.com/spreadsheets/d/1rQDUvgM1uNTLeklLOQzoprsNrLaTmgU-nL8uw30S_xw/edit#gid=632817659) spreadsheet.
2. Assign keys to each user.
3. Record the data generated from the participant. Each participant will perform following activities.
   1. Analyse the project based on Ease of use, Accuracy, Cost, Range of choice.
   2. Compare current project with other tools available online (Wallet Investor, AIStockFinder)
   3. Report bugs(if found)
   4. Review the project on scale 1(Low) to 5(High).
4. Utilize the data and analyse the feedback received from each participant.
5. Generate aggregated rating for the entire project based on Ease of use, Accuracy, Cost, Range of choice.

## Web App Screenshots<br>

![](https://github.com/lokesh45/StockPrediction/blob/master/doc/StockGraph.PNG)<br>
![](https://github.com/lokesh45/StockPrediction/blob/master/doc/loginPNG.PNG)<br>
![](https://github.com/lokesh45/StockPrediction/blob/master/doc/webapp1.PNG)<br>
![](https://github.com/lokesh45/StockPrediction/blob/master/doc/Register.PNG)<br>
![](https://github.com/lokesh45/StockPrediction/blob/master/doc/Choose%20Stock.PNG)

## Technologies and Tools

<b>Language</b>: Python 3, HTML, CSS

<b>Web Application Framework</b>: [Docker](https://www.docker.com/), [Flask](https://github.com/pallets/flask/)

<b>Test Framework</b>: [pytest](https://github.com/pytest-dev/pytest)

<b>Database</b>: [MySQL](https://www.mysql.com/)

<b>Tools</b>: [Visual Studio Code](https://code.visualstudio.com/)

<b>Syntax Checker & Style Checker</b>: [flake8](https://gitlab.com/pycqa/flake8), [pylint](https://github.com/PyCQA/pylint/)

<b>Code Formatter</b>: [black](https://github.com/psf/black), [prettier](https://github.com/prettier/prettier)

<b>Version Control</b>: git

# Installation Guide

## Running the application using Docker (Recommended for testers)

```
$ cd projDir
$ docker build -t csc510/p2:latest .
$ docker run -p 5000:5000 csc510/p2:latest
```

You can now find the app at http://localhost:5000/auth/login.

## Running the application using Flask (for development)

Insure that you have flask installed, then initialize the default flask db and run the app.

```
$ cd projDir
$ set FLASK_APP=flaskr
$ flask init-db
$ flask run
```

# Application Overview

<img src="/doc/ApplicationStructure1.png" />

# Database Schema

<img src="/doc/Schema.png" />
