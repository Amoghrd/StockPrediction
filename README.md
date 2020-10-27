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

<b>Libraries</b>: Flask, click, yfinance, matplotlib, Werkzeug, pandas, numpy, get_all_tickers, pytest, scikit_learn.

<b>Web Application Framework</b>: Docker, Flask

<b>Test Framework</b>: pytest

<b>Database</b>: SQLite

<b>Tools</b>: Visual Studio Code

<b>Syntax Checker & Sytle Checker</b>: pylint (VSCode Python v2020.8.109390 Extension)

<b>Code Formatter</b>: autopep8 (VSCode Python-autopep8 v1.0.2)

<b>Version Control</b>: git

# Installation Guide

## Running the application using Docker(Recommended for testers)

1. Navigate to the project directory with the Dockerfile
2. Docker build -t csc510/p1:latest .
3. Docker run -p 5000:5000 csc510/p1:latest
4. The app should be running on http://localhost:5000/auth/login

# Running the application using Flask(for developers)
## For Mac/Ubuntu

Install Flask using pip - pip/pip3 install flask

cd to project directory

export FLASK_APP=flaskr

flask init-db

## For Windows

Install Flask using pip - pip/pip3 install flask

cd to project directory

set FLASK_APP=flaskr

flask init-db

## Run

To run just do the following

flask run

# Application Overview

<img src="/doc/ApplicationStructure.png" />

# Database Schema

<img src="/doc/Schema.png" />

