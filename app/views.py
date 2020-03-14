""" API and internal endpoints """
from flask import render_template, request
from app import app, git , data

DEBUG = False


@app.route('/')
def main():
    """Generate a blank homepage"""

    return ""

@app.route('/update_data')
def update_data():
    """Pull an updated copy of the repo and create a json blob of the requested data"""

    # pull from the master branch
    repo_version = "master"

    # clone the repo
    git.repo_setup(repo_version)

    # convert the csv to json
    data_json = data.generate_data()

    # cleanup your mess when you are through
    git.cleanup()

    return data_json
