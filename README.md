# Stock Exchange Prediction using Machine Learning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Build Status](https://travis-ci.org/lokesh45/StockPrediction.svg?branch=master)](https://travis-ci.org/lokesh45/StockPrediction)

[![DOI](https://zenodo.org/badge/301582156.svg)](https://zenodo.org/badge/latestdoi/301582156)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

## Video

Below is the video which describes our project's idea

[![Stock Market Predictions using Machine Learning](https://github.com/lokesh45/StockPrediction/blob/master/Video.png)](https://youtu.be/7ZUhyTCfLUM)

## Why choose this project:

- The project provides visualisation of stocks of 2000+ company markets and helps in making prediction for the next time period.
- Modular architecture
- Scalable design
- You will be able to explore data analysis, predictive modelling and explore the integration of NLP functionality.
- You can scale the project to use different predictive models to compare the efficiencies as well as compare different stocks to make the right decision to invest.

## Technologies and Tools

<b>Language</b>: Python 3, HTML, CSS

<b>Libraries</b>: Flask, click, yfinance, matplotlib, Werkzeug, pandas, numpy, get_all_tickers, pytest, scikit_learn.

<b>Web Application Framework</b>: Flask

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
